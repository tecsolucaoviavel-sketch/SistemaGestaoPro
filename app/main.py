import sqlite3
import os

# Caminho para o banco de dados que será criado
DB_PATH = "database/gestao_real.db"

def inicializar_sistema():
    # Conecta ao banco (se não existir, ele cria o ficheiro .db)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Criar a tabela de inventário se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            preco_venda REAL,
            qtd_atual INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_produto(nome, preco, qtd):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventario (descricao, preco_venda, qtd_atual) VALUES (?, ?, ?)", (nome, preco, qtd))
    conn.commit()
    conn.close()
    print(f"\n✅ Produto '{nome}' registado com sucesso!")

def listar_stock():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventario")
    produtos = cursor.fetchall()
    print("\n--- STOCK ATUAL ---")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]} Kz | Qtd: {p[3]}")
    conn.close()

# Menu do Sistema
inicializar_sistema()
while True:
    print("\n1. Registar Produto | 2. Ver Stock | 0. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço de venda: "))
        qtd = int(input("Quantidade: "))
        adicionar_produto(nome, preco, qtd)
    elif opcao == "2":
        listar_stock()
    elif opcao == "0":
        break
