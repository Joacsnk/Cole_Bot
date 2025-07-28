import sqlite3

print("📚 SQLite Tutorial - Parte 2: Inserir Dados")
print("=" * 50)

# Conectar ao banco que criamos antes
conexao = sqlite3.connect('tutorial.db')
cursor = conexao.cursor()

# MÉTODO 1: Inserir um registro simples
print("\n📝 MÉTODO 1: Inserir um produto...")

sql_inserir = """
INSERT INTO produtos (nome, preco, categoria)
VALUES ('Arroz 5kg', 15.90, 'Grãos')
"""

cursor.execute(sql_inserir)
print("✅ Arroz inserido!")

# MÉTODO 2: Inserir com variáveis (FORMA SEGURA)
print("\n🔒 MÉTODO 2: Inserir com variáveis (seguro)...")

nome = "Leite Integral 1L"
preco = 4.50
categoria = "Laticínios"

sql_seguro = """
INSERT INTO produtos (nome, preco, categoria) 
VALUES (?, ?, ?)
"""

cursor.execute(sql_seguro, (nome, preco, categoria))
print(f"✅ {nome} inserido!")
print("💡 Os '?' protegem contra SQL Injection")

# MÉTODO 3: Inserir múltiplos registros
print("\n📦 MÉTODO 3: Inserir vários produtos de uma vez...")

produtos_lista = [
    ("Banana Prata 1kg", 3.20, "Frutas"),
    ("Maçã Gala 1kg", 5.80, "Frutas"), 
    ("Detergente 500ml", 2.30, "Limpeza"),
    ("Pasta de Dente", 4.90, "Higiene")
]

cursor.executemany(sql_seguro, produtos_lista)
print(f"✅ {len(produtos_lista)} produtos inseridos!")
print("💡 executemany() = inserir vários de uma vez")

# VERIFICAR quantos registros temos
print("\n🔢 VERIFICANDO: Quantos produtos temos?")
cursor.execute("SELECT COUNT(*) FROM produtos")
total = cursor.fetchone()[0]
print(f"📊 Total de produtos: {total}")

# MÉTODO 4: Inserir e pegar o ID gerado
print("\n🆔 MÉTODO 4: Inserir e pegar o ID...")

cursor.execute(sql_seguro, ("Café 500g", 12.50, "Bebidas"))
ultimo_id = cursor.lastrowid
print(f"✅ Café inserido com ID: {ultimo_id}")
print("💡 lastrowid = ID do último registro inserido")

# Salvar tudo
conexao.commit()
print("\n💾 Todas as inserções foram salvas!")

# EXTRA: Vamos ver o que inserimos
print("\n👀 VISUALIZANDO: Alguns produtos inseridos...")
cursor.execute("SELECT id, nome, preco FROM produtos LIMIT 3")
primeiros_tres = cursor.fetchall()

for produto in primeiros_tres:
    id_produto, nome, preco = produto
    print(f"  {id_produto}. {nome} - R$ {preco:.2f}")

conexao.close()

print("\n" + "=" * 50)
print("🎉 RESUMO - FORMAS DE INSERIR:")
print("1. INSERT direto (texto fixo)")
print("2. INSERT com ? (variáveis seguras)")  
print("3. executemany() (múltiplos registros)")
print("4. lastrowid (pegar ID gerado)")
print("\n⚠️ SEMPRE use '?' para variáveis - NUNCA f-strings em SQL!")