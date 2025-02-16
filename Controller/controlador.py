class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.conectar_signals()
    
    def conectar_signals(self):
        self.vista.signalPaginaVenta.connect(self.mostrarPaginaVenta)
        self.vista.signalPaginaNuevo.connect(self.mostrarPaginaNuevo)
        self.vista.signalPaginaEditar.connect(self.mostrarPaginaEditar)
        self.vista.signalPaginaEliminar.connect(self.mostrarPaginaEliminar)
        self.vista.signalPaginaCatalogo.connect(self.mostrarPaginaCatalogo)

    def mostrarPaginaVenta(self):
        self.vista.mostrarPagina(0)

    def mostrarPaginaNuevo(self):
        self.vista.mostrarPagina(1)

    def mostrarPaginaEditar(self):
        self.vista.mostrarPagina(2)

    def mostrarPaginaEliminar(self):
        self.vista.mostrarPagina(3)

    def mostrarPaginaCatalogo(self):
        self.vista.mostrarPagina(4)