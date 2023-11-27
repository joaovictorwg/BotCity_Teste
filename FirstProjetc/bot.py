"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

from botcity.core import DesktopBot, Backend

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    app_path = "C:/Users/jvict/OneDrive/Documentos/Programas-Jogos/Teams_windows_x64.exe"
    bot.execute(app_path)
    bot.wait(15000)

    #Pesquisar por Perfil
    if not bot.find( "search_anchor", matching=0.97, waiting_time=10000):
        not_found("search_anchor")
    bot.click_relative(-784, 27)
    bot.paste("Danilo Ferreira")
    bot.enter()
    
    #Clicar Perfil
    if not bot.find( "perfil_anchor", matching=0.97, waiting_time=10000):
        not_found("perfil_anchor")
    bot.click_relative(149, 85)

    #Digitar Mensagem
    if not bot.find( "msg_anchor", matching=0.97, waiting_time=10000):
        not_found("msg_anchor")
    bot.click_relative(122, -25)
    bot.paste("Olá, essa é uma mensagem enviada por um Bot feito em Python pela BotCity.\nAqui está o link para o Repositório: https://github.com/joaovictorwg/BotCity_Teste")
    bot.enter()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()




