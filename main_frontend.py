import requests
import time

# http://<host ip>:5000/
url = "http://127.0.0.1:5000/"
while 1 :
    response = requests.get(url)
    data = response.text
    print(data)
    time.sleep(2)