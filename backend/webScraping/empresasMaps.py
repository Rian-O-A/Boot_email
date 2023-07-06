from backend.webScraping import driver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def pesquisarEmpresas(search, scroll):
    driver.get("https://www.google.com.br")
    campo_pesquisa = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
    campo_pesquisa.send_keys(search)
    campo_pesquisa.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[5]/div/div/div[1]/div[1]/div/a[1]").click()

    # Aguarde até que o elemento do painel lateral seja encontrado
    panel_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]"))
    )




    for i in range(scroll):
        panel_element.send_keys(Keys.END)
        sleep(0.5)
        

    elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'Nv2PK')]")


    print(f"Empresas encontradas ==> {len(elements)}")
    empresas = []
    for pos in elements:
        formatado = pos.text.split("\n")
        link = pos.find_elements(By.TAG_NAME, 'a')[-1].get_attribute('href')    
        del formatado[1]
        formatado = [item.strip() for item in formatado if item not in ['Rotas', 'Website']]
        formatado = [ item.split("·")[-1] if '·' in item else item for item in formatado]
        formatado = [ item.strip() for item in formatado if formatado.index(item) < 3 ]
        formatado = list(filter(None, formatado))
        formatado.append(None if 'https://www.google.com.br/maps' in link else link)
        
        empresas.append(formatado)
        
    return empresas
    
