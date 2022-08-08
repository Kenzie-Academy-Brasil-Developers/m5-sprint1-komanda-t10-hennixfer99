from datetime import date, time, datetime, timedelta, timezone;
from utils.json_handler import read_database

def totalvalue(data:dict):
    
    nuvem = read_database()
    delivered = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    finalprice = []
    for key in data:
        for product in nuvem:
             if key["id"] == product["id"]:
                finalprice.append(key["amount"]*product["price"])

    comanda = {"subtotal":sum(finalprice), "created_at":delivered}
    
    return comanda
