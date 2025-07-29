from telegram.ext import ApplicationBuilder # Build principal do bot
from dotenv import load_dotenv # Carregar .env
import os
from handlers import start_handler, add_handler, list_handler, remove_handler, clear_handler # Comandos 
from database import init_db 

# Carrega as variáveis do arquivo .env
load_dotenv()
token = str(os.getenv("TELEGRAM_TOKEN"))

if not token: # Caso não exista
    raise ValueError("❌ A variável TELEGRAM_TOKEN não está definida no arquivo .env.")
else:
    print("✅ Token carrregado")

# Cria e inicia o bot
def main():
    
    init_db()
    print("✅ Banco de dados integrado")

    app = ApplicationBuilder().token(token).build() # Build do app, informando o token
    print("✅ Build do bot iniciado")

    app.add_handler(start_handler) # Comando /start
    app.add_handler(add_handler) # Comando /add
    app.add_handler(list_handler) # Comando /list
    app.add_handler(remove_handler) # Comando /remove
    app.add_handler(clear_handler) # Comando /clear
    print("✅ Comandos ativos")

    os.system("cls")
    print("✅ Bot iniciado com sucesso. Rodando no momento...")
    
    app.run_polling()

if __name__ == "__main__":
    main()
