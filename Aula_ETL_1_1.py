#requests
#pandas
#BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd


#URL = 'https://www.unichristus.edu.br/nossos-cursos/pos-graduacao/'
#URL = 'https://www.unichristus.edu.br/nossos-cursos/graduacao/'
URL = 'https://www.unichristus.edu.br/nossos-cursos/mestrado/'

reponse = requests.get(URL)

if reponse.status_code == 200:
    print('Requisição bem sucedida')

    soup = BeautifulSoup(reponse.text, 'html.parser')

    cursos_link = soup.find_all('h2')

    cursos = []
    
    for h2 in cursos_link:
        a = h2.find('a', href = True)
        if a is not None:
            nome_curso = a.text.strip()
            url_curso = a['href'] 
            cursos.append({'Curso': nome_curso, 'URL': url_curso})
    
    df_cursos = pd.DataFrame(cursos)

    #print(df_cursos)

    df_cursos.to_excel('cursos_mestrado.xlsx', index=False)

else:
    print('Erro na requisição')

