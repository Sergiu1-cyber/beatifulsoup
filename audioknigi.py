import requests

url = "https://rutracker.net/forum/viewforum.php?f=2387"

HEADERS = {
  'Accept' : '*/*',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
   
}

resp = requests.get(url, headers=HEADERS)

r = resp.text

print(r)

#with open('audioknighi.html', 'w') as file:
  #file.write(r)
  
  
