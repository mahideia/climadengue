import streamlit as st
import pandas as pd

import graficos 

st.set_page_config(layout="wide")

st.image("banner.png")
st.write("Este dashboard permite que você naveque pelos dados de notificações de casos de dengue do SINAN e de temperatura e precipitação de estações automáticas do INMET. \n A maioria dos dados utilizados aqui estão disponíveis no data lake da Base dos Dados")
#st.write("A maioria dos dados utilizados aqui estão disponíveis no data lake da Base dos Dados")

#---
# carregar dados que serão utilizados
diarios = pd.read_csv('diarios.csv')
semanais = pd.read_csv('semanais.csv')


#---
# selecionar cidade
st.selectbox('Selecione a capital',semanais['cidade'].sort_values().unique())

#--- 
# criar as tabs
dengue, clima, climadengue = st.tabs(["Dengue","Clima e tempo","ClimaDengue"])

#--- 
#criar uma seleção na barral ateral do dashboard
#cidade = st.sidebar.selectbox('Capital',semanais['cidade'].unique())
#ano = st.sidebar.selectbox('Ano',semanais['ano'].unique())

#filtrar dados considerando as seleções
#dados_diarios = diarios[(diarios['ano']==ano) & (diarios['cidade']==cidade)]
#dados_semanais = semanais[(semanais['ano']==ano)&(semanais['cidade']==cidade)]
#function_dict = {'temperatura_media':'mean','precipitacao':'sum','casos':'sum'}
#dados_mensais = dados_diarios.groupby(by=['cidade','ano','mes']).aggregate(function_dict).reset_index()


#-- layout?
#l1_c1, l1_c2 = st.columns(2)  # Primeira linha com duas colunas
#l2_c1 = st.columns(1)  # Segunda linha com três colunas
#l3_c1 = st.columns(1)  # terceira  linha com três colunas?




#---
#exibir os gráficos nos lugares certos
#l1_c1.plotly_chart(graficos.climograma(dados_mensais), use_container_width=True)
#l1_c2.plotly_chart(graficos.casos(dados_mensais), use_container_width=True)
#l2_c1[0].plotly_chart(graficos.temp_casos(dados_semanais), use_container_width=True)
#l3_c1[0].plotly_chart(graficos.precip_casos(dados_semanais), use_container_width=True)