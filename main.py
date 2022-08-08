from utils.json_handler import read_database,save_to_database
from management.tab_handler import totalvalue

if __name__ == "__main__":
   
    def rewritejson():
        new_item = {"name": "CHURROS DO M5", "price": 5.0}
        nuvem = read_database()
        nuvem.append({"id":len(nuvem) + 1, "name":new_item["name"], "price":new_item["price"]})
        save_to_database(nuvem)

    rewritejson()
    print(read_database())

    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    
    print(totalvalue(table_1))
