import requests
from bs4 import BeautifulSoup
import time
import random

def buscar_preco_mercado_livre(item):
    url = f"https://lista.mercadolivre.com.br/{item.replace(' ', '-')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        preco = soup.select_one(".andes-money-amount__fraction")
        if preco:
            return float(preco.text.strip().replace(".", ""))
    except Exception as e:
        print(f"Erro no Mercado Livre ({item}): {e}")
    return None

def buscar_precos_em_sites(item):

    time.sleep(random.uniform(1.0, 2.5))
    
    resultados = []

    for nome, func in [
        ("Mercado Livre", buscar_preco_mercado_livre)
    ]:
        preco = func(item)
        if preco:
            resultados.append((nome, preco))

    return resultados

