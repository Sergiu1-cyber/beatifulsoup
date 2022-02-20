import requests
from bs4 import BeautifulSoup
import lxml

z = 1
while True:
    
    url = "https://losst.ru/"
    pg = f"page/{z}"
    pagine = url + pg

    resp = requests.get(pagine)
    
    soup = BeautifulSoup(resp.content, 'lxml')

    #div = soup.find_all('div', class_="article"

    info = soup.find_all('h2', class_="title post-title")
    
    f = open('comenzi.txt', 'a')

    for n in info:
        a = n.find('a')
        
        print(z)
        print('---')
        print(a.string)
        print(a.get('href'))
        print('---')
        
        f.write(str(z) + '\n')
        f.write('---' + '\n')
        f.write(a.string + '\n')
        f.write(a.get('href') + '\n')
        f.write('---' + '\n')
        
        z += 1

    
    
    
