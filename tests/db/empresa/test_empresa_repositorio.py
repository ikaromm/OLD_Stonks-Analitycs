from stonks_analytics.db.repository.empresa_repositorio import EmpresaRepositorio
from stonks_analytics.db.entity.empresa import Empresa

from unittest import TestCase
from pathlib import Path

from sqlalchemy import create_engine


class TestEmpresaRepositorio(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///test.db')

    def tearDown(self):
        Path('test.db').unlink(missing_ok=True)

    def test_class_instance(self):
        empresa_repositorio = EmpresaRepositorio(self.engine)

        self.assertIsInstance(empresa_repositorio, EmpresaRepositorio)

    def test_get_all(self):

        empresas = [Empresa(codigo=f'TESTE{i}', nome=f'Teste {i}') for i in range(10)]

        empresa_repositorio = EmpresaRepositorio(self.engine)

        empresa_repositorio.add_all(empresas)

        empresas_salvas = empresa_repositorio.get_all()

        self.assertEqual(
            len(empresas),
            len(empresas_salvas)
        )


    def test_add(self):
        empresa_repositorio = EmpresaRepositorio(self.engine)

        empresa = Empresa(
            codigo='TESTE',
            nome='Teste'
        )

        empresa_repositorio.add(empresa)
        empresa_salva = empresa_repositorio.get(empresa.id)

        self.assertEqual(
            empresa.id, 
            empresa_salva.id
        )

    def test_update(self):
        empresa_repositorio = EmpresaRepositorio(self.engine)

        empresa = Empresa(
            codigo='TESTE',
            nome='Teste'
        )

        empresa_repositorio.add(empresa)

        empresa.nome = 'Teste 2'
        empresa_repositorio.update(empresa)

        empresa_salva = empresa_repositorio.get(empresa.id)

        self.assertEqual(
            empresa.nome, 
            empresa_salva.nome
        )

    def test_remove(self):
        empresa_repositorio = EmpresaRepositorio(self.engine)

        empresa = Empresa(
            codigo='TESTE',
            nome='Teste'
        )

        empresa_repositorio.add(empresa)
        empresa_repositorio.remove(empresa)

        empresa_salva = empresa_repositorio.get(empresa.id)

        self.assertIsNone(empresa_salva)