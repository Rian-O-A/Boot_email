import requests
import json

numPage = 1
url = "https://api.casadosdados.com.br/v2/public/cnpj/search"

# Cabeçalhos da requisição
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": "https://casadosdados.com.br",
    "Referer": "https://casadosdados.com.br/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# Dados a serem enviados no corpo da requisição (substitua pelos seus dados)
packetCNPJ = []
for x in range(1, numPage+1):
    print(x)
    data = {
        "query": {
            "termo": [],
            "atividade_principal": [],
            "natureza_juridica": [],
            "uf": [],
            "municipio": [],
            "bairro": [],
            "situacao_cadastral": "ATIVA",
            "cep": [],
            "ddd": [],
        },
        "range_query": {
            "data_abertura": {"lte": None, "gte": None},
            "capital_social": {"lte": None, "gte": None},
        },
        "extras": {
            "somente_mei": False,
            "excluir_mei": False,
            "com_email": False,
            "incluir_atividade_secundaria": False,
            "com_contato_telefonico": False,
            "somente_fixo": False,
            "somente_celular": False,
            "somente_matriz": False,
            "somente_filial": False,
        },
        "page": x,
    }

    # Faz a requisição POST
    response = requests.post(url, json=data, headers=headers)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converte a resposta para JSON e imprime
        json_response = response.json()
        packetCNPJ.extend(json_response["data"]["cnpj"])
        
        
    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        print(response.text)

print(len(packetCNPJ))
json.dump(packetCNPJ, open(f"packetCNPJ.json", 'w', encoding=("UTF-8")), indent=6, ensure_ascii=False)