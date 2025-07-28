from telegram.ext import ApplicationBuilder # Build principal do bot
from dotenv import load_dotenv # Carregar .env
import os
from handlers import start_handler # Comandos 

# Carrega as variáveis do arquivo .env
load_dotenv()
token = str(os.getenv("TELEGRAM_TOKEN"))

if not token: # Caso não exista
    raise ValueError("❌ A variável TELEGRAM_TOKEN não está definida no arquivo .env.")

# Cria e inicia o bot
def main():
    app = ApplicationBuilder().token(token).build() # Build do app, informando o token

    app.add_handler(start_handler) # Comando /start

    print("✅ Bot iniciado com sucesso. Rodando no momento...")
    app.run_polling()

if __name__ == "__main__":
    main()
