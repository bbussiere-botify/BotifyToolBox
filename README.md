# BotifyToolBox

BotifyToolBox is a comprehensive analysis and processing tool for Botify data. It provides a graphical user interface for performing various operations such as sitemap analysis, robots.txt verification, keyword analysis, query parameter extraction, and Botify filter decoding.

## Features

### 🔍 **Sitemap Analysis**
- Extract URLs from sitemaps and sitemap indexes
- Support for hreflang attributes
- Detailed analysis with URL counts and sitemap structure
- Export results in tabular format

### 🤖 **Robots.txt Verification**
- Download and analyze robots.txt files
- Check URL accessibility against robots.txt rules
- Support for multiple User-Agent strings
- Batch URL verification

### 📊 **Keyword Analysis**
- Extract and analyze keywords from Botify CSV files
- Generate word clouds with click and impression data
- Multi-language support (English, French, and more)
- Statistical analysis with CTR calculations
- Export results in CSV format or interactive HTML word clouds

### 🔗 **Query Parameter Analysis**
- Extract and analyze query parameters from URL lists
- Frequency analysis of parameter usage
- Support for CSV and ZIP file formats
- Detailed parameter statistics

### 🔐 **Botify Filter Decoding**
- Decode Botify URL filters and explorer parameters
- Format JSON filters for easy reading
- Validate JSON structure
- Extract context and explorer filters

### 🌐 **Web Analysis**
- Browser integration for web page analysis
- Resource tracking and analysis
- ADN Cloud script detection
- Network request monitoring

## Installation

### For End Users

#### Windows
1. Download the latest release from the "Releases" section
2. Extract the archive
3. Run `BotifyToolBox.exe`

#### macOS
1. Download the latest release from the "Releases" section
2. Extract the archive
3. Run `BotifyToolBox` (you may need to allow it in Security & Privacy settings)

### For Developers

1. Clone the repository
```bash
git clone [REPO_URL]
cd BotifyToolBox
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python main.py
```

4. Build the executable
```bash
python build.py
```

## Dependencies

- **PySide6** (≥6.4.0) - GUI framework
- **pandas** (≥1.5.0) - Data analysis
- **nltk** (≥3.7) - Natural language processing
- **requests** (≥2.28.0) - HTTP requests
- **robotexclusionrulesparser** (≥1.7.1) - Robots.txt parsing
- **pyinstaller** (≥5.7.0) - Executable creation

## Usage

### Sitemap Analysis
1. Enter the sitemap URL in the "Sitemap URL" field
2. Click "Analyze Sitemap"
3. Results will display URLs, hreflang information, and sitemap structure
4. Use "Save Results" to export the analysis

### Robots.txt Verification
1. Enter the robots.txt URL
2. Paste URLs to check (one per line)
3. Select the User-Agent
4. Click "Check URLs"
5. Results show which URLs are allowed/blocked

### Keyword Analysis
1. Load your Botify CSV/ZIP file using "Open File"
2. Select the language for analysis
3. Choose display format (CSV table or word cloud)
4. Click "Analyze Keywords"
5. Results show word frequency, clicks, impressions, and CTR

### Query Parameter Analysis
1. Load a file containing URLs
2. Click "Extract Query Parameters"
3. Results show parameter frequency analysis

### Botify Filter Decoding
1. Paste a Botify URL containing filters
2. Click "Decode Filter"
3. Results show formatted JSON filters and columns

### Web Analysis
1. Enter a URL in the browser field
2. Click "Go to URL"
3. The integrated browser will load the page
4. Network resources and scripts are tracked automatically

## File Formats Supported

- **CSV files** - Botify exports, URL lists
- **ZIP files** - Compressed Botify data
- **Text files** - URL lists, configuration files
- **JSON files** - Filter exports, configuration

## Export Options

- **CSV format** - Tabular data for spreadsheet analysis
- **Text format** - Plain text for documentation
- **JSON format** - Structured data for APIs
- **HTML format** - Interactive word clouds and visualizations

## System Requirements

- **Windows**: Windows 10 or later
- **macOS**: macOS 10.14 or later
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 100MB free space
- **Network**: Internet connection for web analysis features

## Troubleshooting

### Common Issues

1. **"NLTK data not found"**
   - The application will automatically download required NLTK data on first run
   - Ensure internet connection is available

2. **"File not found"**
   - Check file path and permissions
   - Ensure file format is supported

3. **"Network error"**
   - Check internet connection
   - Verify URL accessibility
   - Try different User-Agent if blocked

### Performance Tips

- For large files (>100MB), processing may take several minutes
- Use the progress bar to monitor analysis status
- Close other applications to free up memory
- For word cloud generation, limit to 100-200 words for best performance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or feature requests:
- Create an issue in the GitHub repository
- Include detailed error messages and system information
- Provide sample data when possible (anonymized)

## Changelog

### Version 1.0.0
- Initial release with core functionality
- Sitemap analysis with hreflang support
- Robots.txt verification
- Keyword analysis with word clouds
- Query parameter extraction
- Botify filter decoding
- Web browser integration 