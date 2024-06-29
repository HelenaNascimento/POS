import pandas as pd

#Seleção de conjunto de dados
#https://dados.gov.br/dados/conjuntos-dados/configuracoes-das-filas-de-analise-da-anvisa

def load_data():
    df = pd.read_csv("/home/technical/WorkSpace/POS/ETL/FILA_ANALISE_ASSUNTO_SITUACAO.csv")
    return df

df = load_data()

pd.DataFrame(df)



