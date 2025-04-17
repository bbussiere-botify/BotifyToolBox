import os
import sys
import nltk
import shutil
from pathlib import Path

def prepare_nltk_data():
    """Télécharge les données NLTK nécessaires"""
    nltk.download('stopwords')

def cleanup_previous_build():
    """Nettoie les builds précédents"""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

def create_executable():
    """Crée l'exécutable avec PyInstaller"""
    import PyInstaller.__main__

    # Prépare les données NLTK
    prepare_nltk_data()
    
    # Nettoie les builds précédents
    cleanup_previous_build()

    # Détermine le nom de l'exécutable selon l'OS
    exe_name = 'BotifyToolBox.exe' if sys.platform == 'win32' else 'BotifyToolBox'

    # Configuration PyInstaller
    PyInstaller.__main__.run([
        'main.py',
        '--name=%s' % exe_name,
        '--onefile',
        '--windowed',
        '--icon=resources/icon.ico' if os.path.exists('resources/icon.ico') else None,
        '--add-data=%s' % os.path.join(nltk.data.path[0], 'tokenizers;tokenizers'),
        '--add-data=%s' % os.path.join(nltk.data.path[0], 'corpora;corpora'),
        '--hidden-import=nltk',
        '--hidden-import=nltk.corpus',
        '--hidden-import=nltk.tokenize',
        '--hidden-import=nltk.data',
    ])

    # Copie les fichiers nécessaires dans le dossier dist
    dist_dir = Path('dist')
    if not dist_dir.exists():
        dist_dir.mkdir()

    # Copie le README et autres fichiers nécessaires
    if os.path.exists('README.md'):
        shutil.copy2('README.md', dist_dir)

    print(f"\nBuild terminé ! L'exécutable se trouve dans le dossier 'dist'")

if __name__ == '__main__':
    create_executable() 