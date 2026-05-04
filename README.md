# 🎬 CineDash

![Python](https://img.shields.io/badge/Python-Data%20Pipeline-blue)
![API](https://img.shields.io/badge/API-TMDB-green)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Integration-success)
![Dashboard](https://img.shields.io/badge/Dashboard-Looker%20Studio-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

##  --> Sobre o Projeto

Pipeline de dados completo desenvolvido em Python para extração, transformação e disponibilização de dados de filmes utilizando a API do TMDB.

O projeto coleta informações detalhadas de filmes populares, trata os dados e os disponibiliza para análise em um dashboard interativo.

---

## --> Dashboard

👉 Acesse o dashboard interativo:  
https://datastudio.google.com/reporting/c259ca58-1c22-422f-bdfb-5baeea6b945f

---

## --> Tecnologias Utilizadas

- Python (requests, pandas)
- SQLite
- Google Sheets API (gspread)
- Looker Studio (Data Studio)
- HTML + CSS

---

## --> Pipeline de Dados

### 1️⃣ Extração (API TMDB)
- Coleta filmes populares
- Busca detalhes individuais
- Obtém:
  - Diretor
  - Elenco
  - Roteiristas
  - Gêneros
  - Receita e orçamento

---

### 2️⃣ Transformação
- Limpeza de dados
- Remoção de duplicidades
- Tratamento de valores nulos
- Normalização de gêneros (explode)

---

### 3️⃣ Armazenamento
- CSV (`filmes_tmdb.csv`)
- Banco SQLite (`filmes.db`)

---

### 4️⃣ Integração
- Envio automático para Google Sheets
- Criação de aba analítica para gêneros

---

### 5️⃣ Visualização
- Dashboard interativo no Looker Studio
- Interface HTML simulando uma “sala de cinema”

---

## --> Estrutura dos Dados

Principais campos coletados:

- ID do filme
- Título
- Data de lançamento
- Nota média
- Popularidade
- Gêneros
- Orçamento
- Receita
- Diretor
- Roteiristas
- Elenco principal

---

## --> Interface do Dashboard

O projeto inclui uma página HTML personalizada que simula uma tela de cinema para exibição do dashboard.

Características:
- 🎬 Tema cinematográfico  
- 🎭 Elementos visuais (cortinas, iluminação)  
- 📺 Dashboard incorporado via iframe  
- 📱 Layout responsivo  

---

## --> Como Executar


```bash
1. Clone o repositório

git clone https://github.com/juancavalcanti1609-sketch/ProjetoDashCinema.git
cd ProjetoDashCinema

2. Instale as dependências
pip install -r requirements.txt

3. Configure suas credenciais
API Key do TMDB
Arquivo credentials.json do Google Sheets

## --> Benefícios do Projeto
🔄 Pipeline completo (ETL)
🌐 Integração com múltiplas fontes
📊 Pronto para análise em BI
🧠 Estruturação de dados para insights
🎯 Projeto end-to-end

## --> Observações
A API Key não está incluída por segurança
O projeto utiliza delay entre requisições para evitar bloqueios
Pode haver limite de requisições da API
