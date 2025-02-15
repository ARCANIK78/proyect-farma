import sys
from PyQt6.QtWidgets import QApplication
from Vista.vista import VistaPage  # Importamos la clase con la lógica

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VistaPage()   # Usamos Vista, que ya incluye la configuración y lógica
    ventana.show()
    sys.exit(app.exec())