from entities import *

if __name__ == "__main__":
    i = InvestimentoSelicRecorrente(
        ticker="SELIC",
        value=100,
        start=datetime.datetime(year=2023, month=1, day=1),
        end=datetime.datetime.now(),
    )
    
    print(i.result.df_capital_cumprod)
    print(i.default.df_capital_cumprod)

    pass
    