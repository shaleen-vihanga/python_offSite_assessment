import pandas as pd

def get_past_aapl_price(filename="stock_data.csv"):
    df = pd.read_csv(filename)

    stock_data = df[df['Company'] == 'AAPL']


    aapl_price = stock_data.iloc[-1]['Price']
    return aapl_price

# price = get_past_aapl_price("stock_data.csv")
# print (price)
