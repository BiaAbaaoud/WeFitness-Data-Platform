import pandas as pd
import sqlite3

# Conecta ao banco que acabamos de limpar
conn = sqlite3.connect('wefitness_warehouse.db')

# Lê a tabela fato final
fato_final = pd.read_sql("SELECT * FROM fato_checkin", conn)

# Salva em Parquet com compressão máxima
fato_final.to_parquet('wefitness_fato_final.parquet', compression='snappy', index=False)

conn.close()
print("📁 Warehouse sincronizado e Backup Parquet gerado com sucesso!")