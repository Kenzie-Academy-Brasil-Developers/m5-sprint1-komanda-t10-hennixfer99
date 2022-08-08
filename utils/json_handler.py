import json

def read_database():

    try:    
        
        with open('menu.json',encoding="utf-8") as file:
             lecture = json.load(file)
    except(json.JSONDecodeError,FileNotFoundError,FileExistsError):
             return []
             
    return lecture
    

         
def save_to_database(data: dict):
    with open('menu.json', "w") as database:
      return json.dump(data, database, indent=4)
        