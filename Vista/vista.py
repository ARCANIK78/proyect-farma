from PyQt5.QtWidgets import QMainWindow
from .ui_untitled import Ui_MainWindow

class VistaPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar los botones a sus respectivas funciones
        self.pushButton.clicked.connect(self.mostrarPaginaventa)
        self.pushButton_2.clicked.connect(self.mostrarPaginaNuevo)
        self.pushButton_7.clicked.connect(self.mostrarPaginaNuevo)
        self.pushButton_8.clicked.connect(self.mostrarPaginaEditar)
        self.pushButton_9.clicked.connect(self.mostrarPaginaEliminar)
        self.pushButton_10.clicked.connect(self.mostrarPaginaCatalogo)
    
    def mostrarPaginaventa(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def mostrarPaginaNuevo(self):
        self.stackedWidget.setCurrentIndex(1)

    def mostrarPaginaEditar(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def mostrarPaginaEliminar(self):
        self.stackedWidget.setCurrentIndex(3)

    def mostrarPaginaCatalogo(self):
        self.stackedWidget.setCurrentIndex(4)
