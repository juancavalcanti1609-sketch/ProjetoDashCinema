import requests
import pandas as pd
import sqlite3
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


API_KEY = "vou tirar a api por segurança, sla vai que kkkk"
SHEET_URL = "link da planilha"


# Extraindo dados da TMBD (lembrar de puxar poucas páginas)

def buscar_filmes(paginas=10):
    filmes_lista = []

    for page in range(1, paginas + 1):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=pt-BR&page={page}"
        
        response = requests.get(url)
        data = response.json()

        for filme in data["results"]:
            movie_id = filme["id"]

            # detalhes
            detalhes_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=pt-BR"
            detalhes = requests.get(detalhes_url).json()

            # diretor, elenco, roteirista
            credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=pt-BR"
            credits = requests.get(credits_url).json()

            # gêneros
            generos = ", ".join([g["name"] for g in detalhes.get("genres", [])])

            # cartaz
            poster_path = filme.get("poster_path")
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

            # diretor
            diretor = None
            roteiristas = []

            for person in credits.get("crew", []):
                if person["job"] == "Director":
                    diretor = person["name"]

                if person["job"] in ["Screenplay", "Writer"]:
                    roteiristas.append(person["name"])

            # elenco principal (apenas 5 para testes)
            elenco = [a["name"] for a in credits.get("cast", [])[:5]]

            filmes_lista.append({
                "id": movie_id,
                "titulo": filme.get("title"),
                "data_lancamento": filme.get("release_date"),
                "nota": filme.get("vote_average"),
                "popularidade": filme.get("popularity"),
                "generos": generos,
                "orcamento": detalhes.get("budget"),
                "receita": detalhes.get("revenue"),
                "poster_url": poster_url,
                "diretor": diretor,
                "roteiristas": ", ".join(roteiristas),
                "elenco_principal": ", ".join(elenco)
            })

            time.sleep(0.3)

        print(f"Página {page} carregada")

    df = pd.DataFrame(filmes_lista)
    df = df.drop_duplicates(subset="id")

    return df



# Conexão com o bd

def salvar_banco(df):
    conn = sqlite3.connect("filmes.db")
    df.to_sql("filmes", conn, if_exists="replace", index=False)
    conn.close()
    print("Banco atualizado!")


# Separar todos os generos para analise detalhada

def tratar_generos(df):
    df_generos = df.copy()
    df_generos["generos"] = df_generos["generos"].str.split(", ")
    df_generos = df_generos.explode("generos")
    return df_generos



# Envio para planilha (CÓDIGO CORRIGIDO)

def enviar_sheets(df, df_generos):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(SHEET_URL)

    # aba principal
    sheet_filmes = spreadsheet.sheet1

    # aba gêneros
    try:
        sheet_generos = spreadsheet.worksheet("filmes_generos")
    except:
        sheet_generos = spreadsheet.add_worksheet(
            title="filmes_generos",
            rows="2000",
            cols="20"
        )


    df_clean = df.fillna("")
    df_clean = df_clean.replace([float("inf"), float("-inf")], "")
    
    df_generos_clean = df_generos.fillna("")
    df_generos_clean = df_generos_clean.replace([float("inf"), float("-inf")], "")

    # limpa e envia filmes
    sheet_filmes.clear()
    sheet_filmes.update([df_clean.columns.values.tolist()] + df_clean.values.tolist())

    # limpa e envia gêneros
    sheet_generos.clear()
    sheet_generos.update([df_generos_clean.columns.values.tolist()] + df_generos_clean.values.tolist())

    print("Dados enviados para o Google Sheets!")



# EXECUÇÃO

df = buscar_filmes(paginas=10)

df.to_csv("filmes_tmdb.csv", index=False, encoding="utf-8-sig")

salvar_banco(df)

df_generos = tratar_generos(df)

enviar_sheets(df, df_generos)

print("PIPELINE FINALIZADO ")
