import json
from backend.webScraping.empresasMaps import pesquisarEmpresas
from backend.webScraping.filters.distill import Distill
from backend.fireBase import Firestore
# json.dump(pesquisarEmpresas("empressas em vitoria", 17), open("arquivoB.json", 'w', encoding="UTF-8"), indent=6, ensure_ascii=False)

empresas = {}
pesquisa = [
      "Empresa de fabricação de plástico em vitoria",
      "Empresa de fabricação de plástico em vila velha",
      "Empresa de fabricação de plástico em guarapari"
    ]

for empresa in pesquisa:
    empresas[empresa] = Distill.nameList(pesquisarEmpresas(empresa, 17))
    
Firestore.setPack(empresas)
