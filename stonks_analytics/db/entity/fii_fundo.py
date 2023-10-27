from stonks_analytics.db.entity import Base

from sqlalchemy import Column, Integer, String


class Fundo(Base):
    
    __tablename__ = "fundo"

    id = Column(Integer, primary_key=True)
    codigo = Column(String(10), nullable=False)
    nome = Column(String(50), nullable=False)
