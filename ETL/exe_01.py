import pandas as pd

#Seleção de conjunto de dados
#https://dados.gov.br/dados/conjuntos-dados/configuracoes-das-filas-de-analise-da-anvisa

def load_data(df):
    df = pd.read_csv("TL\FILA_ANALISE_ASSUNTO_SITUACAO.csv")
    return df

pd.DataFrame(df)



