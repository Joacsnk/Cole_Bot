from telegram import Update # Update do chat (mensagem recebida)
from telegram.ext import CommandHandler, ContextTypes # Comandos e configurações extras
from database import add_item, get_items, remove_item, clear_list
from telegram.constants import ParseMode 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): # Mensagem de /start
    if update.message: # Caso não seja None
       await update.message.reply_text("Olá! Eu sou o Cole, seu assistente de compras 🛒.\n\nUse /add para adicionar itens à sua lista.")
    else:
        print("update.message está None")

start_handler = CommandHandler("start", start)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE): # Adiciona itens
    
    if not update.message or not update.effective_user:
        print("❌ update.message ou update.effective_user está None") # Caso esteja None
        return
    
    user_id = update.effective_user.id
    
    args = context.args if context.args else []
    item = " ".join(args) # Junta todos os args
    

    if not item:
        await update.message.reply_text("❌ Você precisa informar o item. Ex: /add leite")
        return

    add_item(user_id, item) 
    await update.message.reply_text(f"✅ Item '{item}' adicionado à sua lista.")
    
add_handler = CommandHandler("add", add)


async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE): # Lista todos os itens
    
    if not update.message or not update.effective_user:
        print("❌ update.message ou update.effective_user está None") # Caso esteja None
        return
    
    user_id = update.effective_user.id
    items = get_items(user_id)

    if not items:
        await update.message.reply_text("Sua lista de compras está vazia.")
        return
    
    text = "📝 *Sua Lista de Compras:*\n\n" # Lista numerada em um index
    for index, (db_id, item) in enumerate(items, start=1):
        text += f"{index}. {item}\n"

    if context.user_data is None:
        context.user_data = {}
    context.user_data["index_map"] = {i + 1: item[0] for i, item in enumerate(items)}

    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

list_handler = CommandHandler("list", list_items)

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if not update.message or not update.effective_user:
        print("❌ update.message ou update.effective_user está None") # Caso esteja None
        return
    
    user_id = update.effective_user.id

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Use o número da lista. Ex: /remove 2")
        return

    index = int(context.args[0])
    if context.user_data is None:
        context.user_data = {}
    index_map = context.user_data.get("index_map", {})

    if index not in index_map:
        await update.message.reply_text("Esse número não existe na sua lista atual.")
        return

    real_id = index_map[index]
    sucesso = remove_item(user_id, real_id)

    if sucesso:
        await update.message.reply_text(f"Item {index} removido com sucesso.")
    else:
        await update.message.reply_text("Erro ao remover o item.")


remove_handler = CommandHandler("remove", remove)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE): # Limpa toda a lista
    
    if not update.message or not update.effective_user:
        print("❌ update.message ou update.effective_user está None") # Caso esteja None
        return

    user_id = update.effective_user.id
    clear_list(user_id)
    await update.message.reply_text("Sua lista foi apagada com sucesso.")

clear_handler = CommandHandler("clear", clear)