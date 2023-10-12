from stonks_analytics.db.repository.fii_repositorio import FiiRepositorio
from stonks_analytics.db.entity.fii_fundo import Fundo

from stonks_analytics.db.repository.fii_repositorio import (
    FiiRepositorio,
)
from stonks_analytics.db.entity.fii import Fii

from unittest import TestCase
from pathlib import Path

from sqlalchemy import create_engine

from stonks_analytics.db.repository.fundo_repositorio import FundoRepositorio

class TestFii(TestCase):

    def setUp(self):
        self.engine = create_engine("sqlite:///test.db")

        self.fundo = Fundo(codigo="TESTE", nome="Teste")
        self.fundo_repositorio = FundoRepositorio(self.engine)
        self.fundo_repositorio.add(self.fundo)

        
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

    def tearDown(self):
        Path("test.db").unlink(missing_ok=True)

    def test_add(self):
        fii = Fii(**self.dados)

        fii_repositorio = FiiRepositorio(self.engine)

        fii_repositorio.add(fii)
        fii_salva = fii_repositorio.get(fii.id)

        self.assertEqual(fii.id, fii_salva.id)

    def test_get_all(self):

        fiis = []
        fundo_repositorio = FundoRepositorio(self.engine)

        fii_repositorio = FiiRepositorio(self.engine)

        fii_existentes = fii_repositorio.get_all()

        for i in range(10):
            fundo = Fundo(codigo=f"TESTE{i}", nome=f"Teste{i}")
            fundo_repositorio.add(fundo)
            
            fii = Fii(
                fundo_id=fundo.id,
                dy12m=1,
                cotacao=1,
                pvp=1,
                prazo=1,
                taxa_adm=1,
                vacancia=1,
                ult_rendimento=1,
                qnt_imoveis=1,
                dy5anos=1,
                pontuacao=i,
            )    

            fiis.append(fii)

        
        fii_repositorio.add_all(fiis)

        fii_salvas = fii_repositorio.get_all()

        self.assertEqual(len(fiis), len(fii_salvas))    