from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import engine
from base import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Codigo_de_barra = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    categoria = relationship("categoria", backref="productos")
    Fecha_de_caducidad  = Column(DateTime, nullable=False)
    Vencido = Column(Boolean, nullable=False)
    Precio = Column(Float, nullable=False)


