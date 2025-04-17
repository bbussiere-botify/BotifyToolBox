# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QThread, Signal

class GenericWorkerThread(QThread):
    # Déclaration des signaux
    update_progress = Signal(int)
    calculation_finished = Signal(object)
    error_occurred = Signal(str)
    update_text = Signal(str)

    def __init__(self, function_to_run, *args, **kwargs):
        super().__init__()
        print("Initialisation du thread worker")
        self.function_to_run = function_to_run
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            print("Début de l'exécution du thread")
            # Ajouter un paramètre de progression à la fonction
            if 'progress_callback' not in self.kwargs:
                print("Ajout du callback de progression")
                self.kwargs['progress_callback'] = self.update_progress.emit

            # Exécuter la fonction avec ses arguments
            print("Appel de la fonction avec les arguments")
            result = self.function_to_run(*self.args, **self.kwargs)

            # Émettre le résultat
            print("Émission du résultat")
            self.calculation_finished.emit(result)

        except Exception as e:
            print(f"Erreur dans le thread: {str(e)}")
            self.error_occurred.emit(str(e)) 