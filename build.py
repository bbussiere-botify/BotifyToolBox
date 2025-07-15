import os
import sys
import nltk
import shutil
from pathlib import Path

def prepare_nltk_data():
    """Télécharge les données NLTK nécessaires"""
    nltk.download('stopwords')

def get_nltk_data_paths():
    """Récupère les chemins corrects des données NLTK"""
    # Trouve le chemin des données NLTK
    nltk_data_path = nltk.data.path[0]
    print(f"Chemin NLTK trouvé: {nltk_data_path}")
    
    # Vérifie les dossiers existants
    tokenizers_path = os.path.join(nltk_data_path, 'tokenizers')
    corpora_path = os.path.join(nltk_data_path, 'corpora')
    
    print(f"Tokenizers path: {tokenizers_path} - Existe: {os.path.exists(tokenizers_path)}")
    print(f"Corpora path: {corpora_path} - Existe: {os.path.exists(corpora_path)}")
    
    # Retourne seulement les chemins qui existent
    paths = []
    if os.path.exists(tokenizers_path):
        paths.append(f'{tokenizers_path};tokenizers')
    if os.path.exists(corpora_path):
        paths.append(f'{corpora_path};corpora')
    
    return paths

def cleanup_previous_build():
    """Nettoie les builds précédents"""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

def create_spec_file():
    """Crée un fichier .spec pour PyInstaller"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['nltk', 'nltk.corpus', 'nltk.tokenize', 'nltk.data'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BotifyToolBox',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('BotifyToolBox.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("Fichier .spec créé : BotifyToolBox.spec")

def create_executable_with_spec():
    """Crée l'exécutable en utilisant le fichier .spec"""
    import PyInstaller.__main__
    
    # Prépare les données NLTK
    prepare_nltk_data()
    
    # Nettoie les builds précédents
    cleanup_previous_build()
    
    # Crée le fichier .spec
    create_spec_file()
    
    # Lance PyInstaller avec le fichier .spec
    PyInstaller.__main__.run(['BotifyToolBox.spec', '--clean', '--noconfirm'])
    
    print(f"\nBuild terminé ! L'exécutable se trouve dans le dossier 'dist'")

def create_executable():
    """Crée l'exécutable avec PyInstaller"""
    import PyInstaller.__main__

    # Prépare les données NLTK
    prepare_nltk_data()
    
    # Nettoie les builds précédents
    cleanup_previous_build()

    # Détermine le nom de l'exécutable selon l'OS
    exe_name = 'BotifyToolBox.exe' if sys.platform == 'win32' else 'BotifyToolBox'

    # Construction de la liste d'arguments PyInstaller
    pyinstaller_args = [
        'main.py',
        '--name=%s' % exe_name,
        '--onefile',
        '--windowed',
        '--clean',  # Nettoie le cache PyInstaller
        '--noconfirm',  # Pas de confirmation pour écraser
        '--hidden-import=nltk',
        '--hidden-import=nltk.corpus',
        '--hidden-import=nltk.tokenize',
        '--hidden-import=nltk.data',
    ]
    
    # Ajoute les données NLTK seulement si elles existent
    nltk_paths = get_nltk_data_paths()
    for path in nltk_paths:
        pyinstaller_args.append(f'--add-data={path}')
    
    # Ajoute l'icône seulement si elle existe
    if os.path.exists('resources/icon.ico'):
        pyinstaller_args.append('--icon=resources/icon.ico')

    print("Arguments PyInstaller:", pyinstaller_args)
    
    # Configuration PyInstaller
    PyInstaller.__main__.run(pyinstaller_args)

    # Copie les fichiers nécessaires dans le dossier dist
    dist_dir = Path('dist')
    if not dist_dir.exists():
        dist_dir.mkdir()

    # Copie le README et autres fichiers nécessaires
    if os.path.exists('README.md'):
        shutil.copy2('README.md', dist_dir)

    print(f"\nBuild terminé ! L'exécutable se trouve dans le dossier 'dist'")

if __name__ == '__main__':
    # Essayez d'abord la méthode normale, sinon utilisez le fichier .spec
    try:
        create_executable()
    except Exception as e:
        print(f"Erreur avec la méthode normale: {e}")
        print("Tentative avec fichier .spec...")
        create_executable_with_spec() 