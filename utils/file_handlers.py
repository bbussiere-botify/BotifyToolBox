# This Python file uses the following encoding: utf-8
import zipfile
import io
import csv
from collections import defaultdict

class FileHandler:
    @staticmethod
    def open_file(file_path):
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                file_bytes = zip_ref.open(zip_ref.namelist()[0])
                return io.TextIOWrapper(file_bytes, encoding='utf-8')
        else:
            return open(file_path, 'r')

    @staticmethod
    def extract_query_params_from_file(file_path, progress_callback=None):
        with FileHandler.open_file(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            # Skip the first two lines
            next(reader) #sep=,
            next(reader) #header
            urls = []

            # Lire le fichier une première fois pour compter le nombre total de lignes
            total_rows = sum(1 for _ in reader)
            csvfile.seek(0)  # Retourner au début du fichier
            next(reader)  # Skip sep=,
            next(reader)  # Skip header

            for i, row in enumerate(reader, 1):
                urls.append(row[0])
                if progress_callback:
                    progress = int((i / total_rows) * 100)
                    progress_callback(progress)

        return urls

    @staticmethod
    def save_to_file(file_path, content):
        with open(file_path, 'w') as f:
            f.write(content) 