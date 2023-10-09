from stonks_analytics.db.entity.estatiticas import Estatisticas

from unittest import TestCase


class TestEstatistica(TestCase):
    def setUp(self):
        self.dados = {
            "empresa_id": 1,
            "setor": "Teste",
            "segmento": "Teste",
            "pvp": 1,
            "tag_along": 1,
            "free_float": 1,
            "graham": 1,
            "cotacao": 1,
            "pontuacao": 1,
        }

    def test_class_instance(self):
        estatistica = Estatisticas(**self.dados)

        self.assertIsInstance(estatistica, Estatisticas)
