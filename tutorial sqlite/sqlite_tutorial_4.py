import sqlite3

print("📚 SQLite Tutorial - Parte 4: UPDATE e DELETE")
print("=" * 50)

conexao = sqlite3.connect('tutorial.db')
cursor = conexao.cursor()

# Primeiro, vamos ver o que temos
print("📋 ESTADO INICIAL - Alguns produtos:")
cursor.execute("SELECT id, nome, preco, categoria FROM produtos LIMIT 5")
for produto in cursor.fetchall():
    print(f"  {produto[0]}. {produto[1]} - R$ {produto[2]:.2f} ({produto[3]})")

print("\n" + "-" * 50)

# UPDATE 1: Atualizar um produto específico
print("\n✏️ UPDATE 1: Mudando preço do Arroz...")

# Primeiro vamos ver o preço atual
cursor.execute("SELECT nome, preco FROM produtos WHERE nome LIKE '%Arroz%'")
antes = cursor.fetchone()
print(f"🔍 Antes: {antes[0]} custava R$ {antes[1]:.2f}")

# Atualizar o preço
novo_preco = 17.90
cursor.execute("""
    UPDATE produtos 
    SET preco = ? 
    WHERE nome LIKE '%Arroz%'
""", (novo_preco,))

# Ver quantas linhas foram afetadas
linhas_alteradas = cursor.rowcount
print(f"✅ {linhas_alteradas} produto(s) atualizado(s)")

# Verificar a mudança
cursor.execute("SELECT nome, preco FROM produtos WHERE nome LIKE '%Arroz%'")
depois = cursor.fetchone()
print(f"🔍 Depois: {depois[0]} agora custa R$ {depois[1]:.2f}")

# UPDATE 2: Atualizar múltiplas colunas
print("\n🔄 UPDATE 2: Atualizando múltiplas colunas...")

cursor.execute("""
    UPDATE produtos 
    SET preco = ?, categoria = ?, em_estoque = ?
    WHERE nome LIKE '%Leite%'
""", (5.20, "Laticínios Premium", False))

cursor.execute("SELECT nome, preco, categoria, em_estoque FROM produtos WHERE nome LIKE '%Leite%'")
leite_info = cursor.fetchone()
print(f"✅ Leite atualizado:")
print(f"   • Preço: R$ {leite_info[1]:.2f}")
print(f"   • Categoria: {leite_info[2]}")
print(f"   • Em estoque: {leite_info[3]}")

# UPDATE 3: Atualizar com base em condição
print("\n💰 UPDATE 3: Aumentar preços de produtos caros em 10%...")

# Ver produtos caros antes
cursor.execute("SELECT nome, preco FROM produtos WHERE preco > 10")
caros_antes = cursor.fetchall()
print(f"🔍 Produtos > R$ 10,00 antes ({len(caros_antes)}):")
for nome, preco in caros_antes:
    print(f"   • {nome}: R$ {preco:.2f}")

# Aumentar preços em 10%
cursor.execute("""
    UPDATE produtos 
    SET preco = preco * 1.10 
    WHERE preco > 10
""")

print(f"✅ {cursor.rowcount} produtos tiveram aumento de 10%")

# Ver depois
cursor.execute("SELECT nome, preco FROM produtos WHERE preco > 11")  # Agora > 11
caros_depois = cursor.fetchall()
print(f"🔍 Produtos caros depois:")
for nome, preco in caros_depois:
    print(f"   • {nome}: R$ {preco:.2f}")

print("\n" + "-" * 50)

# DELETE 1: Deletar produto específico
print("\n🗑️ DELETE 1: Removendo um produto específico...")

# Primeiro inserir um produto para deletar
cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", 
               ("Produto Teste", 1.00, "Teste"))
produto_teste_id = cursor.lastrowid
print(f"➕ Produto teste criado com ID {produto_teste_id}")

# Agora deletar
cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_teste_id,))
print(f"🗑️ {cursor.rowcount} produto deletado (ID {produto_teste_id})")

# DELETE 2: Deletar com condição
print("\n🧹 DELETE 2: Removendo produtos fora de estoque...")

# Primeiro, vamos marcar alguns como fora de estoque
cursor.execute("UPDATE produtos SET em_estoque = FALSE WHERE preco < 3")
cursor.execute("SELECT COUNT(*) FROM produtos WHERE em_estoque = FALSE")
fora_estoque = cursor.fetchone()[0]
print(f"📦 Produtos fora de estoque: {fora_estoque}")

# Deletar produtos fora de estoque
cursor.execute("DELETE FROM produtos WHERE em_estoque = FALSE")
deletados = cursor.rowcount
print(f"🗑️ {deletados} produtos fora de estoque foram removidos")

# CUIDADO: DELETE sem WHERE
print("\n⚠️ ATENÇÃO: DELETE sem WHERE remove TUDO!")
print("❌ NUNCA faça: DELETE FROM produtos")
print("✅ SEMPRE use WHERE: DELETE FROM produtos WHERE condicao")

# Verificar estado final
print("\n📊 ESTADO FINAL:")
cursor.execute("SELECT COUNT(*) FROM produtos")
total_final = cursor.fetchone()[0]
print(f"📦 Total de produtos restantes: {total_final}")

cursor.execute("SELECT nome, preco FROM produtos ORDER BY preco LIMIT 3")
mais_baratos_finais = cursor.fetchall()
print("💰 3 produtos mais baratos:")
for nome, preco in mais_baratos_finais:
    print(f"   • {nome}: R$ {preco:.2f}")

# Salvar todas as mudanças
conexao.commit()
print("\n💾 Todas as mudanças foram salvas!")

conexao.close()

print("\n" + "=" * 50)
print("🎉 COMANDOS UPDATE/DELETE QUE VOCÊ APRENDEU:")
print("\n📝 UPDATE:")
print("• UPDATE tabela SET coluna = valor WHERE condicao")
print("• UPDATE com múltiplas colunas")
print("• UPDATE com cálculos (preco = preco * 1.10)")
print("• cursor.rowcount = quantas linhas foram afetadas")
print("\n🗑️ DELETE:")
print("• DELETE FROM tabela WHERE condicao")
print("• SEMPRE use WHERE (senão deleta tudo!)")
print("• cursor.rowcount = quantas linhas foram deletadas")
print("\n⚠️ LEMBRETE IMPORTANTE:")
print("• SEMPRE use WHERE em UPDATE e DELETE")
print("• Teste com SELECT antes de UPDATE/DELETE")
print("• Use commit() para salvar mudanças")