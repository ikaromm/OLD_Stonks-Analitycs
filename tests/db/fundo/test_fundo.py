from stonks_analytics.db.entity.fii_fundo import Fundo
from unittest import TestCase


class TestFundo(TestCase):
    def test_class_instance(self):
        fundo = Fundo(codigo="TESTE", nome="Teste")

        self.assertIsInstance(fundo, Fundo)
