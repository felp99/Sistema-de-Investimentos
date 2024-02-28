import unittest
import datetime
from entities import *

class TestAnalise(unittest.TestCase):

    def setUp(self):
        self.dfu = DataFrameUtil()

    def test_investimento_ticker(self):
        i = InvestimentoTicker(
            ticker="PETZ3.SA",
            value=2000,
            start=datetime.datetime(year=2020, month=1, day=1),
            end=datetime.datetime.now(),
        )

        self.assertIsNotNone(i.result.df_cumprod)
        self.assertIsNotNone(i.default.df_cumprod)

    def test_investimento_selic(self):
        i = InvestimentoSelic(
            ticker="SELIC",
            value=2000,
            start=datetime.datetime(year=2020, month=1, day=1),
            end=datetime.datetime.now(),
        )
        
        self.assertIsNotNone(i.result.df_cumprod)
        self.assertIsNotNone(i.default.df_cumprod)

    def test_investimento_selic_recorrente(self):
        i = InvestimentoSelicRecorrente(
            ticker="SELIC",
            value=100,
            start=datetime.datetime(year=2023, month=1, day=1),
            end=datetime.datetime.now(),
        )

        self.assertIsNotNone(i.result.df_cumprod)
        self.assertIsNotNone(i.default.df_cumprod)

    def test_investimento_carteira(self):
        c = Carteira([
            InvestimentoSelicRecorrente(
                ticker="SELIC",
                value=100,
                start=datetime.datetime(year=2023, month=1, day=1),
                end=datetime.datetime.now(),
                freq="M"),
            InvestimentoTickerRecorrente(
                ticker="^BVSP",
                value=50,
                start=datetime.datetime(year=2023, month=6, day=1),
                end=datetime.datetime.now(),
                freq="M"),
        ])

        self.assertIsNotNone(c.result.df_cumprod)
        self.assertIsNotNone(c.default.df_cumprod)

if __name__ == '__main__':
    unittest.main()