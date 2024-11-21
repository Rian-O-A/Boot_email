import requests
import re
import json
import logging


userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36"

def is_valid_email(email):
    # Use uma expressão regular para verificar um formato de e-mail básico
    return re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

def limpar_emails(empresa_email):
    empresas_filtradas = []
    
    for email in empresa_email:
        if  is_valid_email(email):
            empresas_filtradas.append(email)
    
    return empresas_filtradas


def buscar_email(organizado):
    logging.basicConfig(filename='email_extraction.log', level=logging.INFO)
    empresa_email = []

    for data in organizado:
        link = data.get("Site")
        nome = data.get("Nome")

        if link is not None and "https://www.google.com/maps/place/" not in link:
            try:
                response = requests.get(link, headers={"User-Agent": userAgent}, timeout=30)
                response.raise_for_status()

                html = response.text

                search = re.findall(r'[\w\-.]+@[\w\-]+\.\w+\.?\w*', html)

                if search:
                    data["emails"] = limpar_emails(list(set(search)))
                    
                else:
                    data["emails"] = []
                    logging.info(f"Sem e-mails encontrados para {nome}")
                    
                

            except requests.exceptions.RequestException as e:
                logging.error(f"Falha ao fazer a requisição para {link}: {str(e)}")
            except Exception as e:
                logging.error(f"Erro ao processar {nome}: {str(e)}")

        empresa_email.append(data)
    

        
    return empresa_email




