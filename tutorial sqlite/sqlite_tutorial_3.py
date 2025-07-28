import sqlite3

print("📚 SQLite Tutorial - Parte 3: Consultar Dados (SELECT)")
print("=" * 60)

conexao = sqlite3.connect('tutorial.db')
cursor = conexao.cursor()

# CONSULTA 1: Buscar tudo
print("\n🔍 CONSULTA 1: Buscar TODOS os produtos...")
cursor.execute("SELECT * FROM produtos")
todos_produtos = cursor.fetchall()

print(f"📊 Encontrados: {len(todos_produtos)} produtos")
print("🗂️ Estrutura: (id, nome, preco, categoria, em_estoque)")

for produto in todos_produtos[:3]:  # Mostrar apenas 3
    print(f"  {produto}")

# CONSULTA 2: Buscar colunas específicas
print("\n🎯 CONSULTA 2: Buscar apenas NOME e PREÇO...")
cursor.execute("SELECT nome, preco FROM produtos")
nomes_precos = cursor.fetchall()

for nome, preco in nomes_precos[:4]:  # Mostrar 4
    print(f"  • {nome}: R$ {preco:.2f}")

# CONSULTA 3: Buscar com filtro (WHERE)
print("\n🔎 CONSULTA 3: Produtos MAIS BARATOS que R$ 5...")
cursor.execute("SELECT nome, preco FROM produtos WHERE preco < ?", (5.0,))
baratos = cursor.fetchall()

print(f"💰 Encontrados {len(baratos)} produtos baratos:")
for nome, preco in baratos:
    print(f"  • {nome}: R$ {preco:.2f}")

# CONSULTA 4: Buscar por categoria
print("\n🍎 CONSULTA 4: Produtos da categoria 'Frutas'...")
cursor.execute("SELECT nome, preco FROM produtos WHERE categoria = ?", ("Frutas",))
frutas = cursor.fetchall()

for nome, preco in frutas:
    print(f"  🍓 {nome}: R$ {preco:.2f}")

# CONSULTA 5: Ordenar resultados
print("\n📈 CONSULTA 5: Produtos ordenados por PREÇO (menor para maior)...")
cursor.execute("SELECT nome, preco FROM produtos ORDER BY preco ASC LIMIT 3")
mais_baratos = cursor.fetchall()

for i, (nome, preco) in enumerate(mais_baratos, 1):
    print(f"  {i}º lugar: {nome} - R$ {preco:.2f}")

# CONSULTA 6: fetchone() vs fetchall()
print("\n🎯 CONSULTA 6: Diferença entre fetchone() e fetchall()...")

# fetchone() - pega apenas 1 registro
cursor.execute("SELECT nome, preco FROM produtos ORDER BY preco DESC")
mais_caro = cursor.fetchone()  # Apenas o primeiro (mais caro)
print(f"💎 Produto mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}")

# fetchall() - pega todos os restantes
restantes = cursor.fetchall()
print(f"📦 Restaram {len(restantes)} produtos para buscar")

# CONSULTA 7: Contar e agrupar
print("\n📊 CONSULTA 7: Quantos produtos por categoria...")
cursor.execute("""
    SELECT categoria, COUNT(*) as quantidade 
    FROM produtos 
    GROUP BY categoria 
    ORDER BY quantidade DESC
""")

por_categoria = cursor.fetchall()
print("📈 Ranking de categorias:")
for categoria, quantidade in por_categoria:
    print(f"  • {categoria}: {quantidade} produtos")

# CONSULTA 8: Busca com LIKE (parecido)
print("\n🔍 CONSULTA 8: Produtos que contêm 'kg' no nome...")
cursor.execute("SELECT nome, preco FROM produtos WHERE nome LIKE ?", ("%kg%",))
produtos_kg = cursor.fetchall()

for nome, preco in produtos_kg:
    print(f"  ⚖️ {nome}: R$ {preco:.2f}")

# CONSULTA 9: Calcular média de preços
print("\n🧮 CONSULTA 9: Estatísticas de preços...")
cursor.execute("""
    SELECT 
        COUNT(*) as total_produtos,
        AVG(preco) as preco_medio,
        MIN(preco) as menor_preco,
        MAX(preco) as maior_preco
    FROM produtos
""")

stats = cursor.fetchone()
total, media, minimo, maximo = stats

print(f"📊 Estatísticas:")
print(f"  • Total de produtos: {total}")
print(f"  • Preço médio: R$ {media:.2f}")
print(f"  • Menor preço: R$ {minimo:.2f}")
print(f"  • Maior preço: R$ {maximo:.2f}")

conexao.close()

print("\n" + "=" * 60)
print("🎉 COMANDOS SELECT QUE VOCÊ APRENDEU:")
print("• SELECT * FROM tabela (buscar tudo)")
print("• SELECT coluna1, coluna2 FROM tabela (colunas específicas)")
print("• WHERE campo = valor (filtrar)")
print("• ORDER BY campo ASC/DESC (ordenar)")
print("• LIMIT numero (limitar resultados)")
print("• LIKE '%texto%' (busca parecida)")
print("• COUNT(), AVG(), MIN(), MAX() (funções)")
print("• GROUP BY (agrupar)")
print("\n🔧 MÉTODOS PYTHON:")
print("• fetchall() = todos os resultados")
print("• fetchone() = apenas um resultado")