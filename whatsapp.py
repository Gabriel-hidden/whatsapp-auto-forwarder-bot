# Importar bibliotecas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from pyperclip import copy
from time import sleep

# Verificar a necessidade de instalar o chromedriver
servico = Service(ChromeDriverManager().install())

# Criar um navegador
navegador = webdriver.Chrome(service=servico)

# Abrir o WhatsApp Web
navegador.get('https://web.whatsapp.com/')

# Esperar 5 minutos até que o login seja feito
try:
    WebDriverWait(navegador, 300).until(
        EC.presence_of_all_elements_located((By.ID, 'side'))
    )
except:
    navegador.quit()

mensagem = "Olá! 👋 Esta é uma mensagem de teste para verificar a funcionalidade do bot. Se precisar de ajuda ou tiver alguma pergunta, sinta-se à vontade para perguntar!"

contatos = ['Meu Número', 'Contato 1', 'Contato 2', 'Contato 3', 'Contato 4', 'Contato 5', 'Contato 6', 'Contato 7']

# Tratar mensagem (remover emojis e espaços vazios)
_mensagem = []
for letra in mensagem:
    if letra.isalnum():
        _mensagem.append(letra)

_mensagem = ''.join(_mensagem)

# Clicar na lupa de pesquisa
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
sleep(1.5)

# Limpar campo de busca
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').clear()
sleep(1.5)

# Escrever (Meu número)
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(contatos[0])
sleep(1.5)

# Esperar o contato ser encontrado
try:
    lista_elementos = WebDriverWait(navegador, 300).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'matched-text'))
    )
except:
    navegador.quit()

for elemento in lista_elementos:
    if contatos[0] == elemento.text:
        break
else:
    print('Contato não encontrado!')
    navegador.quit()

# Entrar na conversa
navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/2/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
sleep(1.5)

# Limpar campo de busca da conversa
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').clear()
sleep(1.5)

# Copiar a mensagem para a área de transferência
copy(mensagem)

# Escrever a mensagem
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + 'v')
sleep(1.5)

# Enviar a mensagem
navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
sleep(1.5)

x = 1
y = 6
contador = 1

while contador < len(contatos) - 1:
    if x > 1:
        # Clicar na lupa de pesquisa
        navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
        sleep(1.5)

        # Limpar campo de busca
        navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').clear()
        sleep(1.5)

        # Escrever (Meu número)
        navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(contatos[0])
        sleep(1.5)

        # Esperar o contato ser encontrado
        try:
            lista_elementos = WebDriverWait(navegador, 300).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'matched-text'))
            )
        except:
            navegador.quit()

        for elemento in lista_elementos:
            if contatos[0] == elemento.text:
                break
        else:
            print('Contato não encontrado!')
            navegador.quit()

        # Entrar na conversa
        navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(1.5)

        # Limpar campo de busca da conversa
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').clear()
        sleep(1.5)

    # Encontrar a caixa correspondente a mensagem
    itens = navegador.find_elements(By.CLASS_NAME, 'UzMP7')
    for item in itens:
        elemento = item
        _mensagem_wpp = []

        for item in item.text.replace(' ', ''):
            if item.isalnum():
                _mensagem_wpp.append(item)

        if ''.join(_mensagem_wpp)[:-4] == _mensagem:
            break

    # Mover para a caixa correspondente
    ActionChains(navegador).move_to_element(elemento).perform()
    sleep(1.5)

    # Clicar na seta de opções
    navegador.find_element(By.CLASS_NAME, '_3u9t-').click()
    sleep(1.5)

    # Botão de encaminhar
    navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    sleep(1.5)
    navegador.find_element(By.XPATH, '//*[@id="main"]/span[2]/div/button[4]/span').click()
    sleep(1.5)

    for contato in contatos[x:y]:
        contador += 1

        # Escrever contato
        navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(contato)
        sleep(1.5)

        # Selecionar contato
        navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(1.5)

        # Limpar caixa de pesquisa
        navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').clear()
        sleep(1.5)

    # Enviar mensagem
    navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div').send_keys(Keys.ENTER)
    sleep(1.5)

    x += y
    y += 6

    if y > len(contatos):
        y = len(contatos) + 1
