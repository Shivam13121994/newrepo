# This is separate application. it has no relation with DRF or this project
# This application is extracting the data using get request.
# This application is requesting the data from our api, and getting the response.
import requests

URL = "http://127.0.0.1:8000/studentinfo/2"

r = requests.get(url = URL)

data = r.json()

print(data)



