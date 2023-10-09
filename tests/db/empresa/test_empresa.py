from stonks_analytics.db.entity.empresa import Empresa

from unittest import TestCase


class TestEmpresa(TestCase):
    def test_class_instance(self):
        empresa = Empresa(codigo="TESTE", nome="Teste")

        self.assertIsInstance(empresa, Empresa)
