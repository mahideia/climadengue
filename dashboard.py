import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout="wide")


#---
# carregar dados que serão utilizados
diarios = pd.read_csv('diarios.csv')
semanais = pd.read_csv('semanais.csv')


#--- 
#criar uma seleção na barralateral do dashboard
cidade = st.sidebar.selectbox('Capital',semanais['cidade'].unique())
ano = st.sidebar.selectbox('Ano',semanais['ano'].unique())

#filtrar dados considerando as seleções
dados_diarios = diarios[(diarios['ano']==ano) & (diarios['cidade']==cidade)]
dados_semanais = semanais[(semanais['ano']==ano)&(semanais['cidade']==cidade)]
function_dict = {'temperatura_media':'mean','precipitacao':'sum','casos':'sum'}
dados_mensais = dados_diarios.groupby(by=['cidade','ano','mes']).aggregate(function_dict).reset_index()


#-- layout?
l1_c1, l1_c2 = st.columns(2)  # Primeira linha com duas colunas
l2_c1 = st.columns(1)  # Segunda linha com três colunas
l3_c1 = st.columns(1)  # terceira  linha com três colunas?


#--- gráficos
#climograma
fig_climograma = make_subplots(specs=[[{"secondary_y": True}]])
fig_climograma.add_trace(
    go.Bar(x=dados_mensais['mes'], y=dados_mensais['precipitacao'], name="Precipitação (mm)"),
    secondary_y=False,
)
fig_climograma.add_trace(
    go.Scatter(x=dados_mensais['mes'], y=dados_mensais['temperatura_media'], name="Temperatura média (°C)"),
    secondary_y=True,
)
fig_climograma.update_layout(title_text=f"Climograma - {ano}")
fig_climograma.update_xaxes(title_text="Mês")
fig_climograma.update_yaxes(title_text="Precipitação (mm)", secondary_y=False)
fig_climograma.update_yaxes(title_text="Temperatura média (°C)", secondary_y=True)
fig_climograma.update_layout(plot_bgcolor='white')
fig_climograma.update_layout(xaxis={'tickmode':'linear'})
fig_climograma.update_layout(yaxis2={'rangemode':'tozero'})

#casos por m}es
fig_casos = go.Figure()
fig_casos.add_trace(
    go.Bar(x=dados_mensais['mes'],y=dados_mensais['casos'],marker_color='teal')
)
fig_casos.update_xaxes(title_text="Mês")
fig_casos.update_yaxes(title_text="Notificações")
fig_casos.update_layout(title_text=f"Casos de Dengue - {ano}")
fig_casos.update_layout(xaxis={'tickmode':'linear'})
fig_casos.update_layout(plot_bgcolor='white')

#temperatura media e casos por semana epidemiologica
fig_temp_casos = make_subplots(specs=[[{"secondary_y": True}]])
fig_temp_casos.add_trace(
    go.Bar(x=dados_semanais['semana'], y=dados_semanais['casos'], name="Notificações",marker_color='teal'),
    secondary_y=False,
)
fig_temp_casos.add_trace(
    go.Scatter(x=dados_semanais['semana'], y=dados_semanais['temperatura_media'], name="Temperatura média (°C)"),
    secondary_y=True,
)
fig_temp_casos.update_layout(title_text=f"Casos e Temperatura")
fig_temp_casos.update_xaxes(title_text="Semana epidemiológica")
fig_temp_casos.update_yaxes(title_text="Precipitação (mm)", secondary_y=False)
fig_temp_casos.update_yaxes(title_text="Temperatura média (°C)", secondary_y=True)
fig_temp_casos.update_layout(plot_bgcolor='white')
fig_temp_casos.update_layout(yaxis2={'rangemode':'tozero'})


#precipitacao total e casos por semana epidemiologica
fig_precip_casos = make_subplots(specs=[[{"secondary_y": True}]])
fig_precip_casos.add_trace(
    go.Bar(x=dados_semanais['semana'], y=dados_semanais['casos'], name="Notificações",marker_color='teal'),
    secondary_y=False,
)
fig_precip_casos.add_trace(
    go.Scatter(x=dados_semanais['semana'], y=dados_semanais['precipitacao'], name="Precipitação (mm)",marker_color='blue'),
    secondary_y=True,
)
fig_precip_casos.update_layout(title_text=f"Casos e Precipitação")
fig_precip_casos.update_xaxes(title_text="Semana epidemiológica")
fig_precip_casos.update_yaxes(title_text="Casos", secondary_y=False)
fig_precip_casos.update_yaxes(title_text="Precipitação (mm)", secondary_y=True)
fig_precip_casos.update_layout(plot_bgcolor='white')
fig_precip_casos.update_layout(yaxis={'rangemode':'tozero'})

#---
#exibir os gráficos nos lugares certos
l1_c1.plotly_chart(fig_climograma, use_container_width=True)
l1_c2.plotly_chart(fig_casos, use_container_width=True)
l2_c1[0].plotly_chart(fig_temp_casos, use_container_width=True)
l3_c1[0].plotly_chart(fig_precip_casos, use_container_width=True)