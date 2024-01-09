import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}                # this data we will send 
    if id is not None:
        data = {'id':id}
    headers = {'content-Type' : 'application/json'} #added 
    json_data = json.dumps(data)
    r = requests.get(url = URL,headers = headers, data = json_data) # headers added
    data = r.json()
    print(data)
    
    
#get_data()

def post_data():
    data = {
        'name' : 'Rakesh',
        'roll' : 189,
        'city' : 'mathura',
    }
    headers = {'content-Type' : 'application/json'} #added 
    
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers = headers, data = json_data)
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
 
   
     

        
        
