import pandas as pd
import random
import json
from datetime import datetime, timedelta

# Configurações iniciais
n_registros = 1500
academias_wefitness = [
    "WeFitness - Paulista", "WeFitness - Itaim", "WeFitness - Barra", 
    "WeFitness - Centro", "WeFitness - Savassi", "WeFitness - Beira Mar"
]
planos = ["Basic", "Silver", "Gold", "Platinum"]
categorias = ["Musculação", "Crossfit", "Natação", "Yoga", "Pilates"]

# Listas para gerar nomes fictícios mais realistas
nomes = ["Beatriz", "Gabriel", "Felipe", "Mariana", "Ricardo", "Larissa", "Thiago", "Camila", "Bruno", "Isabela"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes"]

data_inicial = datetime(2025, 1, 1)
registros = []

for i in range(n_registros):
    data_checkin = data_inicial + timedelta(
        days=random.randint(0, 30), 
        hours=random.randint(6, 22), 
        minutes=random.randint(0, 59)
    )
    
    # Gera um nome completo aleatório
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    
    checkin = {
        "id_transacao": f"TRX-{1000 + i}",
        "usuario_id": random.randint(5000, 5500),
        "nome_usuario": nome_completo,  # <--- Nomes agora são realistas!
        "plano_usuario": random.choice(planos),
        "unidade_wefitness": random.choice(academias_wefitness),
        "categoria_servico": random.choice(categorias),
        "data_hora": data_checkin.strftime("%Y-%m-%d %H:%M:%S"),
        "valor_repasse": round(random.uniform(15.0, 45.0), 2)
    }
    registros.append(checkin)

with open('checkins_raw.json', 'w', encoding='utf-8') as f:
    json.dump(registros, f, indent=4, ensure_ascii=False)

print(f"✅ Sucesso! 'checkins_raw.json' gerado com nomes reais e {n_registros} linhas.")