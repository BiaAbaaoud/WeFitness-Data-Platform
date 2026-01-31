import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="WeFitness Analytics", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #F5F5F5; }
    h1, h2, h3 { color: #333333; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Título
st.title("📊 Dashboard de Performance - Rede WeFitness")

# --- CARGA DE DADOS (USANDO PARQUET PARA FUNCIONAR ONLINE) ---
# Lendo os arquivos que você subiu para o GitHub
df_fato = pd.read_parquet('wefitness_fato_final.parquet')

# Para as unidades, como não tínhamos parquet dela, vamos simular os nomes 
# ou você pode subir a dim_unidade em parquet também. 
# Por hora, vamos usar a fato que já tem os IDs.
# Se você tiver a dim_unidade.parquet, use: df_unidade = pd.read_parquet('dim_unidade.parquet')

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
    st.subheader("Volume de Check-ins")
    # Gráfico simples de pizza usando a coluna que tiver disponível
    fig_pizza = px.pie(df_fato, values='valor_repasse', names='id_unidade',
                 color_discrete_sequence=px.colors.sequential.Blues_r,
                 hole=0.4)
    st.plotly_chart(fig_pizza, use_container_width=True)

with col_dir:
    st.subheader("Faturamento por ID de Unidade")
    bar_data = df_fato.groupby('id_unidade')['valor_repasse'].sum().reset_index()
    fig_bar = px.bar(bar_data, x='valor_repasse', y='id_unidade', orientation='h')
    st.plotly_chart(fig_bar, use_container_width=True)