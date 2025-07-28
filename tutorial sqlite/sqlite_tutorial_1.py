import sqlite3

print("📚 SQLite Tutorial - Parte 1: Conectar e Criar")
print("=" * 50)

# PASSO 1: Conectar ao banco de dados
print("\n🔌 PASSO 1: Conectando ao banco...")
conexao = sqlite3.connect('tutorial.db')
print("✅ Conectado! (arquivo 'tutorial.db' criado/aberto)")

# PASSO 2: Criar um cursor
print("\n📝 PASSO 2: Criando cursor...")
cursor = conexao.cursor()
print("✅ Cursor criado!")
print("💡 Cursor = ferramenta para executar comandos SQL")

# PASSO 3: Criar uma tabela
print("\n🏗️ PASSO 3: Criando tabela 'produtos'...")

sql_criar_tabela = """
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT,
    em_estoque BOOLEAN DEFAULT TRUE
)
"""

cursor.execute(sql_criar_tabela)
print("✅ Tabela 'produtos' criada!")

# EXPLICAÇÃO DOS TIPOS DE DADOS
print("\n📖 TIPOS DE DADOS USADOS:")
print("• INTEGER = números inteiros (1, 2, 3...)")
print("• TEXT = textos ('Arroz', 'Leite'...)")  
print("• REAL = números decimais (15.90, 4.50...)")
print("• BOOLEAN = verdadeiro/falso (TRUE, FALSE)")

# EXPLICAÇÃO DOS MODIFICADORES
print("\n🔧 MODIFICADORES EXPLICADOS:")
print("• PRIMARY KEY = chave única (identifica cada linha)")
print("• AUTOINCREMENT = aumenta automaticamente (1, 2, 3...)")
print("• NOT NULL = campo obrigatório")
print("• DEFAULT = valor padrão se não especificar")

# PASSO 4: Salvar mudanças
print("\n💾 PASSO 4: Salvando mudanças...")
conexao.commit()
print("✅ Mudanças salvas!")
print("💡 commit() = confirma as mudanças no arquivo")

# PASSO 5: Fechar conexão
print("\n🚪 PASSO 5: Fechando conexão...")
conexao.close()
print("✅ Conexão fechada!")
print("💡 Sempre feche a conexão para liberar recursos")

print("\n" + "=" * 50)
print("🎉 RESUMO DO QUE FIZEMOS:")
print("1. Conectamos ao banco 'tutorial.db'")
print("2. Criamos uma tabela 'produtos'")
print("3. Definimos 5 colunas com tipos diferentes")
print("4. Salvamos e fechamos")
print("\n💾 Arquivo 'tutorial.db' foi criado na sua pasta!")