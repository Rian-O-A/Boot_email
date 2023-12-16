import json
from backend.webScraping.scripts.empresasMaps import pesquisarEmpresas
# from backend.webScraping.empresasEmails import startEmail
from backend.webScraping.filters.distill import DataFormatter
# from backend.fireBase.manager import Firestore

json.dump(DataFormatter().process_data(pesquisarEmpresas("Limpeza de automoveis vitoria", 17)), open("condominios.json", 'w', encoding="UTF-8"), indent=6, ensure_ascii=False)
# DataFormatter().process_data(pesquisarEmpresas("Empresa de fabricação de exportação em vitoria", 17))
# empresas = {}
# pesquisa = [
#       "Empresa de fabricação de plástico em vitoria",
#       "Empresa de fabricação de plástico em vila velha",
#       "Empresa de fabricação de plástico em guarapari"
#     ]

# for empresa in pesquisa:
#     try:
#          empresas[empresa] = DataFormatter().process_data(pesquisarEmpresas(empresa, 17))
#     except:
#             print("Não deu")
# Firestore.setPack(empresas)
