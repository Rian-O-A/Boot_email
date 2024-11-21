from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo sem interface gráfica
chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU
chrome_options.add_argument("--no-sandbox")  # Desabilitar sandbox (opcional)
chrome_options.add_argument("--disable-dev-shm-usage")  # Evitar problemas em containers

    # Inicializa o driver usando o webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

