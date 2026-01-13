import pyautogui
import time
import pandas

# Sequência
# 1. Entrar no sistema/site ✅
# 2. Fazer login ✅
# 3. Importar a base de dados ✅
# 4. Cadastrar o primeiro produto ✅
# 5. Cadastrar os demais produtos até não sobrar mais nenhum ✅

pyautogui.PAUSE = 0.3

# Entrar no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Digitar o email
pyautogui.click(x=677, y=479)
pyautogui.write("pythontest@gmail.com")
pyautogui.press("tab")

# Digitar a senha:
pyautogui.write("senhaparateste")
pyautogui.press("tab")

# Clicar pora logar
pyautogui.press("enter")
time.sleep(1)

# Importando base de dados
table = pandas.read_csv("produtos.csv")

for line in table.index:
    pyautogui.click(x=924, y=330)    
    # código do produto
    codigo = table.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = table.loc[line, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = table.loc[line, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = table.loc[line, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preço
    preco = table.loc[line, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = table.loc[line, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    observation = table.loc[line, "obs"]
    if str(observation) != "nan":
        pyautogui.write(str(observation))
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")

    pyautogui.scroll(5000)