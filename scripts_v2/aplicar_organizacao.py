import json, uuid
from scripts_v2.pesquisa_web_empresa import empresa


organizado = []
nome_comp = {}
empacotado = {}
empresas_brutos =  empresa


def comp(Uuid, conteudo, pos_v2):
        if pos_v2 == 0:
            if len(conteudo) > 30:
                organizado.append({'nome': conteudo[:30]+'...', 'Uuid': Uuid})
                nome_comp[conteudo[:30]+'...'] = conteudo

            else:
                organizado.append({'nome': conteudo, 'Uuid': Uuid})

        elif pos_v2 == 2:
            conteudo = conteudo.split('·')
            organizado[-1]['classe'] = conteudo[0].strip()
            organizado[-1]['endereco'] = conteudo[-1].strip()

        elif pos_v2 == 3:
            if '(' in conteudo:
                if 'Aberto' in conteudo or 'Fechado' in conteudo or 'Abre' in conteudo:
                    dividido = conteudo.split("·")
                    dividido = dividido[-1].strip()
                    if 'Aberto' not in dividido or 'Fechado' not in dividido or 'Abre' not in dividido:
                        organizado[-1]['contato'] = dividido
                    else:
                        organizado[-1]['contato'] = None
                elif '(' in conteudo:
                    organizado[-1]['contato'] = conteudo

            else:
                        organizado[-1]['contato'] = None
        




for pos in range(len(empresas_brutos)):
    Uuid = str(uuid.uuid4())
    for pos_v2 in range(len(empresas_brutos[pos])):
        conteudo = empresas_brutos[pos][pos_v2]
        if len(empresas_brutos[pos]) == 7:
            comp(Uuid=Uuid, conteudo=conteudo, pos_v2=pos_v2)
            if pos_v2 == 6:
                organizado[-1]['site'] = conteudo

        elif len(empresas_brutos[pos]) == 6:
            comp(Uuid=Uuid, conteudo=conteudo, pos_v2=pos_v2)
            if pos_v2 == 5:
                organizado[-1]['site'] = conteudo

        elif len(empresas_brutos[pos]) == 5:
            comp(Uuid=Uuid, conteudo=conteudo, pos_v2=pos_v2)
            if pos_v2 == 4:
                organizado[-1]['site'] = conteudo



empacotado['empresas'] = organizado
empacotado['buscar_nome'] = nome_comp

arquivo = open('banco_dados/dados_filtrados/empresas_filtrados.json', 'w', encoding='utf-8')
json.dump(empacotado, arquivo, indent=6, ensure_ascii=False)