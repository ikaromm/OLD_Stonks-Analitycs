from stonks_analytics.db.repository import Repositorio
from stonks_analytics.db.entity.estatiticas import Estatisticas
from stonks_analytics.db.entity.empresa import Empresa

from sqlalchemy.orm import Session
from sqlalchemy import Select


class EstatisticasRepositorio(Repositorio):
    entidade = Estatisticas

    def obter_por_empresa(self, empresa_id: int) -> Estatisticas:
        with Session(self.engine) as sessao:
            return (
                sessao.query(self.entidade)
                .where(self.entidade.empresa_id == empresa_id)
                .first()
            )

    def obter_por_empresa_codigo(self, empresa_codigo: str) -> Estatisticas:
        with Session(self.engine) as sessao:

            query = (
                Select(self.entidade)
                .join(Empresa)
                .where(Empresa.codigo == empresa_codigo)
            )

            return sessao.execute(query).first()
