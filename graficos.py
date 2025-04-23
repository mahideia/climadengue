
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots





#--- gráficos
#climograma
def climograma(dados_mensais):
    fig_climograma = make_subplots(specs=[[{"secondary_y": True}]])
    fig_climograma.add_trace(
        go.Bar(x=dados_mensais['mes'], y=dados_mensais['precipitacao'], name="Precipitação (mm)"),
        secondary_y=False,
    )
    fig_climograma.add_trace(
        go.Scatter(x=dados_mensais['mes'], y=dados_mensais['temperatura_media'], name="Temperatura média (°C)"),
        secondary_y=True,
    )
    fig_climograma.update_layout(title_text=f"Climograma")
    fig_climograma.update_xaxes(title_text="Mês")
    fig_climograma.update_yaxes(title_text="Precipitação (mm)", secondary_y=False)
    fig_climograma.update_yaxes(title_text="Temperatura média (°C)", secondary_y=True)
    fig_climograma.update_layout(plot_bgcolor='white')
    fig_climograma.update_layout(xaxis={'tickmode':'linear'})
    fig_climograma.update_layout(yaxis2={'rangemode':'tozero'})
    return fig_climograma

#casos por mês
def casos(dados_mensais):
    fig_casos = go.Figure()
    fig_casos.add_trace(
        go.Bar(x=dados_mensais['mes'],y=dados_mensais['casos'],marker_color='teal')
    )
    fig_casos.update_xaxes(title_text="Mês")
    fig_casos.update_yaxes(title_text="Notificações")
    fig_casos.update_layout(title_text=f"Casos de Dengue")
    fig_casos.update_layout(xaxis={'tickmode':'linear'})
    fig_casos.update_layout(plot_bgcolor='white')
    return fig_casos

#temperatura media e casos por semana epidemiologica
def temp_casos(dados_semanais):
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
    return fig_temp_casos

#precipitacao total e casos por semana epidemiologica
def precip_casos(dados_semanais):
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
    return fig_precip_casos