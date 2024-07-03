import pandas as pd
import folium
import folium.plugins

# Função para carregar os dados das cidades
def dados_cidade():
    imp_dados_cidade = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/localizacao_cidades_CE.csv')
    return imp_dados_cidade

# Função para carregar os dados das vendas
def dados_vendas():
    imp_dados_vendas = pd.read_csv('/home/technical/WorkSpace/POS/ETL/Ativ_extra/DADOS/Dados_Vendas_JAN.csv')
    return imp_dados_vendas

# Função para verificar os nomes das colunas
def verificar_colunas(dados_vendas, dados_cidade):
    print("Colunas em dados_vendas:", dados_vendas.columns)
    print("Colunas em dados_cidade:", dados_cidade.columns)

# Função para combinar os dados
def merge_data(imp_dados_vendas, imp_dados_cidade):
    verificar_colunas(imp_dados_vendas, imp_dados_cidade)  # Verificando os nomes das colunas
    juncao_dos_dados = pd.merge(imp_dados_vendas, imp_dados_cidade, left_on='Cod_CidIbge', right_on='Cod_CidIbge', how='inner')
    filtro_dados = juncao_dos_dados[['Fantasia', 'Cidade', 'Longitude', 'Latitude', 'Qtd_Total_JAN', 'vlr_total_JAN']]
    return filtro_dados

# Função para criar o mapa
def create_map(dados):
    mapa = folium.Map(location=[-3.71722, -38.5433], zoom_start=7)  # Coordenadas aproximadas do Ceará
    for _, row in dados.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Fantasia']}<br>Qtd Venda: {row['Qtd_Total_JAN']}<br>Vlr Venda: {row['vlr_total_JAN']}",
            tooltip=row['Cidade']
        ).add_to(mapa)
    return mapa

# Carregar os dados
imp_dados_cidade = dados_cidade()  # Carregar os dados da tabela cidade
imp_dados_vendas = dados_vendas()  # Carregar os dados de vendas

# Verificar os nomes das colunas
verificar_colunas(imp_dados_vendas, imp_dados_cidade)

# Combinar os dados
dados_combinados = merge_data(imp_dados_vendas, imp_dados_cidade)  # Carregar os dados combinados

# Criar o mapa
mapa_vendas = create_map(dados_combinados)  # Criar o mapa

# Salvar o mapa em um arquivo HTML
mapa_vendas.save('mapa_vendas.html')

# Mensagem de sucesso
print("O mapa foi salvo como 'mapa_vendas.html'.")
