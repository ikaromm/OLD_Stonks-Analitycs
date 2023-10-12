from stonks_analytics.db.entity.fii import Fii

from unittest import TestCase

class TestFii(TestCase):

    def setUp(self):
        self.dados = {
            "fundo_id": 1,
            "dy12m": 1,
            "cotacao": 1,
            "pvp": 1,
            "prazo": 1,
            "taxa_adm": 1,
            "vacancia": 1,
            "ult_rendimento": 1,
            "qnt_imoveis": 1,
            "dy5anos": 1,
            "pontuacao": 1,
        }

    def test_class_instance(self):
        fii = Fii(**self.dados)

        self.assertIsInstance(fii, Fii)    