from stonks_analytics.db.entity import Base

from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime

from datetime import datetime


class Fii(Base):

    __tablename__ = "fii"

    id = Column(Integer, primary_key=True)
    fundo_id = Column(Integer, ForeignKey("fundo.id"), nullable=False)

    dy12m = Column(Float, nullable=False)
    cotacao = Column(Float, nullable=False)
    pvp = Column(Float, nullable=False)
    prazo = Column(Float, nullable=False)
    taxa_adm = Column(Float, nullable=False)
    vacancia = Column(Float, nullable=False)
    ult_rendimento = Column(Float, nullable=False)
    qnt_imoveis = Column(Float, nullable=False)
    dy5anos = Column(Float, nullable=False)
    pontuacao = Column(Float, nullable=False)
    



    data_pesquisa = Column(DateTime, default=datetime.now)
    data_cotacao = Column(DateTime, default=datetime.now, onupdate=datetime.now)
