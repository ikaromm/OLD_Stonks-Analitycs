from stonks_analytics.data_handler.data_handler import DataHandler

from unittest import TestCase, mock


class TestDataHandler(TestCase):
    def test_class_instance(self):
        handler = DataHandler()

        self.assertIsInstance(handler, DataHandler)

    def test_append(self):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mock_open.side_effect = FileNotFoundError
            
            handler = DataHandler()
            handler.load_data()

            dados = {
                "Empresa": 'Stonks',
                "Cotação": 0,
                "Divida Liquida": 0,
                "Custos": 0,
                "Lucro Bruto": 0,
                "Margem Bruta": 0,
                "Margem Ebita": 0,
                "Margem Liquida": 0,
                "Divida Bruta": 0,
                "ROE": 0,
                "Receita Liquida": 0,
                "EBITA": 0,
                "EBIT": 0,
                "Impostos": 0,
                "Margem EBITA": 0,
                "Lucro Liquido": 0,
                "Roic": 0,
                "Dy": 0,
                "P/VP": 0,
                "P/L": 0,
            }

            handler.append(dados)

            self.assertEqual(len(handler.loaded_data), 1)

            dados['Cotação'] = 1
            handler.append(dados)

            self.assertEqual(len(handler.loaded_data), 1)

            dados = handler.get_dados_from_empresa('Stonks')
            self.assertEqual(dados['Cotação'], 1)

