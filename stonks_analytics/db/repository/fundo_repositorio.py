from stonks_analytics.db.repository import Repositorio
from stonks_analytics.db.entity.fii_fundo import Fundo


class FundoRepositorio(Repositorio):
    entidade = Fundo
