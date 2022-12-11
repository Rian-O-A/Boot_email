import json
from scripts_v2.aplicar_organizacao import empacotado
from scripts_v2.filter_email import filter_email

empacotado['emails'] = filter_email

arquivo = open('empacotado.json', 'w', encoding='utf-8')
json.dump(empacotado, arquivo, indent=6, ensure_ascii=False)
arquivo.close()