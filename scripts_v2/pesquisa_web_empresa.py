import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

 

def buscar_google(palavra):
    
    driver.get("https://www.google.com.br")

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(palavra) # digita na barra de pesquisa
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER) # executa a pesquisa
    driver.find_element(By.XPATH, '''//*[@id="hdtb-msb"]/div[1]/div/div[2]/a''').click() # clica no maps
    sleep(2)


def scroll_page(categoria):
    SCROLL_PAUSE_TIME = 1.2 # pause do scroll
    quant_scroll = 17
    count = 0
    tot = len(categorias)
    print(f"Page: {categoria}")

    print(f'{categorias.index(categoria)+1} --> {tot}')
    while True and count < quant_scroll:
        count +=1
        print(f"Scroll: {count} --> {quant_scroll}")
        driver.execute_script('''document.querySelector('div[class="m6QErb DxyBCb kA9KIf dS8AEf ecceSd"]').firstChild.scrollTo(0, document.querySelector('div[class="m6QErb DxyBCb kA9KIf dS8AEf ecceSd"]').firstChild.scrollHeight)''')
        sleep(SCROLL_PAUSE_TIME)
        

categorias = json.load(open("banco_dados/dados_brutos/categorias.json", 'r', encoding='utf8'))
for categoria in categorias:
    ancora = []
    empresa = []
    link = []
    try:
        buscar_google(categoria)
        scroll_page(categoria)
        page = driver.find_elements(By.CLASS_NAME, 'lI9IFe')
        for pa in page:
            ancora.append(pa.find_elements(By.TAG_NAME, 'a'))

        page[0].get_dom_attribute
        for an in ancora:
            link.append(an[0].get_dom_attribute('href'))
        

        for emp in range(len(page)):
            empresa.append(page[emp].text.split("\n")) 

        for pos in range(0, len(link)):
            empresa[pos].append(link[pos])      
        
        if categorias.index(categoria) != 0:
            ler = open('banco_dados/dados_brutos/empresas_bruto.json', 'r', encoding='utf-8')
            arquivo_r = json.load(ler)
            ler.close()
            arquivo = open('banco_dados/dados_brutos/empresas_bruto.json', 'w', encoding='utf-8')

            
            for comp_02 in empresa:
                if comp_02 in arquivo_r:
                    del(empresa[empresa.index(comp_02)])

            empresa.extend(arquivo_r)

        else:
            arquivo = open('banco_dados/dados_brutos/empresas_bruto.json', 'w', encoding='utf-8')

        json.dump(empresa, arquivo, indent=6, ensure_ascii=False)
        arquivo.close()

    except: 
        print("Deu não, vou para o proximo!")
 


    
print("----------------------------FIM--------------------------------")
