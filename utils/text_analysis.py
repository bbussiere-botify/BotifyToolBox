# This Python file uses the following encoding: utf-8
import re
import csv
import nltk
import colorsys
import pandas as pd
from collections import defaultdict
from nltk.corpus import stopwords
from utils.file_handlers import FileHandler

class TextAnalyzer:
    @staticmethod
    def clean_and_extract_words(text, language='english'):
        try:
            stop_words = set(stopwords.words(language))
        except LookupError:
            nltk.download(f'stopwords_{language}')
            stop_words = set(stopwords.words(language))
            
        words = text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return re.findall(r'\b\w+\b', ' '.join(filtered_words))

    @staticmethod
    def analyze_keywords(file_path, language='english', progress_callback=None):
        word_stats = defaultdict(lambda: {
            'occurrences': 0,
            'total_clicks': 0,
            'total_impressions': 0
        })

        with FileHandler.open_file(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)  # Skip sep=,
            headers = next(reader)  # Get headers

            # Trouver les indices des colonnes nécessaires
            keyword_idx = headers.index('Keyword')
            clicks_idx = headers.index('Clicks')
            impressions_idx = headers.index('Impressions')

            # Compter le nombre total de lignes
            total_rows = sum(1 for _ in reader)
            csvfile.seek(0)  # Retourner au début du fichier
            next(reader)  # Skip sep=,
            next(reader)  # Skip headers

            for i, row in enumerate(reader, 1):
                try:
                    keywords = TextAnalyzer.clean_and_extract_words(row[keyword_idx], language)
                    clicks = int(row[clicks_idx])
                    impressions = int(row[impressions_idx])
                    
                    for word in keywords:
                        word_stats[word]['occurrences'] += 1
                        word_stats[word]['total_clicks'] += clicks
                        word_stats[word]['total_impressions'] += impressions

                    if progress_callback:
                        progress = int((i / total_rows) * 100)
                        progress_callback(progress)
                except (IndexError, ValueError) as e:
                    print(f"Erreur lors du traitement de la ligne {i}: {str(e)}")
                    continue

        return TextAnalyzer.create_word_stats_dataframe(word_stats)

    @staticmethod
    def create_word_stats_dataframe(word_stats):
        df = pd.DataFrame.from_dict(
            word_stats,
            orient='index',
            columns=['occurrences', 'total_clicks', 'total_impressions']
        ).reset_index()

        df.columns = ['Word', 'Occurrences', 'Total_Clicks', 'Total_Impressions']
        df = df.sort_values('Occurrences', ascending=False)
        df['Avg_CTR'] = (df['Total_Clicks'] / df['Total_Impressions'] * 100).round(2)
        
        return df

    @staticmethod
    def generate_word_cloud_html(df, max_words=100):
        df_sorted = df.sort_values('Occurrences', ascending=False).head(max_words)
        max_occurrences = df_sorted['Occurrences'].max()
        max_clicks = df_sorted['Total_Clicks'].max()

        def normalize_size(occurrences, max_val=max_occurrences, min_size=10, max_size=50):
            return min_size + (occurrences / max_val) * (max_size - min_size)

        def generate_color(clicks, max_val=max_clicks):
            normalized = clicks / max_val
            h = (1 - normalized) * 0.4
            l = 0.5
            s = 0.7
            r, g, b = [int(x * 255) for x in colorsys.hls_to_rgb(h, l, s)]
            return f'rgb({r},{g},{b})'

        word_cloud_items = []
        for _, row in df_sorted.iterrows():
            size = int(normalize_size(row['Occurrences']))
            color = generate_color(row['Total_Clicks'])
            title = f"Mot: {row['Word']}\nOccurrences: {row['Occurrences']}\nClics: {row['Total_Clicks']}\nCTR: {row['Avg_CTR']}%"
            word_item = f'<span class="word" style="font-size: {size}px; color: {color};" title="{title}">{row["Word"]}</span>'
            word_cloud_items.append(word_item)

        return TextAnalyzer.get_word_cloud_template(' '.join(word_cloud_items))

    @staticmethod
    def get_word_cloud_template(word_items):
        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Tag Clouds</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f4;
        }}
        #word-cloud {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .word {{
            margin: 5px;
            padding: 5px;
            border-radius: 5px;
            transition: transform 0.3s ease;
            cursor: help;
        }}
        .word:hover {{
            transform: scale(1.1);
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}
    </style>
</head>
<body>
    <h1>Tag Clouds</h1>
    <div id="word-cloud">
        {word_items}
    </div>
</body>
</html>""" 