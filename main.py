import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Vista.ui_untitled import Ui_MainWindow  # Importa la UI generada

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainApp()
    ventana.show()
    sys.exit(app.exec())  # Ejecuta la aplicación correctamente en PyQt6
