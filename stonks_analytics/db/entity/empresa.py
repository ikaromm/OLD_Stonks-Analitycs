from stonks_analytics.db.entity import Base

from sqlalchemy import Column, Integer, String


class Empresa(Base):
    __tablename__ = 'empresa'
    
    id = Column(Integer, primary_key=True)
    codigo = Column(String(10), nullable=False)
    nome = Column(String(50), nullable=False)