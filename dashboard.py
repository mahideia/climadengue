import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
import graficos 

st.set_page_config(
    page_title="ClimaDengue - Base dos Dados",
    page_icon=":mosquito:",
    layout="wide"
    )

st.image("banner.png")

col1, col2 = st.columns([3,2])

with col1:
    st.write("Este dashboard permite que você naveque pelos dados de notificações de casos de dengue do SINAN e de temperatura e precipitação de estações automáticas do INMET. \n A maioria dos dados utilizados aqui estão disponíveis no data lake da Base dos Dados")


#---
# carregar dados que serão utilizados
diarios = pd.read_csv('diarios.csv')
semanais = pd.read_csv('semanais.csv')
populacao = pd.read_csv('populacao.csv')


#---
# selecionar cidade
with col2:
    filtros = st.container(border=True)
    
with filtros:
    cidade = st.selectbox('Selecione a capital',semanais['cidade'].sort_values().unique())


#---
# filtrar e combinar os dados conforme necessidade
dados_diarios = diarios[diarios['cidade']==cidade]
dados_semanais = semanais[semanais['cidade']==cidade]
function_dict = {'temperatura_media':'mean','precipitacao':'sum','casos':'sum'}
dados_mensais = dados_diarios.groupby(by=['cidade','ano','mes']).aggregate(function_dict).reset_index()
dados_mensais = dados_mensais[dados_mensais['cidade']==cidade]
pop = populacao[populacao['cidade']==cidade]
dados_anuais = dados_mensais.groupby(by='ano').aggregate(function_dict).reset_index()

dados_semanais = dados_semanais.merge(pop,left_on='ano',right_on='ano')
dados_semanais['casos_100k'] = round(dados_semanais['casos']/dados_semanais['população']*100000)
dados_mensais = dados_mensais.merge(pop,left_on='ano',right_on='ano')
dados_mensais['casos_100k'] = round(dados_mensais['casos']/dados_mensais['população']*100000)

casos_totais = dados_mensais['casos'].sum()
ano_mais_casos = int(dados_anuais.loc[dados_anuais['casos']==dados_anuais['casos'].max(),'ano'].values[0])
print(ano_mais_casos)
#--- 
# criar as tabs
dengue, clima, climadengue = st.tabs(["Dengue","Clima e tempo","Clima e Dengue"])

#--- 
# tab1: DENGUE
# aqui ficarão: heatmap de casos por semana epidemiológica, casos por mês ao longo dos últimos 10 anos, casos por 100mil habitantes, por mês, ao longo dos últimos 10 anos.
with dengue:
    col_card1, col_card2, col_texto = st.columns([1,1,3])
    col_heatmap = st.columns(1)[0]
    col_casos_absolutos = st.columns(1)[0]
    #col_casos_100k = st.columns(1)

with col_card1:
    ui.metric_card(title='Total de casos',content=casos_totais,description='nos últimos dez anos')
with col_card2:
    ui.metric_card(title='Ano com mais casos',content=ano_mais_casos,description='nos últimos dez anos')
with col_texto:
    st.markdown("<p style='padding-top:10px'></p>", unsafe_allow_html=True)
    st.markdown("""
                Os dados utilizados para o desenvolvimento destas visualizações estão disponíveis no dataset [SINAN na Base dos Dados](https://basedosdados.org/dataset/f51134c2-5ab9-4bbc-882f-f1034603147a?table=9bdbca38-d97f-47fa-b422-84477a6b68c8). 
                Dados de população das capitais são das projeções disponíveis do Ministério da Saúde, acessados pelo [Tabnet](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?ibge/cnv/projpop2024uf.def)
                """)

with col_heatmap:
    pivot_semanais = pd.pivot_table(dados_semanais,values='casos_100k',index=['ano'],columns=['semana'],aggfunc='sum', fill_value=0)
    st.plotly_chart(graficos.heatmap(pivot_semanais), use_container_width=False)

with col_casos_absolutos:
    st.plotly_chart(graficos.casos_absolutos(dados_mensais))

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