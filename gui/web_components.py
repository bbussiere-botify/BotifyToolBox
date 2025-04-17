# This Python file uses the following encoding: utf-8
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineUrlRequestInterceptor

class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.console_message_callback = None

    def setConsoleMessageCallback(self, callback):
        self.console_message_callback = callback

    def javaScriptConsoleMessage(self, level, message, line_number, source_id):
        if self.console_message_callback:
            self.console_message_callback(message, level, source_id)
        return super().javaScriptConsoleMessage(level, message, line_number, source_id)

class NetworkInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self):
        super().__init__()
        self.resources = []
    
    def reset_resources(self):
        self.resources = []

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if url.endswith('.js') and url not in self.resources:
            self.resources.append(url)
        return info 