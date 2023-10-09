from stonks_analytics.db.entity import Base

from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime

from datetime import datetime


class Estatisticas(Base):
    __tablename__ = "estatisticas"

    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

    setor = Column(String(50), nullable=False)
    segmento = Column(String(50), nullable=False)
    pvp = Column(Float, nullable=False)
    tag_along = Column(Float, nullable=False)
    free_float = Column(Float, nullable=False)
    graham = Column(Float, nullable=False)
    cotacao = Column(Float, nullable=False)
    pontuacao = Column(Float, nullable=False)

    data_pesquisa = Column(DateTime, default=datetime.now)
    data_cotacao = Column(DateTime, default=datetime.now, onupdate=datetime.now)
