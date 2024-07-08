import pandas as pd
import folium

# Função para carregar dados de cidades
def dados_cidade():
    imp_dados_cidade = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/localizacao_cidades_CE.csv', delimiter=';')
    print("Colunas do DataFrame de Cidades:", imp_dados_cidade.columns)
    # Renomear as colunas para corresponder ao que é esperado no merge
    imp_dados_cidade.rename(columns={'Longe': 'Longitude', 'Latit': 'Latitude'}, inplace=True)
    return imp_dados_cidade

# Função para carregar dados de vendas
def dados_vendas():
    imp_dados_vendas = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/Dados_Vendas_JAN.csv', delimiter=';')
    print("Colunas do DataFrame de Vendas:", imp_dados_vendas.columns)
    return imp_dados_vendas

# Função para combinar dados
def merge_data(imp_dados_vendas, imp_dados_cidade):
    print("Verificando nomes das colunas antes do merge:")
    print("Colunas de vendas:", imp_dados_vendas.columns)
    print("Colunas de cidades:", imp_dados_cidade.columns)
    
    juncao_dos_dados = pd.merge(imp_dados_vendas, imp_dados_cidade, left_on='Cod_CidIbge', right_on='Cod_CidIbge', how='right')
    filtro_dados = juncao_dos_dados[['Fantasia', 'Cod_CidIbge', 'Cidade', 'Longitude', 'Latitude', 'Qtd_Total_JAN', 'vlr_total_JAN']]
    return filtro_dados

# Função para criar mapa
def create_map(dados):
    mapa = folium.Map(location=[-3.71722, -38.5433], zoom_start=7)  # Coordenadas aproximadas do Ceará
    for _, row in dados.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Fantasia']}<br>Qtd Venda: {row['Qtd_Total_JAN']}<br>Vlr Venda: {row['vlr_total_JAN']}",
            tooltip=row['Cidade']
        ).add_to(mapa)
    return mapa

imp_dados_cidade = dados_cidade()  # Carregar os dados da tabela cidade
imp_dados_vendas = dados_vendas()  # Carregar os dados de Vendas

dados_combinados = merge_data(imp_dados_vendas, imp_dados_cidade)  # Carregar os dados combinados

mapa_vendas = create_map(dados_combinados)  # Criar o mapa

mapa_vendas
