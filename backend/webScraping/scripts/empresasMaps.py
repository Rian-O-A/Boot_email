from backend.webScraping import driver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def pesquisarEmpresas(search, max_scroll):
    driver.get("https://www.google.com/maps/")
    campo_pesquisa = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#searchboxinput')))
    campo_pesquisa.send_keys(search)
    campo_pesquisa.send_keys(Keys.ENTER)

    # driver.find_element(By.XPATH, "/html/body/div[6]/div/div[5]/div/div/div[1]/div[1]/div/a[1]").click()

    # Aguarde até que o elemento do painel lateral seja encontrado
    panel_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd"))
    )

    for _ in range(max_scroll):
        # Guarde o tamanho atual da página
        page_size = driver.execute_script("return document.body.scrollHeight")

        # Role até o final da página
        panel_element.send_keys(Keys.END)
        
        # Aguarde um curto período de tempo
        sleep(2)
        

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
    
