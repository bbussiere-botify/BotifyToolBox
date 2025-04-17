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
            response = requests.get(sitemap_url, headers=WebAnalyzer.get_headers())
            response.raise_for_status()
            
            if 'xml' not in response.headers.get('content-type', '').lower():
                return "Le contenu n'est pas un XML valide"

            root = ET.fromstring(response.content)
            namespaces = {
                'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                'xhtml': 'http://www.w3.org/1999/xhtml'
            }

            results = ["URL\threflang URL\threflang\tSitemap"]

            if root.tag.endswith('sitemapindex'):
                sitemaps = root.findall('sm:sitemap', namespaces)
                total_sitemaps = len(sitemaps)
                
                for i, sitemap in enumerate(sitemaps, 1):
                    sitemap_url = sitemap.find('sm:loc', namespaces).text
                    sitemap_name = urlparse(sitemap_url).path.split('/')[-1]

                    try:
                        sitemap_response = requests.get(sitemap_url, headers=WebAnalyzer.get_headers())
                        sitemap_response.raise_for_status()
                        sitemap_root = ET.fromstring(sitemap_response.content)
                        
                        results.extend(WebAnalyzer.process_urlset(sitemap_root, sitemap_name, namespaces))
                        
                        if progress_callback:
                            progress = int((i / total_sitemaps) * 100)
                            progress_callback(progress)
                    except Exception as e:
                        results.append(f"Erreur lors du traitement de {sitemap_url}: {str(e)}")
            else:
                results.extend(WebAnalyzer.process_urlset(root, "main", namespaces))

            return "\n".join(results)

        except Exception as e:
            return f"Erreur lors de l'analyse du sitemap: {str(e)}"

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
                results.append(f"Erreur lors du traitement d'une URL: {str(e)}")
        return results

    @staticmethod
    def analyze_robots_txt(url):
        try:
            response = requests.get(url, headers=WebAnalyzer.get_headers())
            response.raise_for_status()
            return response.content.decode('utf-8')
        except Exception as e:
            return f"Erreur lors de la récupération du robots.txt: {str(e)}"

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
                return "Erreur: L'URL doit être une URL Botify (app.botify.com)"

            if not parsed_url.query:
                return "Erreur: Aucun paramètre de filtre trouvé dans l'URL"

            query_params = parse_qs(parsed_url.query)
            results = []

            if 'context' in query_params:
                try:
                    filter_json = json.loads(query_params["context"][0])
                    results.append("---Filters---")
                    results.append(json.dumps(filter_json, indent=4, ensure_ascii=False))
                except json.JSONDecodeError:
                    results.append("Erreur: Le filtre context n'est pas un JSON valide")

            if 'explorerFilter' in query_params:
                try:
                    columns_json = json.loads(query_params["explorerFilter"][0])
                    results.append("\n---Columns---")
                    results.append(json.dumps(columns_json, indent=4, ensure_ascii=False))
                except json.JSONDecodeError:
                    results.append("Erreur: Le filtre explorerFilter n'est pas un JSON valide")

            if not results:
                return "Aucun filtre trouvé dans l'URL"

            return "\n".join(results)
        except Exception as e:
            return f"Erreur lors du décodage du filtre: {str(e)}"

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