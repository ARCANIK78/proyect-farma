from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config import engine
from base import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)

