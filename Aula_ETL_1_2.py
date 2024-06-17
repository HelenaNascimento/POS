import requests
from bs4 import BeautifulSoup
import pandas as pd


urls = ["https://www.unichristus.edu.br/nossos-cursos/pos-graduacao/", 
        "https://www.unichristus.edu.br/nossos-cursos/graduacao/"]

dados_cursos = {}

def extrair_dados_cursos(url):
    reponse = requests.get(url)

    if reponse.status_code == 200:
        print("Conexão OK")

        soup = BeautifulSoup(reponse.text, 'html.parser')
        cursos = soup.find_all('h2')

        for h2 in cursos:

            a = h2.find('a', href = True)

            if a is not None:
                nome_curso = a.text.strip()
                url_curso = a['href'] 
                dados_cursos[nome_curso] = {'Nome_Curso': nome_curso, 'URL':url_curso}

    else:
        print("Erro na conexão")

for url in urls:
    extrair_dados_cursos(url)

df_cursos = pd.DataFrame(dados_cursos.values(), index=dados_cursos.keys())

df_cursos.to_excel('Cursos.xlsx', index=False)

print(df_cursos)