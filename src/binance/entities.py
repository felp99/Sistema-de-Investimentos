import pandas as pd
from binance.client import Client

# Initialize the Binance client
client = Client('api_key', 'api_secret')

# Get all trades
trades = client.get_my_trades(symbol='BTCUSDT')

# Convert the trades to a DataFrame
df = pd.DataFrame(trades)

# Show the DataFrame
print(df)
