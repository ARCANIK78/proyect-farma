from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from Controller.ProductoController import ProductoController

class VentaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.Controller = ProductoController()

        