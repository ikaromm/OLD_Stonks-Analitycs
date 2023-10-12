from stonks_analytics.db.repository.fundo_repositorio import FundoRepositorio
from stonks_analytics.db.entity.fii_fundo import Fundo

from unittest import TestCase
from pathlib import Path

from sqlalchemy import create_engine


class TestFundoRepositorio(TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///test.db")

    def tearDown(self):
        Path("test.db").unlink(missing_ok=True)

    def test_class_instance(self):
        fundo_repositorio = FundoRepositorio(self.engine)

        self.assertIsInstance(fundo_repositorio, FundoRepositorio)

    def test_get_all(self):
        fundos = [
            Fundo(codigo=f"TESTE{i}", nome=f"Teste {i}") for i in range(10)
        ]    

        fundo_repositorio = FundoRepositorio(self.engine)

        fundo_repositorio.add_all(fundos)

        fundos_salvas = fundo_repositorio.get_all()

        self.assertEqual(len(fundos), len(fundos_salvas))

    def test_add(self):
        fundo_repositorio = FundoRepositorio(self.engine)

        fundo = Fundo(codigo="TESTE", nome="Teste")

        fundo_repositorio.add(fundo)
        fundo_salva = fundo_repositorio.get(fundo.id)

        self.assertEqual(fundo.id, fundo_salva.id)

    def test_remove(self):
        fundo_repositorio = FundoRepositorio(self.engine)

        fundo = Fundo(codigo="TESTE", nome="Teste")

        fundo_repositorio.add(fundo)
        fundo_repositorio.remove(fundo)

        fundo_salva = fundo_repositorio.get(fundo.id)

        self.assertIsNone(fundo_salva)