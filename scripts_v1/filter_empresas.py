import json
from collections import Counter

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

dados = ler_json('banco_dados/dados_brutos/jsonfiltrado.json')

dados_filter = []
for pos in range(len(dados)):
        for pos_02 in range(len(dados[pos][0])):
                if len(dados[pos][0]) == 7:
                        if pos_02 == 0:
                                info_01 = dados[pos][0][pos_02].split()
                                del info_01[-1]
                                info_01 = ' '.join(info_01)
                                dados_filter.append([info_01])
                        elif pos_02 == 4:
                                if len(dados[pos][0][pos_02]) != 0:
                                        info_01 = dados[pos][0][pos_02].split(" ")
                                        dados_filter[-1].append(info_01[0]+info_01[1])
                                        dados_filter[-1].append(dados[pos][1])
                        elif pos_02 != 0 and pos_02 != 4 and pos_02 != 5 and pos_02 != 6:
                                info_01 = dados[pos][0][pos_02].strip()
                                dados_filter[-1].append(info_01)

                if len(dados[pos][0]) == 6:
                        if pos_02 == 0:
                                info_01 = dados[pos][0][pos_02].split()
                                del info_01[-1]
                                info_01 = ' '.join(info_01)
                                dados_filter.append([info_01])
                        elif pos_02 == 4:
                                if len(dados[pos][0][pos_02]) != 0:
                                        info_01 = dados[pos][0][pos_02].split(" ")
                                        dados_filter[-1].append(info_01[0]+info_01[1])
                                        dados_filter[-1].append(dados[pos][1])
                        elif pos_02 != 0 and pos_02 != 4 and pos_02 != 5:
                                info_01 = dados[pos][0][pos_02].strip()
                                dados_filter[-1].append(info_01)



                if len(dados[pos][0]) == 5:
                        if pos_02 == 0:
                                info_01 = dados[pos][0][pos_02].split()
                                del info_01[-1]
                                info_01 = ' '.join(info_01)
                                dados_filter.append([info_01])
                        elif pos_02 == 4:
                                if len(dados[pos][0][pos_02]) != 0:
                                        info_01 = dados[pos][0][pos_02].split(" ")
                                        dados_filter[-1].append(info_01[0]+info_01[1])
                                        dados_filter[-1].append(dados[pos][1])
                        elif pos_02 != 0 and pos_02 != 4:
                                info_01 = dados[pos][0][pos_02].strip()
                                dados_filter[-1].append(info_01)

                        

                elif len(dados[pos][0]) == 4:
                        if pos_02 == 0:
                                info_01 = dados[pos][0][pos_02].split()
                                del info_01[-1]
                                info_01 = ' '.join(info_01)
                                dados_filter.append([info_01])
                        elif pos_02 == 3:
                                if len(dados[pos][0][pos_02]) != 0:
                                        info_01 = dados[pos][0][pos_02].split(" ")
                                        dados_filter[-1].append(info_01[0]+info_01[1])
                                        dados_filter[-1].append(dados[pos][1])
                                
                        elif pos_02 != 0 and pos_02 != 4:
                                info_01 = dados[pos][0][pos_02].strip()
                                dados_filter[-1].append(info_01) 

                

                elif len(dados[pos][0]) == 3:
                        if pos_02 == 0:
                                info_01 = dados[pos][0][pos_02].split()
                                del info_01[-1]
                                info_01 = ' '.join(info_01)
                                dados_filter.append([info_01])                       
                        elif pos_02 != 0:
                                info_01 = dados[pos][0][pos_02].strip()
                                dados_filter[-1].append(info_01) 
                                if pos_02 == 2:
                                        dados_filter[-1].append(dados[pos][1])

                        
dados_tratados = []
for pos_t in range(len(dados_filter)):
        for pos_t2 in range(len(dados_filter[pos_t])):
                if len(dados_filter[pos_t]) == 7:
                        if pos_t2 == 0:
                                cortado = dados_filter[pos_t][pos_t2].split(" ") 
                                if 'Nenhuma' in dados_filter[pos_t][pos_t2]: 
                                        del cortado[-1]
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado]) 
                                else:
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado])
                        
                        elif pos_t2 != 0:
                                dados_tratados[-1].append(dados_filter[pos_t][pos_t2])


                elif len(dados_filter[pos_t]) == 6:
                        if pos_t2 == 0:
                                cortado = dados_filter[pos_t][pos_t2].split(" ") 
                                if 'Nenhuma' in dados_filter[pos_t][pos_t2]: 
                                        del cortado[-1]
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado]) 
                                else:
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado])

                        if pos_t2 == 3:
                                if '\"' in dados_filter[pos_t][pos_t2]:
                                        cortado = dados_filter[pos_t][pos_t2].split('\"')
                                        del cortado[-1]
                                        del cortado[-1]
                                        cortado = cortado[0]
                                        cortado = cortado.strip().split(" ")
                                        del cortado[-1]
                                        cortado = ''.join(cortado)
                                        dados_tratados[-1].append(cortado)
                                else:
                                        dados_tratados[-1].append(dados_filter[pos_t][pos_t2])
                        
                        elif pos_t2 != 3 and pos_t2 != 0:
                                dados_tratados[-1].append(dados_filter[pos_t][pos_t2])

                elif len(dados_filter[pos_t]) == 5:
                        if pos_t2 == 0:
                                cortado = dados_filter[pos_t][pos_t2].split(" ") 
                                if 'Nenhuma' in dados_filter[pos_t][pos_t2]: 
                                        del cortado[-1]
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado]) 
                                else:
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado])

                        elif pos_t2 == 2:
                                if '\"' in dados_filter[pos_t][pos_t2]:
                                        cortado = dados_filter[pos_t][pos_t2].split('\"')
                                        del cortado[-1]
                                        del cortado[-1]
                                        cortado = cortado[0]
                                        cortado = cortado.strip().split(" ")
                                        del cortado[-1]
                                        cortado = ''.join(cortado)
                                        dados_tratados[-1].append(cortado)
                                else:
                                        dados_tratados[-1].append(dados_filter[pos_t][pos_t2])

                        elif pos_t2 == 3:
                                cortado = dados_filter[pos_t][pos_t2].split('\"')
                                if len(cortado) > 1:
                                        del cortado[-1]
                                        dados_tratados[-1].append(cortado[0])
                                else:
                                        dados_tratados[-1].append(cortado[0])
                        
                        elif pos_t2 != 0 and pos_t2 != 3 and pos_t2 != 2:
                                dados_tratados[-1].append(dados_filter[pos_t][pos_t2])

                elif len(dados_filter[pos_t]) == 4:
                        if pos_t2 == 0:
                                cortado = dados_filter[pos_t][pos_t2].split(" ") 
                                if 'Nenhuma' in dados_filter[pos_t][pos_t2]: 
                                        del cortado[-1]
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado]) 
                                else:
                                        cortado = ' '.join(cortado)
                                        dados_tratados.append([cortado])

                        elif pos_t2 == 2:
                                if 'Rotas' in dados_filter[pos_t][pos_t2]:
                                        cortado = dados_filter[pos_t][pos_t2].split(' ')
                                        del cortado[-1]
                                        cortado = ' '.join(cortado)
                                        dados_tratados[-1].append(cortado)
                                else:
                                        dados_tratados[-1].append(dados_filter[pos_t][pos_t2])
                        
                        elif pos_t2 != 0 and pos_t2 != 2:
                                dados_tratados[-1].append(dados_filter[pos_t][pos_t2])


dados_tratados_02 = {}
nome_completo = []
for p1 in range(len(dados_tratados)):
        for p2 in range(len(dados_tratados[p1])):
                if dados_tratados[p1][p2] != "":
                        if len(dados_tratados[p1]) == 6:
                                if p2 == 0:
                                        if len(dados_tratados[p1][p2]) <= 30:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2]}
                                        else:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2][:30]+"..."}
                                                nome_completo.append([dados_tratados[p1][p2][:30]+"...", [dados_tratados[p1][p2]]])
                                
                                elif p2 == 1:
                                        dados_tratados_02["empresa-"+str(p1+1)]["classe"] = dados_tratados[p1][p2]
                                elif p2 == 2:
                                        dados_tratados_02["empresa-"+str(p1+1)]["endereco"] = dados_tratados[p1][p2]
                                elif p2 == 3:
                                        if '(' in dados_tratados[p1][p2]:
                                                dados_tratados_02["empresa-"+str(p1+1)]["contato"] = dados_tratados[p1][p2]
                                        else:
                                                dados_tratados_02["empresa-"+str(p1+1)]["horario"] = dados_tratados[p1][p2]
                                elif p2 == 4:
                                        dados_tratados_02["empresa-"+str(p1+1)]["contato"] = dados_tratados[p1][p2]
                                elif p2 == 5:
                                        dados_tratados_02["empresa-"+str(p1+1)]["site"] = dados_tratados[p1][p2]

                        elif len(dados_tratados[p1]) == 5:
                                if p2 == 0:
                                        if len(dados_tratados[p1][p2]) <= 30:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2]}
                                        else:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2][:30]+"..."}
                                                nome_completo.append([dados_tratados[p1][p2][:30]+"...", [dados_tratados[p1][p2]]])
                                
                                elif p2 == 1:
                                        dados_tratados_02["empresa-"+str(p1+1)]["classe"] = dados_tratados[p1][p2]
                                elif p2 == 2:
                                        dados_tratados_02["empresa-"+str(p1+1)]["endereco"] = dados_tratados[p1][p2]
                                elif p2 == 3:
                                        dados_tratados_02["empresa-"+str(p1+1)]["contato"] = dados_tratados[p1][p2]
                                elif p2 == 4:
                                        dados_tratados_02["empresa-"+str(p1+1)]["site"] = dados_tratados[p1][p2]

                        elif len(dados_tratados[p1]) == 4:
                                if p2 == 0:
                                        if len(dados_tratados[p1][p2]) <= 30:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2]}
                                        else:
                                                dados_tratados_02["empresa-"+str(p1+1)] = {"nome":dados_tratados[p1][p2][:30]+"..."}
                                                nome_completo.append([dados_tratados[p1][p2][:30]+"...", [dados_tratados[p1][p2]]])
                                
                                elif p2 == 1:
                                        dados_tratados_02["empresa-"+str(p1+1)]["classe"] = dados_tratados[p1][p2]
                                elif p2 == 2:
                                        if '(' in dados_tratados[p1][p2]:
                                                dados_tratados_02["empresa-"+str(p1+1)]["contato"] = dados_tratados[p1][p2]
                                        else:
                                                dados_tratados_02["empresa-"+str(p1+1)]["endereco"] = dados_tratados[p1][p2]
                                        
                                elif p2 == 3:
                                        dados_tratados_02["empresa-"+str(p1+1)]["site"] = dados_tratados[p1][p2]


# empacotado = {"informacao": dados_tratados_02, "buscar":nome_completo}

# arquivo = open('banco_dados/dados_filtrados.json', 'w', encoding='utf8')

# json.dump(empacotado, arquivo, indent= 6, ensure_ascii=False)

# arquivo.close()
