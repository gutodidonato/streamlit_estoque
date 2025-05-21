from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..db import Base

class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    vendivel = Column(Boolean, default=True)
    
    preco_aquisicao = Column(Float, nullable=True)
    preco_venda = Column(Float, nullable=False)

    quantidade = Column(Integer, nullable=False)
    estoque_minimo = Column(Integer, nullable=True)
    estoque_alerta = Column(Integer, nullable=True)
    estoque_maximo = Column(Integer, nullable=True)

    local = Column(String, nullable=True)
    
    componentes = relationship("MaterialComposicao",
                               foreign_keys="[MaterialComposicao.produto_id]",
                               back_populates="produto")

    usado_em = relationship("MaterialComposicao",
                            foreign_keys="[MaterialComposicao.componente_id]",
                            back_populates="componente")



class MaterialComposicao(Base):
    __tablename__= 'material_composicao'
    id = Column(Integer, primary_key=True)
    
    produto_id = Column(Integer, ForeignKey("produto.id"))
    componente_id = Column(Integer, ForeignKey("produto.id"))
    quantidade = Column(Integer, nullable=False)
    
    produto = relationship("Material", foreign_keys=[produto_id], back_populates="componentes")
    componente = relationship("Material", foreign_keys=[componente_id], back_populates="usado_em")
    
    