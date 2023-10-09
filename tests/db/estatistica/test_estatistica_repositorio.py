from stonks_analytics.db.repository.empresa_repositorio import EmpresaRepositorio
from stonks_analytics.db.entity.empresa import Empresa

from stonks_analytics.db.repository.estatisticas_repositorio import (
    EstatisticasRepositorio,
)
from stonks_analytics.db.entity.estatiticas import Estatisticas

from unittest import TestCase
from pathlib import Path

from sqlalchemy import create_engine


class TestEstatisticasRepositorio(TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///test.db")

        self.empresa = Empresa(codigo="TESTE", nome="Teste")
        self.empresa_repositorio = EmpresaRepositorio(self.engine)
        self.empresa_repositorio.add(self.empresa)

        self.dados = {
            "empresa_id": self.empresa.id,
            "setor": "Teste",
            "segmento": "Teste",
            "pvp": 1,
            "tag_along": 1,
            "free_float": 1,
            "graham": 1,
            "cotacao": 1,
            "pontuacao": 1,
        }

    def tearDown(self):
        Path("test.db").unlink(missing_ok=True)

    def test_add(self):
        estatistica = Estatisticas(**self.dados)

        estatistica_repositorio = EstatisticasRepositorio(self.engine)

        estatistica_repositorio.add(estatistica)
        estatistica_salva = estatistica_repositorio.get(estatistica.id)

        self.assertEqual(estatistica.id, estatistica_salva.id)

    def test_get_all(self):

        estatisticas = []
        for i in range(10):
            empresa = Empresa(codigo=f"TESTE{i}", nome=f"Teste{i}")
            self.empresa_repositorio = EmpresaRepositorio(self.engine)
            self.empresa_repositorio.add(empresa)

            estatistica = Estatisticas(
                empresa_id=empresa.id,
                setor=f"Teste{i}",
                segmento=f"Teste{i}",
                pvp=1,
                tag_along=1,
                free_float=1,
                graham=1,
                cotacao=1,
                pontuacao=1,
            )

            estatisticas.append(estatistica)

        estatistica_repositorio = EstatisticasRepositorio(self.engine)

        estatistica_repositorio.add_all(estatisticas)

        estatisticas_salvas = estatistica_repositorio.get_all()

        self.assertEqual(len(estatisticas), len(estatisticas_salvas))

    def test_update(self):
        estatistica = Estatisticas(**self.dados)

        estatistica_repositorio = EstatisticasRepositorio(self.engine)

        estatistica_repositorio.add(estatistica)

        estatistica.graham = 2
        estatistica.setor = "Teste 2"
        estatistica_repositorio.update(estatistica)

        estatistica_salva = estatistica_repositorio.get(estatistica.id)

        self.assertEqual(estatistica.graham, estatistica_salva.graham)

    def test_remove(self):
        estatistica_repositorio = EstatisticasRepositorio(self.engine)
        estatistica = Estatisticas(**self.dados)
        estatistica_repositorio.add(estatistica)
        estatistica_repositorio.remove(estatistica)

        estatistica_salva = estatistica_repositorio.get(estatistica.id)

        self.assertIsNone(estatistica_salva)
