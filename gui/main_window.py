# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Slot, QTimer, QUrl
from PySide6.QtWidgets import (
    QMainWindow, QProgressBar, QPushButton, QFileDialog, 
    QSizePolicy
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import pandas as pd
import json

from gui.web_components import CustomWebEnginePage, NetworkInterceptor
from workers.thread_worker import GenericWorkerThread
from utils.file_handlers import FileHandler
from utils.text_analysis import TextAnalyzer
from utils.web_analysis import WebAnalyzer
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_web_view()
        self.setup_connections()
        self.fileInput = ""
        self.fileOutput = ""

    def setup_ui(self):
        # Créer une barre de progression dans la statusbar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(200)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%p%")
        self.progress_bar.hide()

        # Créer un bouton de sauvegarde
        self.save_button = QPushButton("Save Results")
        self.save_button.setMaximumWidth(100)
        
        # Ajouter les widgets à la statusbar
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.statusBar().addPermanentWidget(self.save_button)

    def setup_web_view(self):
        self.web_view = QWebEngineView()
        self.page = CustomWebEnginePage(self.web_view)
        self.page.setConsoleMessageCallback(self.handle_console_message)
        self.web_view.setPage(self.page)

        self.network_interceptor = NetworkInterceptor()
        profile = self.web_view.page().profile()
        profile.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        profile.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        profile.settings().setAttribute(QWebEngineSettings.AutoLoadImages, True)
        profile.setUrlRequestInterceptor(self.network_interceptor)

        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.web_view.setMinimumSize(200, 200)
        self.ui.verticalLayout_2.addWidget(self.web_view)

    def setup_connections(self):
        # Connecter les boutons aux fonctions
        self.ui.pushButton_open.clicked.connect(self.openFileDiablog)
        self.ui.pushButton_open_2.clicked.connect(self.openFileDiablog)
        self.ui.pushButton_query.clicked.connect(self.extractQueryParam)
        self.ui.pushButton_keyword.clicked.connect(self.getUniqueKeyword)
        self.ui.pushButton_GoURL.clicked.connect(self.launchBrowser)
        self.ui.pushButton_sitemap.clicked.connect(self.launchSitemap)
        self.ui.pushButton_retrieve_robots.clicked.connect(self.retrieveRobots)
        self.ui.pushButton_check_robots.clicked.connect(self.check_urls_by_robots)
        self.ui.pushButton_json.clicked.connect(self.decryptBotifyFilter)
        self.ui.pushButton_json_validate.clicked.connect(self.JSON_validation)
        self.save_button.clicked.connect(self.saveToFile)

    def run_long_task(self, task_function, *args, **kwargs):
        self.progress_bar.setValue(0)
        self.progress_bar.show()

        self.worker_thread = GenericWorkerThread(task_function, *args, **kwargs)
        self.worker_thread.update_progress.connect(self.update_progress_bar)
        self.worker_thread.calculation_finished.connect(self.on_task_finished)
        self.worker_thread.error_occurred.connect(self.handle_task_error)
        self.worker_thread.update_text.connect(self.update_text_browser)
        self.worker_thread.start()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def on_task_finished(self, result):
        self.progress_bar.setValue(100)
        if isinstance(result, pd.DataFrame):
            self.display_keyword_results(result)
        QTimer.singleShot(1000, self.progress_bar.hide)

    def display_keyword_results(self, df):
        if self.ui.radioButton_csv.isChecked():
            # Afficher en format CSV
            self.ui.textBrowserOutput.append("Word\tOccurrences\tTotal Clicks\tTotal Impressions\tAvg CTR")
            for _, row in df.iterrows():
                self.ui.textBrowserOutput.append(
                    f"{row['Word']}\t{row['Occurrences']}\t{row['Total_Clicks']}\t"
                    f"{row['Total_Impressions']}\t{row['Avg_CTR']}%"
                )
        else:
            # Afficher en nuage de mots
            html_content = TextAnalyzer.generate_word_cloud_html(df)
            self.ui.textBrowserOutput.setHtml(html_content)

    def handle_task_error(self, error_message):
        self.progress_bar.setValue(0)
        self.progress_bar.hide()
        self.ui.textBrowserOutput.append(f"Error: {error_message}")

    @Slot(str, int, str)
    def handle_console_message(self, message, level, source_id):
        self.ui.textBrowserOutput.append(f"[JS] {message}")
        self.ui.textBrowserOutput.repaint()

    def update_text_browser(self, text):
        self.ui.textBrowserOutput.append(text)

    # File Dialog Methods
    def openFileDiablog(self):
        self.fileInput, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", 
            "Zip File (*.zip);;CSV File (*.csv);;Text File (*.txt);;All Files (*)"
        )
        if self.fileInput:
            self.ui.labelFilename.setText("Selected File:" + str(self.fileInput))

    def saveFileDiablog(self):
        self.fileOutput, _ = QFileDialog.getSaveFileName(
            self, "Save File", "",
            "CSV File (*.csv);;Text File (*.txt);;JSON File (*.json);;All Files (*)"
        )

    def saveToFile(self):
        self.saveFileDiablog()
        if self.fileOutput:
            FileHandler.save_to_file(self.fileOutput, self.ui.textBrowserOutput.toPlainText())
            self.progress_bar.setValue(100)

    # Query Parameter Methods
    def extractQueryParam(self):
        if self.fileInput:
            self.ui.textBrowserOutput.clear()
            self.run_long_task(self.extractQueryParamFromFile)
        else:
            self.ui.textBrowserOutput.append("Please choose a file first")

    def extractQueryParamFromFile(self, progress_callback=None):
        urls = FileHandler.extract_query_params_from_file(self.fileInput, progress_callback)
        query_params_dict = WebAnalyzer.extract_query_params(urls)
        sorted_query_params = sorted(query_params_dict.items(), key=lambda x: x[1], reverse=True)

        self.worker_thread.update_text.emit("Name\tCount")
        for param in sorted_query_params:
            self.worker_thread.update_text.emit(f"{param[0]}\t{param[1]}")
        return "Done"

    # Keyword Analysis Methods
    def getUniqueKeyword(self):
        if self.fileInput:
            self.ui.textBrowserOutput.clear()
            language = self.ui.comboBox_language.currentText()
            self.run_long_task(
                TextAnalyzer.analyze_keywords,
                self.fileInput,
                language
            )
        else:
            self.ui.textBrowserOutput.append("Please choose a file first")

    # Browser Methods
    def launchBrowser(self):
        self.network_interceptor.reset_resources()
        self.web_view.loadFinished.connect(self.get_resources)
        if self.ui.lineEditURL.text().strip():
            self.ui.textBrowserOutput.clear()
            self.web_view.setUrl(QUrl(self.ui.lineEditURL.text().strip()))
        else:
            self.ui.textBrowserOutput.append("Please enter a URL")

    def get_resources(self, ok):
        if ok:
            resources = self.network_interceptor.resources
            adn_cloud_scripts = [
                resource for resource in resources
                if 'adn.cloud' in resource
            ]
            if adn_cloud_scripts:
                self.ui.textBrowserOutput.append("<b>ADN Cloud scripts:</b>")
                self.ui.textBrowserOutput.append("\n".join(adn_cloud_scripts))
                self.web_view.page().runJavaScript(
                    'localStorage.setItem("pageworkers.enable_debug_mode", "true")'
                )
            else:
                self.ui.textBrowserOutput.append("Please Re-Submit to check (sometimes network is too slow)")

    # Sitemap Methods
    def launchSitemap(self):
        if self.ui.lineEdit_sitemap.text().strip():
            self.ui.textBrowserOutput.clear()
            self.ui.textBrowserOutput.append("Analyzing sitemap...")
            
            def on_sitemap_result(result):
                if isinstance(result, str):
                    # Si le résultat contient des tabulations, on utilise une police monospace
                    if "\t" in result:
                        formatted_result = result.replace("\n", "<br>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
                        self.ui.textBrowserOutput.setHtml(
                            f'<pre style="font-family: Courier, monospace;">{formatted_result}</pre>'
                        )
                    else:
                        self.ui.textBrowserOutput.setPlainText(result)

            # Connecter le signal de mise à jour du texte
            self.worker_thread = GenericWorkerThread(
                WebAnalyzer.analyze_sitemap,
                self.ui.lineEdit_sitemap.text().strip()
            )
            self.worker_thread.update_progress.connect(self.update_progress_bar)
            self.worker_thread.calculation_finished.connect(on_sitemap_result)
            self.worker_thread.error_occurred.connect(self.handle_task_error)
            self.worker_thread.update_text.connect(self.update_text_browser)
            
            # Démarrer l'analyse
            self.progress_bar.setValue(0)
            self.progress_bar.show()
            self.worker_thread.start()
        else:
            self.ui.textBrowserOutput.append("Please enter a sitemap URL")

    # Robots.txt Methods
    def retrieveRobots(self):
        if self.ui.lineEdit_rob.text().strip():
            self.ui.plainTextEdit_rules.clear()
            robots_content = WebAnalyzer.analyze_robots_txt(self.ui.lineEdit_rob.text().strip())
            self.ui.plainTextEdit_rules.setPlainText(robots_content)
        else:
            self.ui.textBrowserOutput.append("Please enter a URL for the robots.txt")

    def check_urls_by_robots(self):
        urls = self.ui.plainTextEdit_urls.toPlainText().strip().split('\n')
        user_agent = self.ui.comboBox_ua.currentText()
        robots_content = self.ui.plainTextEdit_rules.toPlainText()

        if not all([urls, user_agent, robots_content]):
            self.ui.textBrowserOutput.append("Please fill all required fields")
            return

        results = WebAnalyzer.check_urls_against_robots(urls, robots_content, user_agent)
        self.ui.textBrowserOutput.clear()
        self.ui.textBrowserOutput.append("Verification results:")
        self.ui.textBrowserOutput.append("")
        
        for url, is_allowed in results:
            if is_allowed:
                self.ui.textBrowserOutput.append(f"✅ {url}")
            else:
                self.ui.textBrowserOutput.append(f'<span style="color: red;">❌ {url}</span>')

    # Botify Filter Methods
    def decryptBotifyFilter(self):
        url = self.ui.lineEdit_burl.text().strip()
        if not url:
            self.ui.textBrowserOutput.append("Please enter a Botify URL with filters")
            return

        self.ui.textBrowserOutput.clear()
        result = WebAnalyzer.decrypt_botify_filter(url)
        
        # Si le résultat contient du JSON formaté, on utilise setHtml pour préserver la mise en forme
        if "---Filters---" in result or "---Columns---" in result:
            formatted_result = result.replace("\n", "<br>").replace(" ", "&nbsp;")
            self.ui.textBrowserOutput.setHtml(f"<pre>{formatted_result}</pre>")
        else:
            self.ui.textBrowserOutput.append(result) 

    def JSON_validation(self):
        json_text = self.ui.plainTextEdit_json.toPlainText().strip()
        if not json_text:
            self.ui.textBrowserOutput.append("Please enter JSON content to validate")
            return
        
        try:
            # Parser le JSON pour vérifier sa validité
            json_data = json.loads(json_text)
            
            # Re-formater le JSON avec une indentation propre
            formatted_json = json.dumps(json_data, indent=2, ensure_ascii=False)
            
            self.ui.textBrowserOutput.clear()

            # Créer du HTML coloré pour l'affichage
            html_content = self._format_json_html(formatted_json)
            
            self.ui.textBrowserOutput.setHtml(html_content)
            
        except json.JSONDecodeError as e:
            error_message = f"Invalid JSON: {str(e)}"
            self.ui.textBrowserOutput.append(f'<span style="color: red; font-weight: bold;">❌ {error_message}</span>')
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"
            self.ui.textBrowserOutput.append(f'<span style="color: red; font-weight: bold;">❌ {error_message}</span>')

    def _format_json_html(self, json_str):
        """Formate le JSON avec des couleurs pour l'affichage HTML"""
        import re
        
        # Remplacer les caractères spéciaux HTML
        json_str = json_str.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        # Appliquer les couleurs
        # Clés (avant les deux points)
        json_str = re.sub(r'(".*?")(\s*:)', r'<span style="color: #0066cc; font-weight: bold;">\1</span>\2', json_str)
        
        # Valeurs string (après les deux points)
        json_str = re.sub(r':\s*(".*?")', r': <span style="color: #009900;">\1</span>', json_str)
        
        # Valeurs numériques
        json_str = re.sub(r':\s*(\d+(?:\.\d+)?)', r': <span style="color: #cc6600;">\1</span>', json_str)
        
        # Valeurs booléennes
        json_str = re.sub(r':\s*(true|false)', r': <span style="color: #990099;">\1</span>', json_str)
        
        # Valeurs null
        json_str = re.sub(r':\s*(null)', r': <span style="color: #666666;">\1</span>', json_str)
        
        # Ajouter le style pour préserver les espaces et utiliser une police monospace
        html_content = f'''
        <div style="background-color: #f8f8f8; border: 1px solid #ddd; padding: 10px; border-radius: 4px;">
            <pre style="font-family: 'Courier New', monospace; font-size: 12px; margin: 0; white-space: pre-wrap;">{json_str}</pre>
        </div>
        '''
        
        return html_content
