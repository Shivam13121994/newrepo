import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}                # this data we will send 
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
    
    
#get_data()

def post_data():
    data = {
        'name' : 'Mohan',
        'roll' : 126,
        'city' : 'varanasi',
    }
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    
    

post_data()

def update_data():
    data = {
        'id' : 4,                 # since we are giving only name, city not roll. hence it is a partial update
        'name' : 'Thakur',
        'city' : 'London',
    }
    
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
    
#update_data()


def delete_data():
    data = {
        'id' : 7,               

    }
    
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
    
#delete_data()
 
   
     

        
        
