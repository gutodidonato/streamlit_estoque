from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..db import Base

class Carrinho(Base):
    __tablename__ = 'carrinho'
    
    id = Column(Integer, primary_key=True)
    data_criacao = Column(DateTime)
    total = Column(Float)
    frete = Column(Float)
    
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    
    itens_carrinho = relationship("ItemCarrinho", back_populates="carrinho", cascade="all, delete-orphan")
    
    
class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    total = Column(Float)
    frete = Column(Float)
    
    data_venda = Column(DateTime)
    forma_pagamento = Column(String)

    itens_venda = relationship("ItemVenda", back_populates="venda", cascade="all, delete-orphan")
    vendedor = relationship("User", back_populates="vendas_realizadas")

