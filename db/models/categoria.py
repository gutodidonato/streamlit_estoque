from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..db import Base

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    
    pai_id = Column(Integer, ForeignKey("categoria.id"), nullable=True)

    pai = relationship("Categoria", back_populates="filhas")
    filhas = relationship("Categoria", back_populates="pai", cascade="all, delete")