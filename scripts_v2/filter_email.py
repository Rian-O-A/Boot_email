import json, re
from scripts_v2.web_crawler_email import e_mails_brutos 

# def dados_email(arquivo):
#     with open(arquivo, 'r', encoding='utf8') as ar:
#         return json.load(ar)

emails = e_mails_brutos

filter_email = {}
for empresa in emails:
    for email in emails[empresa]:
        if re.search(r"[@]\d+[.]\d+[.]\d+|[@]\w+[-]\w+[.]wixpress|[@]\d+[.]\w|[@]sentry[.]\w+|[@]\w+[.]ingest[.]sentry|[@]\w+[-]\w[-]\w+[.][png]+|[@]\w+[-]\w+[.][png]+|[@]\w+[.][png]+|[@]\w+[.][jpg]+|[@]\w+[.]svg", email):
            continue
        else: 
            if empresa not in filter_email: 
                filter_email[empresa] = [email]
            else:
                filter_email[empresa].append(email)


arquivo = open('banco_dados/dados_filtrados/e_mail-final.json', 'w', encoding='utf8')
json.dump(filter_email, arquivo, indent= 6, ensure_ascii=False)
arquivo.close()