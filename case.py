from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as ucd
from openpyxl import load_workbook
from selenium.common.exceptions import TimeoutException
import time 

options = ucd.ChromeOptions()
options.add_argument("--user-data-dir=/home/guest/.config/google-chrome")  #Configuração para logar em um perfil no Chrome (exclusivamente nesse computador)
options.add_argument("--profile-directory=Profile 4")
navegador = ucd.Chrome(version_main=135, options=options)

wb = load_workbook("case.xlsx") #Carrega a planilha Excel

time.sleep(8)
navegador.get("https://www.google.com/") #Entra no site
barra_pesquisa = navegador.find_element(By.XPATH, '//*[@id="APjFqb"]') #Procura a barra de pesquisa
barra_pesquisa.send_keys("Cases de agentes de IA")
barra_pesquisa.send_keys(Keys.ENTER)

p = 1 #Páginas 
j = 3 #Linhas da planilha

navegador.set_page_load_timeout(10) #Tempo limite para carregamento
while j<=27:
    for i in range(0, 12): #i faz a varredura entre as páginas, para alternar de uma a outra
        if j > 27:
            break
        try:
            try:
                resultados = navegador.find_elements(By.XPATH, "//a[h3]") #Procura o elemento que padroniza o link de páginas
                resultados[i].click() #Clica no elemento e entra na página
                time.sleep(1)
                navegador.execute_script("window.stop();") #Para o carregamento da página
                titulo = navegador.title
                url = navegador.current_url
                navegador.back()
            except TimeoutException: #Caso o tempo limite exceda
                navegador.execute_script("window.stop();") 
                time.sleep(1)
                titulo = navegador.title
                url = navegador.current_url
                navegador.back()
                excel = wb.active
                excel[f'A{j}'] = titulo
                excel[f'B{j}'] = url
                j+=1
                continue

            excel = wb.active #Mantém ativa e podendo fazer alterações
            excel[f'A{j}'] = titulo #Salva os dados coletados na planilha
            excel[f'B{j}'] = url
            j+=1 
        except:
            continue
    if j <27:
        p += 1
        mudança_pag = navegador.find_element(By.CSS_SELECTOR, f'[aria-label="Page {p}"]') #Procura o elemento de troca de página
        mudança_pag.click() #Clica e troca de página
try:
    navegador.execute_script("alert('Automação concluída com sucesso')") #Pop-up
    time.sleep(3)
    alert = navegador.switch_to.alert
    alert.accept()
except:
    print("Erro ao exibir ou aceitar o alerta.")
finally:
    wb.save("case.xlsx") #Salva a planilha
    navegador.quit()