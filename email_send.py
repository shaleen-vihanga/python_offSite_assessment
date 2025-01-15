from old_price import get_past_aapl_price
from email_config import send_email
from new_price import get_current_aapl_price


def price_alert(threshold=2.0):
    try:
        current_price = get_current_aapl_price()
    except Exception as e:
        print(f"Error fetching current price: {e}")
        return
    
    previous_price = get_past_aapl_price("stock_data.csv")
    try:
        price_change = current_price - previous_price
    except Exception as e:
        print(f"Error fetching previous price from CSV: {e}")
        return
    
    price_change = current_price - previous_price
    price_change = round(price_change,2)

    if abs(price_change) > threshold:
        try:
            send_email(previous_price, current_price, price_change)
            print(f"Price Alert! Price changed by {price_change}")
        except Exception as e:
            print(f"Error sending email: {e}")
    else:
        print("No significant price change, record,")

price_alert()