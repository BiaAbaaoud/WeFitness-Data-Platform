import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="WeFitness Analytics", layout="wide")

# Estilo CSS para letras simples e cores sóbrias
st.markdown("""
    <style>
    .main { background-color: #F5F5F5; }
    h1, h2, h3 { color: #333333; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Conexão com o Warehouse
conn = sqlite3.connect('wefitness_warehouse.db')

# Título
st.title("📊 Dashboard de Performance - Rede WeFitness")

# --- CARGA DE DADOS ---
df_fato = pd.read_sql("SELECT * FROM fato_checkin", conn)
df_unidade = pd.read_sql("SELECT * FROM dim_unidade", conn)

# 1. KPIs Principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Faturamento Total", f"R$ {df_fato['valor_repasse'].sum():,.2f}")
with col2:
    st.metric("Total de Check-ins", len(df_fato))
with col3:
    st.metric("Ticket Médio", f"R$ {df_fato['valor_repasse'].mean():,.2f}")

st.markdown("---")

# 2. GRÁFICOS
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("Preferência por Modalidade")
    df_cat = pd.merge(df_fato, df_unidade, on='id_unidade')
    pizza_data = df_cat.groupby('categoria_servico').size().reset_index(name='quantidade')
    
    fig_pizza = px.pie(pizza_data, values='quantidade', names='categoria_servico',
                 color_discrete_sequence=px.colors.sequential.Blues_r,
                 hole=0.4)
    fig_pizza.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pizza, use_container_width=True)

with col_dir:
    st.subheader("Faturamento por Unidade")
    bar_data = df_cat.groupby('unidade_wefitness')['valor_repasse'].sum().sort_values(ascending=True).reset_index()
    
    fig_bar = px.bar(bar_data, x='valor_repasse', y='unidade_wefitness', 
                     orientation='h',
                     color_discrete_sequence=['#4A90E2'])
    fig_bar.update_layout(xaxis_title="Faturamento (R$)", yaxis_title=None)
    st.plotly_chart(fig_bar, use_container_width=True)

conn.close()