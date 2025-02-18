from sqlalchemy import Column, Integer, Float, ForeignKey
from base import Base  

class ProductoPrecio(Base):
    __tablename__ = "producto_precios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    precio_costo = Column(Float, nullable=False)
    ganancia = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)