from stonks_analytics.db.repository import Repositorio
from stonks_analytics.db.entity.empresa import Empresa


class EmpresaRepositorio(Repositorio):
    entidade = Empresa
