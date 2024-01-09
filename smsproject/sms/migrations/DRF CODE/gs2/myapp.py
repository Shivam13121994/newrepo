# this is a third party app, no connection with this project
import requests
import json

URL = "http://127.0.0.1:8000/stucreate/" # From urls.py

data = {
    'name' : 'sonam',
    'roll' : 101,
    'city' : 'Ranchi'    
} # this data is in python we need to change it in json we can use dumps method

json_data = json.dumps(data)
# Now we can send this json_data with request
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)


# Now this json data is sent to our API. Now we have to take this data in views.py
# and we have to deserialize it. and change it to complex data. and save that complex data in models table.


