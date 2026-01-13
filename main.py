import pyautogui
import time
import pandas

# Sequência
# 1. Entrar no sistema/site ✅
# 2. Fazer login
# 3. Importar a base de dados
# 4. Cadastrar o primeiro produto
# 5. Cadastrar os demais produtos até não sobrar mais nenhum

# Entrar no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")