from stonks_analytics.db.entity import Base

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
import datetime


class Repositorio:
    """
    Classe base para repositórios que utilizam SQL como banco de dados.
    """

    entidade = Base

    def __init__(self, engine: Engine, entidade: Base = None):
        self.engine = engine

        if entidade is not None:
            self.entidade = entidade

        self.entidade.metadata.create_all(self.engine)
        self.metadata = self.entidade.__table__

    def get(self, id: int) -> entidade:
        with Session(self.engine) as session:
            return session.get(self.entidade, id)

    def get_all(self, **kwargs) -> list[entidade]:
        with Session(self.engine) as session:
            query = session.query(self.entidade)

            query_params = {}
            for key, value in kwargs.items():
                if key in [c.name for c in self.metadata.columns]:
                    if value is not None:
                        query_params[key] = value
            if query_params:
                query = query.filter_by(**query_params)

        return query.all()

    def add(self, entidade: entidade) -> entidade:
        with Session(self.engine, expire_on_commit=False) as session:
            session.add(entidade)

            session.commit()

        return entidade

    def add_all(self, entidades: list[entidade]) -> list[entidade]:
        with Session(self.engine, expire_on_commit=False) as session:
            session.add_all(entidades)

            session.commit()

        return entidades

    def remove(self, entidade: entidade) -> None:
        with Session(self.engine) as session:
            session.delete(entidade)

            session.commit()

    def update(self, entidade: entidade) -> entidade:
        entidade.modified_at = datetime.datetime.utcnow()
        with Session(self.engine, expire_on_commit=False) as session:
            session.merge(entidade)

            session.commit()

        return entidade