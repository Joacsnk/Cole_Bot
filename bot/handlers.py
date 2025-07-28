from telegram import Update # Update do chat (mensagem recebida)
from telegram.ext import CommandHandler, ContextTypes # Comandos e configurações extras

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): # Mensagem de /start
    if update.message: # Caso não seja None
       await update.message.reply_text("Olá! Eu sou o Cole, seu assistente de compras 🛒.\n\nUse /add para adicionar itens à sua lista.")
    else:
        print("update.message está None")

# Registra os handlers
start_handler = CommandHandler("start", start)
