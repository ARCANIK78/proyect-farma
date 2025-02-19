from sqlalchemy.orm import sessionmaker
from config import engine
from model.productoModel import Producto
from model.ventaProductoModel import ProductoPrecio
from datetime import datetime

SessionLocal = sessionmaker(bind=engine)

class ProductoController:
    def __init__(self):
        self.session = SessionLocal()
    
    def get_all_prodcutos(self):
        self.session.query(Producto).all()

    def add_producto(self,data):
        producto = Producto(

            codigo_de_barra=data["codigo_de_barra"],
            nombre=data["nombre"],
            cantidad=data["cantidad"],
            categoria_id=data["categoria_id"],
            fecha_caducidad=datetime.fromisoformat(data["fecha_caducidad"]),
            vencido=data["vencido"]
        )
        self.session.add(producto)
        self.session.commit()
        return producto
    
    def add_precio_to_producto(self, producto_id, precio_data):
        precio = ProductoPrecio(
            producto_id=producto_id,
            precio_costo=precio_data["precio_costo"],
            ganancia=precio_data["ganancia"],
            precio_venta=precio_data["precio_venta"]
        )
        self.session.add(precio)
        self.session.commit()
        return precio
    
    def get_precios_by_producto(self, producto_id):
        producto = self.session.query(Producto).filter_by(id=producto_id).first()
        return producto.precios if producto else[]

    def close(self):
        self.session.close()

