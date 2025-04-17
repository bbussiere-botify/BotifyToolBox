# BotifyToolBox

BotifyToolBox est un outil d'analyse et de traitement pour les données Botify. Il permet d'effectuer diverses opérations comme l'analyse de sitemaps, la vérification de robots.txt, le décodage de filtres Botify et plus encore.

## Installation

### Utilisateurs Windows/Mac
1. Téléchargez la dernière version de BotifyToolBox depuis la section "Releases"
2. Décompressez l'archive
3. Double-cliquez sur l'exécutable `BotifyToolBox.exe` (Windows) ou `BotifyToolBox` (Mac)

### Développeurs
Si vous souhaitez modifier ou compiler le code source :

1. Clonez le repository
```bash
git clone [URL_DU_REPO]
```

2. Installez les dépendances
```bash
pip install -r requirements.txt
```

3. Lancez l'application
```bash
python main.py
```

4. Pour créer l'exécutable
```bash
python build.py
```

## Fonctionnalités

- **Analyse de Sitemap**
  - Extraction des URLs
  - Support des hreflangs
  - Gestion des sitemaps indexés

- **Vérification Robots.txt**
  - Téléchargement et analyse du fichier robots.txt
  - Vérification de l'accessibilité des URLs
  - Support de différents User-Agents

- **Analyse de Mots-clés**
  - Extraction et analyse des mots-clés
  - Visualisation en nuage de mots
  - Support multilingue

- **Décodage de Filtres Botify**
  - Décodage des filtres depuis les URLs Botify
  - Affichage formaté des filtres et colonnes

## Utilisation

1. **Analyse de Sitemap**
   - Entrez l'URL du sitemap
   - Cliquez sur "Analyze"
   - Les résultats s'afficheront dans le tableau

2. **Vérification Robots.txt**
   - Entrez l'URL du robots.txt
   - Collez les URLs à vérifier
   - Sélectionnez le User-Agent
   - Cliquez sur "Check"

3. **Analyse de Mots-clés**
   - Chargez votre fichier CSV/ZIP
   - Sélectionnez la langue
   - Choisissez le format d'affichage (CSV ou nuage de mots)
   - Cliquez sur "Analyze"

4. **Décodage de Filtres**
   - Collez l'URL Botify contenant les filtres
   - Cliquez sur "Decode"

## Support

Pour toute question ou problème, veuillez créer une issue dans le repository GitHub. 