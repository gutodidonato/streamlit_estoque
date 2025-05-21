from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..db import Base

class ItemCarrinho(Base):
    __tablename__ = 'item_carrinho'
    
    id = Column(Integer, primary_key=True)
    item_nome = Column(String)
    preco_unitario = Column(Float)
    quantidade = Column(Integer)
    
    carrinho = relationship("Carrinho", back_populates="itens_carrinho")
    
    
class ItemVenda(Base):
    __tablename__ = 'item_venda'
    
    id = Column(Integer, primary_key=True)
    item_nome = Column(String)
    preco_unitario = Column(Float)
    quantidade = Column(Integer)
    
    
    venda = relationship("Venda", back_populates="itens_venda")
    




