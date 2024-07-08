import pandas as pd
import folium

"""
importar dados do arquivo para o programa 
Dados sobre Cidades do Estado do Ceará
Código do IBGE;
Descrição da Cidade;
Posição Longitude e;
Posição Latitude
"""
def dados_cidade():
    imp_dados_cidade = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/localizacao_cidades_CE.csv')
    return imp_dados_cidade


"""
importar dados sobre vendas dos clientes do mês de janeiro de 2024
Para selecionar a lista usei o select no banco SQL SERVER
  Select top 1000
    substring(cl.Fantasia, 1, 5) as Fantasia,
    Cod_CidIbge,
    sum(ve.Qtd_Total) as Qtd_Total_JAN,
    sum(ve.vlr_total) as vlr_total_JAN
  FROM tab_vendas vd
      inner join tab_cliente cl on vd.cod_clien = cod_clien
  where 
    dat_venda >= '20240101'
    dat_venda <= '20240130'
  group by 
    Cod_CidIbge

Como resultado da consulta vinheram os 1000 clientes que compraram no mês de Janeiro de 2024:
Fantasia, Código IBGE, Quantidade total de itens e valor total das compras dentro do perído

"""
 
def dados_vendas():
    imp_dados_vendas = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/Dados_Vendas_JAN.csv')
    return imp_dados_vendas


# Após ter carregado os arquivos, agora eu preciso juntar os dados para criar o mapa.


def merge_data(imp_dados_vendas, imp_dados_cidade):
    juncao_dos_dados = pd.merge(imp_dados_vendas, imp_dados_cidade, left_on='Cod_CidIbge', right_on='Cod_CidIbge', how='right')  # Corrigir para 'right'
    filtro_dados = juncao_dos_dados[['Fantasia', 'Cod_CidIbge', 'Cidade', 'Longitude', 'Latitude', 'Qtd_Total_JAN', 'vlr_total_JAN']]  # Ajustar os nomes das colunas
    return filtro_dados


# Agora preciso informar onde estão esses clientes no mapa
# É aqui onde a biblioteca folium entra

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
