import sys
from PyQt5.QtWidgets import QApplication
from view.vista import VistaPage
from Controller.controlador import Controlador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = VistaPage()  # Instancia de la vista
    controlador = Controlador(vista)  # El controlador se encarga de conectar la lógica
    vista.show()
    sys.exit(app.exec_())