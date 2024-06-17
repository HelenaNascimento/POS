#requests
#pandas
#BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd


URL_POS = 'https://www.unichristus.edu.br/nossos-cursos/pos-graduacao/'
URL_GRAD = 'https://www.unichristus.edu.br/nossos-cursos/graduacao/'
#URL = 'https://www.unichristus.edu.br/nossos-cursos/mestrado/'

reponse_POS = requests.get(URL_POS)
reponse_GRAD = requests.get(URL_GRAD)

if reponse_POS.status_code == 200 and reponse_GRAD.status_code == 200:
    print('Requisição bem sucedida')

    soup_POS = BeautifulSoup(reponse_POS.text, 'html.parser')

    cursos_POS = soup_POS.find_all('h2')

    cursos_POS = []
    
    for h2 in cursos_POS:
        a = h2.find('a', href = True)
        if a is not None:
            nome_curso = a.text.strip()
            url_curso = a['href'] 
            cursos_POS.append({'Curso': nome_curso, 'URL': url_curso})

    soup_GRAD = BeautifulSoup(reponse_GRAD.text, 'html.parser')

    cursos_GRAD = soup_GRAD.find_all('h2')

    cursos_GRAD = []
    
    for h2 in cursos_GRAD:
        a = h2.find('a', href = True)
        if a is not None:
            nome_curso = a.text.strip()
            url_curso = a['href'] 
            cursos_GRAD.append({'Curso': nome_curso, 'URL': url_curso})
    
    df_cursos_POS = pd.DataFrame(cursos_POS)
    df_cursos_GRAD = pd.DataFrame(cursos_GRAD)

    #print(df_cursos)

    df_cursos_POS.to_excel('cursos_POS.xlsx', index=False)
    df_cursos_GRAD.to_excel('cursos_GRAD.xlsx', index=False)

else:
    print('Erro na requisição')

