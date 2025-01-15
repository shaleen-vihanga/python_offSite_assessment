import requests
from bs4 import BeautifulSoup

def get_current_aapl_price():
    url = "https://finance.yahoo.com/quote/AAPL/?p=AAPL"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    aapl_price = soup.find('span', {'data-testid': 'qsp-price'})
    if aapl_price:
        price = float(aapl_price.text.replace(',', ''))
        return price
    else:
        return None
    

    
# stock_price = get_current_aapl_price()
# if stock_price:
#     print (f"Current stock price of Apple is : ${stock_price}")
# else:
#     print ("failed to retreve stock price")
