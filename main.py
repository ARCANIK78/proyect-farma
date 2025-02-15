import sys
from PyQt5.QtWidgets import QApplication
from Vista.vista import VistaPage  # Importamos la clase con la lógica

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VistaPage()   # Usamos VistaPage, que ya incluye la configuración y lógica
    ventana.show()
    sys.exit(app.exec_())  # En PyQt5 se usa exec_() en lugar de exec()
