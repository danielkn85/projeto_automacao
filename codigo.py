# Passo a passo do projeto

import pyautogui 
import time

pyautogui.PAUSE = 0.5  # para dar 0.5 segundo entre os comandos, para dar tempo para o sistema trabalhar

# 1. Abrir o sistema da empresa
    # a. abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey('alt','space','x') # atalho para maximizar a janela

    # b. entrar no site da empresa

pyautogui.click(x=242, y=79)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  
pyautogui.press("enter")  
time.sleep(3) # para dar um tempo (3 segundos) para o site carregar

# 2. Fazer o Login

# pyautogui.click(x=627, y=534)
pyautogui.press("tab")
pyautogui.write("email@teste.com")
pyautogui.press("tab")
pyautogui.write("AUHIUHDaiudia")
pyautogui.press("tab")
pyautogui.press("enter")

# 3. Importar a base de dados de produtos

import pandas as pd

tabela =  pd.read_csv("produtos.csv")

# 4. Cadastrar um produto

    # a. Clicar no primeiro campo
    
# pyautogui.click(x=677, y=365)  

    # b. Cadastrar um produto

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    categoria = str(tabela.loc[linha, "categoria"]) # Como "Categoria" é um VALOR NUMÉRICO, é necessario transformar em str
    # É possível transformar todas as variáveis em str por padrão    
    pyautogui.click(x=677, y=365)                                         
    pyautogui.write(codigo) # Código do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.write(tabela.loc[linha, "marca"]) # Marca do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"])) # Tipo do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.write(categoria) # Categoria do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # Preço Unitário do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"])) # Custo do Produto
    pyautogui.press("tab") # Passa para o próximo campo
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)    
    pyautogui.press("tab") # Passa para o próximo campo
    pyautogui.press("enter") # Botão enviar
    time.sleep(1)
    pyautogui.press("home") # Rolar para o topo da página

# c. Passar pra o próximo campo
# d. Repetir até finalizar o processo

# 5. Repetir até terminar a lista de produtos

