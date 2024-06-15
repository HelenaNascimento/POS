#requests
#pandas
#BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.unichristus.edu.br/nossos-cursos/pos-graduacao/'

reponse = requests.get(URL)

if reponse.status_code == 200:
    print('Requisição bem sucedida')

    soup = BeautifulSoup(reponse.text, 'html.parser')

    cursos_link = soup.find_all('a', href = True)

    cursos = []
    
    for link in cursos_link:
        nome_curso = link.text.strip()
        url_curso = link['href'] 
        cursos.append({'Curso': nome_curso, 'URL': url_curso})
    
    df_cursos = pd.DataFrame(cursos)

    print(df_cursos)

else:
    print('Erro na requisição')

