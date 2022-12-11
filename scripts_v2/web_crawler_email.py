from scripts_v2.aplicar_organizacao import organizado
import requests, re, json


rota = {}
check = []
empresa_email = {}
for teste in organizado:
    if organizado[teste]["site"] != None:
        rota[organizado[teste]["nome"]] = organizado[teste]["site"]
  

def buscar_email():

    cont = 0
    total = len(rota)
#     headers = {
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
# "Accept-Encoding": "gzip, deflate", 
# "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
# "Dnt": "1", 
# "Host": "httpbin.org", 
# "Upgrade-Insecure-Requests": "1", 
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
# }
 
    for nome in rota:
        cont += 1
        link = rota[nome]
        print(f"{link} --> {cont} --> {total}")
        try:
            r = requests.get(link, timeout=30)
            print("Request: OK")
            html = r.text.encode("utf8")
            print("Html: ok")

            
            search = re.findall(r'[\w\-.]+@[\w\-]+\.\w+\.?\w*', html.decode("utf8"))
            print("Analise: OK")

            check = []
            if len(search) != 0:
                for e_mail in search:
                    
                    if e_mail not in check:
                        check.append(e_mail)
                        print("Email adcionado a lista: ok")
                
                empresa_email[nome] = check

            else:
                print("Sem email!")
                
        except:
            print("Deu não, veado!")

    return empresa_email

e_mails_brutos = buscar_email() 
arquivo_01 =  open('banco_dados/dados_brutos/e_mail_bruto.json', 'w',  encoding='utf8')
json.dump(e_mails_brutos, arquivo_01, indent= 6, ensure_ascii=False)   
