#streamlit - pip install streamlit - https://pypi.org/project/streamlit/
#pandas - pip install pandas - https://pypi.org/project/pandas/
#numpy - pip install numpy - https://pypi.org/project/numpy/
#sqlite - pip install db-sqlite3 - https://pypi.org/project/db-sqlite3/

#importação biblioteca

import sqlite3
import pandas as pd
import streamlit as st


#conexao sqlite

def conexao():
    con = sqlite3.connect("bancopet.sqlite")
    return con
  
def tab_FORNE():
    query = """SELECT * FROM FORNECEDOR"""
    test = pd.read_sql_query(query, con)
    return test  

def tab_CLIEN():
    query = """SELECT * FROM CLIENTE"""
    test = pd.read_sql_query(query, con)
    return test   

def tab_PRODU():
    query = """SELECT * FROM PRODUTO"""
    test = pd.read_sql_query(query, con)
    return test   
 
def tab_rel():
    query = """SELECT * FROM ENT_SAI_PROD"""
    test = pd.read_sql_query(query, con)
    return test 

def comp_prod():
    query = """SELECT 
                Nome_Fornecedor as Fornecedor, 
                sum(Ent_Qtd) as Qtd_Entrada
            FROM "ENT_SAI_PROD" rel
                inner join "FORNECEDOR" forn on rel.IdFornecedor = forn.IdFornecedor
            group by Nome_Fornecedor"""
    test = pd.read_sql_query(query, con)
    return test 

def vend_prod():
    query = """SELECT 
                Nome_Cliente as Cliente, 
                Classe,
                sum(Sai_Qtd) as Qtd_Venda
            FROM "ENT_SAI_PROD" rel
                inner join "CLIENTE" forn on rel.IdCliente = forn.IdCliente
            group by Nome_Cliente"""
    test = pd.read_sql_query(query, con)
    return test 

def viwer_estoque():
    query = """SELECT 
                *
            FROM ESTOQUE """
    test = pd.read_sql_query(query, con)
    return test 

con = conexao()
fornecedor = tab_FORNE()
cliente = tab_CLIEN()
produto = tab_PRODU()
relacao = tab_rel()
ent_prod = comp_prod()
sai_prod = vend_prod()
estoque = viwer_estoque()
 
st.set_page_config(
    page_title="BI - Pet",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

st.divider()
st.write("TABELAS BANCO PET")

col = st.columns(4)

with col[0]:
    with st.container(border = True):
        st.write("Fornecedor")
        st.dataframe(fornecedor)
with col[1]:
    with st.container(border = True):
        st.write("Cliente")
        st.dataframe(cliente)
with col[2]:
    with st.container(border = True):
        st.write("Produto")
        st.dataframe(produto)
with col[3]:
    with st.container(border = True):
        st.write("Relação")
        st.dataframe(relacao)
        
st.divider()
st.write("Viewer Estoque")
st.dataframe(estoque)

st.divider()

st.write("Compras X Produto")
entrada = pd.DataFrame(ent_prod)
exibi = ent_prod[['Qtd_Entrada', 'Fornecedor']]
exibi.set_index('Fornecedor', inplace=True)

col = st.columns((1.5, 6))
with col[0]:
    st.dataframe(entrada)
with col[1]:
    st.bar_chart(exibi)

st.divider()

st.write("Venda X Produto")
saida = pd.DataFrame(sai_prod)
exibi_saida = sai_prod[['Qtd_Venda', 'Cliente']]
exibi_saida.set_index('Cliente', inplace=True)

col = st.columns((1.5, 6))
with col[0]:
    st.dataframe(saida)
with col[1]:
    st.bar_chart(exibi_saida)