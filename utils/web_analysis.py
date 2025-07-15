# This Python file uses the following encoding: utf-8
import requests
import json
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, parse_qs
from robotexclusionrulesparser import RobotExclusionRulesParser

class WebAnalyzer:
    @staticmethod
    def get_headers():
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    @staticmethod
    def analyze_sitemap(sitemap_url, progress_callback=None):
        try:
            if progress_callback:
                progress_callback(10)  # Download started
                
            response = requests.get(sitemap_url, headers=WebAnalyzer.get_headers())
            response.raise_for_status()
            
            if progress_callback:
                progress_callback(20)  # Download completed
            
            content_type = response.headers.get('content-type', '').lower()
            if 'xml' not in content_type:
                return f"Error: Content is not valid XML (Content-Type: {content_type})"

            root = ET.fromstring(response.content)
            namespaces = {
                'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                'xhtml': 'http://www.w3.org/1999/xhtml'
            }

            if progress_callback:
                progress_callback(30)  # XML parsing completed

            results = ["URL\threflang URL\threflang\tSitemap"]
            processed_urls = 0
            total_progress_remaining = 70  # 70% remaining for processing

            if root.tag.endswith('sitemapindex'):
                sitemaps = root.findall('sm:sitemap', namespaces)
                total_sitemaps = len(sitemaps)
                progress_per_sitemap = total_progress_remaining / (total_sitemaps or 1)
                
                for i, sitemap in enumerate(sitemaps, 1):
                    try:
                        sitemap_url = sitemap.find('sm:loc', namespaces).text
                        sitemap_name = urlparse(sitemap_url).path.split('/')[-1]
                        
                        if progress_callback:
                            progress_callback(30 + int(i * progress_per_sitemap))
                            
                        sitemap_response = requests.get(sitemap_url, headers=WebAnalyzer.get_headers())
                        sitemap_response.raise_for_status()
                        sitemap_root = ET.fromstring(sitemap_response.content)
                        
                        new_results = WebAnalyzer.process_urlset(sitemap_root, sitemap_name, namespaces)
                        results.extend(new_results)
                        processed_urls += len(new_results)
                        
                    except Exception as e:
                        results.append(f"Error processing {sitemap_url}: {str(e)}")
            else:
                new_results = WebAnalyzer.process_urlset(root, "main", namespaces)
                results.extend(new_results)
                processed_urls += len(new_results)
                
                if progress_callback:
                    progress_callback(100)  # Processing completed

            # Add summary
            summary = f"\nSummary:\n{processed_urls} URLs processed"
            if root.tag.endswith('sitemapindex'):
                summary += f"\n{len(sitemaps)} sitemaps analyzed"
            
            results.append(summary)
            return "\n".join(results)

        except requests.RequestException as e:
            return f"HTTP request error: {str(e)}"
        except ET.ParseError as e:
            return f"XML parsing error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    @staticmethod
    def process_urlset(root, sitemap_name, namespaces):
        results = []
        for url in root.findall('sm:url', namespaces):
            try:
                page_url = url.find('sm:loc', namespaces).text
                hreflangs = url.findall('.//xhtml:link[@rel="alternate"]', namespaces)

                if hreflangs:
                    for hreflang in hreflangs:
                        hreflang_url = hreflang.get('href')
                        hreflang_lang = hreflang.get('hreflang')
                        results.append(f"{page_url}\t{hreflang_url}\t{hreflang_lang}\t{sitemap_name}")
                else:
                    results.append(f"{page_url}\t\t\t{sitemap_name}")
            except Exception as e:
                results.append(f"Error processing URL: {str(e)}")
        return results

    @staticmethod
    def analyze_robots_txt(url):
        try:
            response = requests.get(url, headers=WebAnalyzer.get_headers())
            response.raise_for_status()
            return response.content.decode('utf-8')
        except Exception as e:
            return f"Error retrieving robots.txt: {str(e)}"

    @staticmethod
    def check_urls_against_robots(urls, robots_content, user_agent):
        parser = RobotExclusionRulesParser()
        parser.parse(robots_content)
        
        results = []
        for url in urls:
            url = url.strip()
            if not url:
                continue
                
            is_allowed = parser.is_allowed(user_agent, url)
            results.append((url, is_allowed))
            
        return results

    @staticmethod
    def decrypt_botify_filter(url):
        try:
            parsed_url = urlparse(url)
            if parsed_url.netloc != "app.botify.com":
                return "Error: URL must be a Botify URL (app.botify.com)"

            if not parsed_url.query:
                return "Error: No filter parameters found in URL"

            query_params = parse_qs(parsed_url.query)
            results = []

            if 'context' in query_params:
                try:
                    filter_json = json.loads(query_params["context"][0])
                    results.append("---Filters---")
                    results.append(json.dumps(filter_json, indent=4, ensure_ascii=False))
                except json.JSONDecodeError:
                    results.append("Error: Context filter is not valid JSON")

            if 'explorerFilter' in query_params:
                try:
                    columns_json = json.loads(query_params["explorerFilter"][0])
                    results.append("\n---Columns---")
                    results.append(json.dumps(columns_json, indent=4, ensure_ascii=False))
                except json.JSONDecodeError:
                    results.append("Error: Explorer filter is not valid JSON")

            if not results:
                return "No filters found in URL"

            return "\n".join(results)
        except Exception as e:
            return f"Error decoding filter: {str(e)}"

    @staticmethod
    def extract_query_params(urls):
        query_param_dict = {}
        for url in urls:
            parsed_url = urlparse(url)
            query_string = parsed_url.query
            query_params = parse_qs(query_string)
            
            for param_name in query_params:
                if param_name not in query_param_dict:
                    query_param_dict[param_name] = 1
                else:
                    query_param_dict[param_name] += 1
        return query_param_dict 