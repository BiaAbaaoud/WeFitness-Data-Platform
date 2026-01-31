import sqlite3
import pandas as pd

def rodar_auditoria():
    conn = sqlite3.connect('wefitness_warehouse.db')
    
    print("--- 🕵️ RELATÓRIO DE QUALIDADE DE DADOS (DATA QUALITY) ---")
    
    # 1. Verificar Nulos
    fato = pd.read_sql("SELECT * FROM fato_checkin", conn)
    nulos = fato.isnull().sum().sum()
    print(f"✅ Valores Nulos: {nulos}")
    
    # 2. Verificar Duplicatas na Fato
    duplicatas = fato.duplicated(subset=['id_transacao']).sum()
    print(f"✅ Transações Duplicadas: {duplicatas}")
    
    # 3. Resumo por Plano (Visão de Negócio para TotalPass)
    query_plano = """
    SELECT u.plano_usuario, COUNT(f.id_transacao) as total_checkins, SUM(f.valor_repasse) as total_repasse
    FROM fato_checkin f
    JOIN dim_usuario u ON f.usuario_id = u.usuario_id
    GROUP BY u.plano_usuario
    ORDER BY total_repasse DESC
    """
    resumo = pd.read_sql(query_plano, conn)
    print("\n--- 💰 RESUMO DE FATURAMENTO POR PLANO ---")
    print(resumo)
    
    conn.close()

if __name__ == "__main__":
    rodar_auditoria()