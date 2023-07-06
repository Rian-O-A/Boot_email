
class Distill:
    
    def nameList(dataList): # formatar 
        listName = []
        for item in dataList:
            nomear = {}
            if len(item) == 3:
                if item[-1] != None:
                    nomear["Nome"] = item[0]
                    if '(' in item[1]:
                        nomear["Tel"] = item[1].replace("(", "").replace(")", "").replace("-", "").replace(' ', '')
                    else:
                        nomear["Endereco"] = item[1]
                        
                    nomear["Site"] = item[2]
                    listName.append(nomear)

            elif len(item) == 4:
                nomear["Nome"] = item[0]
                nomear["Endereco"] = item[1]
                if '(' in item[2]:
                    nomear["Tel"] = item[2].replace("(", "").replace(")", "").replace("-", "").replace(' ', '')
                elif item[2].isdigit():
                    nomear["Tel"] = item[2]
                nomear["Site"] = item[3]
                listName.append(nomear)
            
        return listName
                    
                    
            
 