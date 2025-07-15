# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QThread, Signal

class GenericWorkerThread(QThread):
    # Signal declarations
    update_progress = Signal(int)
    calculation_finished = Signal(object)
    error_occurred = Signal(str)
    update_text = Signal(str)

    def __init__(self, function_to_run, *args, **kwargs):
        super().__init__()
        print("Initializing worker thread")
        self.function_to_run = function_to_run
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            print("Starting thread execution")
            # Add progress parameter to the function
            if 'progress_callback' not in self.kwargs:
                print("Adding progress callback")
                self.kwargs['progress_callback'] = self.update_progress.emit

            # Execute function with arguments
            print("Calling function with arguments")
            result = self.function_to_run(*self.args, **self.kwargs)

            # Emit result
            print("Emitting result")
            self.calculation_finished.emit(result)

        except Exception as e:
            print(f"Error in thread: {str(e)}")
            self.error_occurred.emit(str(e)) 