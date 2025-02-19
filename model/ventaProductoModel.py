from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import engine
from base import Base  

class ProductoPrecio(Base):
    __tablename__ = "producto_precios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    precio_costo = Column(Float, nullable=False)
    ganancia = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)
    producto = relationship("Producto", back_populates="precios")
    
    def __repr__(self):
        return f"<ProductoPrecio(id={self.id}, precio_venta={self.precio_venta})>"