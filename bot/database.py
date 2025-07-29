import sqlite3 # Adicionar banco de dados
import os

# Caminho do banco de dados
DB_PATH = os.path.join("data", "cole.db")

def init_db(): # Cria a tabela com id, user_id e item
    os.makedirs("data", exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                item TEXT NOT NULL
            )
        ''')
        conn.commit()

# Adiciona um item à lista
def add_item(user_id: int, item: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shopping_list (user_id, item) VALUES (?, ?)", (user_id, item))
        conn.commit()

# Lista os itens do usuário
def list_items(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, item FROM shopping_list WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

# Pega todos os itens
def get_items(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, item FROM shopping_list WHERE user_id = ?", (user_id,))
        return cursor.fetchall()
    
# Remove itens
def remove_item(user_id: int, item_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM shopping_list WHERE user_id = ? AND id = ?", (user_id, item_id))
        conn.commit()
        return cursor.rowcount > 0

# Limpa a lista
def clear_list(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM shopping_list WHERE user_id = ?", (user_id,))
        conn.commit()
