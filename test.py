#!/bin/python

import requests

url = "https://losst.ru/"

resp = requests.get(url)

r = resp.text

#(r)

with open('audioknighi.html', 'w') as file:
  file.write(r)
  
  