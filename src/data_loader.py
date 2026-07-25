import pandas as pd
from pathlib import Path

def load_prices(symbols,data_path):
    data = {}
    loaded_symbols = []
    data_path = Path(data_path)

    for symbol in symbols:
        try:
            file = data_path / f"{symbol}.us.txt"
            df = pd.read_csv(file)
            df["Date"] = pd.to_datetime(df["Date"])
            df.set_index("Date", inplace=True)
            if "Close" in df.columns and not df["Close"].isnull().all():
                data[symbol] = df["Close"]
                loaded_symbols.append(symbol)
        except Exception as e:
            print(f"No fue posible cargar {symbol}: {e}")
            
    prices = pd.concat(data, axis=1).dropna().sort_index()
    print("Activos cargados:")
    print(loaded_symbols)
    return prices