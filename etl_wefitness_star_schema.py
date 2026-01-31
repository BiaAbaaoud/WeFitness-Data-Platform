import pandas as pd
import sqlite3
import os

# 1. EXTRAÇÃO
df = pd.read_json('checkins_raw.json')

# 2. TRANSFORMAÇÃO
# --- Dimensão Tempo ---
df['data_hora'] = pd.to_datetime(df['data_hora'])
dim_tempo = pd.DataFrame()
dim_tempo['id_tempo'] = df['data_hora'].dt.strftime('%Y%m%d%H%M')
dim_tempo['data'] = df['data_hora'].dt.date
dim_tempo['dia_semana'] = df['data_hora'].dt.day_name()
dim_tempo = dim_tempo.drop_duplicates(subset=['id_tempo'])

# --- Dimensão Usuário ---
dim_usuario = df[['usuario_id', 'nome_usuario', 'plano_usuario']].drop_duplicates(subset=['usuario_id'])

# --- Dimensão Unidade ---
unidades_unicas = df[['unidade_wefitness', 'categoria_servico']].drop_duplicates(subset=['unidade_wefitness'])
unidades_unicas['id_unidade'] = range(1, len(unidades_unicas) + 1)
dim_unidade = unidades_unicas[['id_unidade', 'unidade_wefitness', 'categoria_servico']]

# --- Tabela Fato (AQUI ESTÁ A CORREÇÃO) ---
# Fazemos o merge e IMEDIATAMENTE removemos duplicadas que podem ter surgido
fato_checkin = df.merge(dim_unidade, on='unidade_wefitness')
fato_checkin['id_tempo'] = fato_checkin['data_hora'].dt.strftime('%Y%m%d%H%M')

# Mantemos APENAS as colunas da fato e removemos qualquer linha duplicada acidental
fato_checkin = fato_checkin[['id_transacao', 'usuario_id', 'id_unidade', 'id_tempo', 'valor_repasse']]
fato_checkin = fato_checkin.drop_duplicates(subset=['id_transacao']) # TRAVA DE SEGURANÇA

# 3. CARGA
conn = sqlite3.connect('wefitness_warehouse.db')

# O 'replace' garante que o banco seja limpo antes de inserir os dados novos
dim_tempo.to_sql('dim_tempo', conn, if_exists='replace', index=False)
dim_usuario.to_sql('dim_usuario', conn, if_exists='replace', index=False)
dim_unidade.to_sql('dim_unidade', conn, if_exists='replace', index=False)
fato_checkin.to_sql('fato_checkin', conn, if_exists='replace', index=False)

conn.close()
print(f"✅ ETL corrigido! Total final na Fato: {len(fato_checkin)} linhas.")