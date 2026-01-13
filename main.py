import pyautogui
import time
import pandas

# Sequência
# 1. Entrar no sistema/site ✅
# 2. Fazer login
# 3. Importar a base de dados
# 4. Cadastrar o primeiro produto
# 5. Cadastrar os demais produtos até não sobrar mais nenhum

pyautogui.PAUSE = 0.5

# Entrar no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Digitar o email
pyautogui.click(x=677, y=479)
pyautogui.write("pythontest@gmail.com")
pyautogui.press("tab")

# Digitar a senha:
pyautogui.write("senhaparateste")
pyautogui.press("tab")

# Clicar pora logar
pyautogui.press("enter")

# Importando base de dados
table = pandas.read_csv("produtos.csv")

for line in table:
    ...