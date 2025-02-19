from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from .ui_untitled import Ui_MainWindow

class VistaPage(QMainWindow, Ui_MainWindow):
    # Definir señales para cada acción
    signalPaginaVenta = pyqtSignal()
    signalPaginaNuevo = pyqtSignal()
    signalPaginaEditar = pyqtSignal()
    signalPaginaEliminar = pyqtSignal()
    signalPaginaCatalogo = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.signalPaginaVenta.emit)
        self.pushButton_2.clicked.connect(self.signalPaginaNuevo.emit)
        self.pushButton_7.clicked.connect(self.signalPaginaNuevo.emit)
        self.pushButton_8.clicked.connect(self.signalPaginaEditar.emit)
        self.pushButton_9.clicked.connect(self.signalPaginaEliminar.emit)
        self.pushButton_10.clicked.connect(self.signalPaginaCatalogo.emit)

    def mostrarPagina(self, index):
        """Método para cambiar la página del stackedWidget."""
        self.stackedWidget.setCurrentIndex(index)
