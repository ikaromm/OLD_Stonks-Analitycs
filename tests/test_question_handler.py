from stonks_analytics.data_handler import QuestionHandler

from unittest import TestCase, mock


class TestQuestionHandler(TestCase):
    def test_class_instance(self):
        handler = QuestionHandler()

        self.assertIsInstance(handler, QuestionHandler)

    def test_append(self):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mock_open.side_effect = FileNotFoundError

            handler = QuestionHandler()
            handler.load_data()

            dados = {
                "Company Name": "Stonks",
                "DÍVIDA LÍQUIDA - LUCRO LÍQUIDO": 0,  # feito
                "DIVIDENDOS": 0,  # feito
                "LUCRO OPERACIONAL>0": 0,  # feito
                "P/VP abaixo de 5": 0,  # feito
                "Líquida/EBITDA é menor que 2": 0,  # feito
                "+30 anos de mercado? (Fundação)": 0,  # feito
                "P/L < 30": 0,  # feito
                "Crescimento de receitas lucro >5perc ultimos 5 anos": 0,
                "Soma_total": 0,
            }

            handler.append(dados)

            self.assertEqual(len(handler.loaded_data), 1)

            dados["DIVIDENDOS"] = 1
            handler.append(dados)

            self.assertEqual(len(handler.loaded_data), 1)
            question = handler.get_question_from_company("Stonks")
            self.assertEqual(question["DIVIDENDOS"], 1)

    def test_append_incomplete_dict(self):
        with mock.patch("builtins.open", mock.mock_open()) as mock_open:
            mock_open.side_effect = FileNotFoundError
            
            handler = QuestionHandler()
            handler.load_data()

            dados = {
                "Company Name": "Stonks",
                "DÍVIDA LÍQUIDA - LUCRO LÍQUIDO": 0,  # feito
                "DIVIDENDOS": 0,  # feito
                "LUCRO OPERACIONAL>0": 0,  # feito
                "P/VP abaixo de 5": 0,  # feito
                "Líquida/EBITDA é menor que 2": 0,  # feito
                "+30 anos de mercado? (Fundação)": 0,  # feito
                "P/L < 30": 0,  # feito
                "Crescimento de receitas lucro >5perc ultimos 5 anos": 0,
            }

            handler.append(dados)

            self.assertEqual(len(handler.loaded_data), 1)
