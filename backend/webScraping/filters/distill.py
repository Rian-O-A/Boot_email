from backend.webScraping.scripts.empresasEmails import buscar_email

class DataFormatter:
    def __init__(self):
        self.listName = []

    def _format_data(self, item):
        formatted_data = {"Nome": item[0]}
        
        if len(item) == 3:
            formatted_data.update(self._format_contact_data(item[1], item[2]))

        elif len(item) == 4:
            formatted_data["Endereco"] = item[1]
            formatted_data.update(self._format_contact_data(item[2], item[3]))

        self.listName.append(formatted_data)

    def _format_contact_data(self, data1, data2):
        if '(' in data1:
            data1 = data1.replace("(", "").replace(")", "").replace("-", "").replace(' ', '')
            return {"Tel": data1, "Site": data2}
        elif data1.isdigit():
            return {"Tel": data1, "Site": data2}
        else:
            return {"Endereco": data1, "Site": data2}

    def process_data(self, dataList):
        for item in dataList:
            if len(item) in (3, 4) and item[-1] is not None:
                self._format_data(item)

        
        return buscar_email(self.listName)

                    
            
 