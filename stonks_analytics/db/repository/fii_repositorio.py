from stonks_analytics.db.repository import Repositorio
from stonks_analytics.db.entity.fii import Fii
from stonks_analytics.db.entity.fii_fundo import Fundo

from sqlalchemy.orm import Session
from sqlalchemy import Select


class FiiRepositorio(Repositorio):
    entidade = Fundo

    def obter_por_fundo(self, fundo_id: int) -> Fii:
        with Session(self.engine) as sessao:
            return (
                sessao.query(self.entidade)
                .where(self.entidade.fundo_id == fundo_id)
                .first()
            )

    def obter_por_fundo_codigo(self, fundo_codigo: str) -> Fii:
        with Session(self.engine) as sessao:
            query = (
                Select(self.entidade)
                .join(fundo)
                .where(fundo.codigo == fundo_codigo)
            )

            return sessao.execute(query).first()
