# 📊 WeFitness Data Platform

Este repositório contém uma solução completa de **Engenharia de Analytics** desenvolvida para a gestão de dados de check-ins e repasses financeiros da rede **WeFitness**, uma rede de academias fictícias criada para gerar esse fluxo. O projeto simula o fluxo real de dados entre uma plataforma de benefícios e suas academias parceiras.

## 🎯 Objetivo do Projeto
O objetivo principal é transformar dados brutos e desestruturados em um **Data Warehouse otimizado**, permitindo que o time de operações realize análises precisas sobre faturamento, engajamento por plano e volumetria por modalidade.

---

## 🏗️ Estrutura do Pipeline
1.  **Ingestão:** Geração de dados sintéticos via Python.
2.  **ETL:** Limpeza, tratamento de duplicatas e modelagem Star Schema.
3.  **Data Quality:** Auditoria rigorosa de nulos e integridade.
4.  **Warehouse:** Armazenamento em SQLite e backup otimizado em Parquet.
5.  **Analytics:** Dashboard interativo para visualização de KPIs.

### 📂 Mapa do Projeto (Estrutura de Arquivos)
Para facilitar a navegação, aqui está o que cada arquivo faz no ecossistema:

* **`ingestao_wefitness.py`**: Script inicial que gera a massa de dados bruta.
* **`checkins_raw.json`**: O arquivo de dados brutos (Raw Data) gerado pela ingestão.
* **`etl_wefitness_star_schema.py`**: O coração do projeto. Transforma o JSON bruto em tabelas de Dimensão e Fato.
* **`auditoria_wefitness.py`**: Script de validação que garante "Zero Erros" no banco de dados.
* **`wefitness_warehouse.db`**: O Banco de Dados funcional (SQLite) onde os dados estão estruturados.
* **`sincronizar_warehouse.py`**: Utilitário que sincroniza o banco de dados com os formatos de backup.
* **`wefitness_fato_final.parquet`**: Backup da tabela fato em formato colunar de alta performance.
* **`fato_checkin_optimized.parquet`**: Versão otimizada e comprimida para análises de Big Data.
* **`dashboard_wefitness.py`**: Código da interface visual e interativa.
* **`README.md`**: Documentação técnica do projeto.

---

## 🛠️ Ferramentas Utilizadas
* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas
* **Banco de Dados:** SQLite (SQL)
* **Armazenamento de Performance:** Apache Parquet
* **Visualização:** Streamlit & Plotly

---

## 🚀 Como Rodar o Projeto
1.  **Clone o repositório** e instale as dependências (`pip install pandas streamlit plotly pyarrow`).
2.  **Siga a ordem de execução**:
    ```bash
    python ingestao_wefitness.py
    python etl_wefitness_star_schema.py
    python auditoria_wefitness.py
    streamlit run dashboard_wefitness.py
    ```

---

## ❓ FAQ - Perguntas Frequentes

**1. Por que utilizar o modelo Star Schema?** Para simplificar as consultas SQL e melhorar a performance. Ao separar entidades em dimensões, evitamos repetição de dados.

**2. Como foi garantida a qualidade dos dados?** Através do script `auditoria_wefitness.py` que verifica valores nulos e duplicidade, garantindo a integridade dos repasses financeiros.

**3. Por que gerar arquivos Parquet?** O Parquet é o padrão ouro para Big Data. Ele reduz o espaço em disco e permite que ferramentas de nuvem leiam os dados de forma muito mais rápida que um CSV ou JSON.

**4. O que o Ticket Médio de R$ 29,93 diz sobre o negócio?** Indica o valor médio que a rede recebe por cada treino. É uma métrica vital para calcular a sustentabilidade da parceria.

**5. Qual foi o maior desafio técnico?** Lidar com o efeito de duplicação de dados (fan-out) durante os joins, o que foi resolvido com travas de segurança no script de ETL.

**6. O projeto é escalável?** Sim. A lógica de ETL e a modelagem em Star Schema permitem que o projeto seja migrado para um ambiente de nuvem (como AWS ou BigQuery) com pouquíssimo esforço.

---
**Desenvolvedora:** Bia Abaaoud
