# -*- coding: utf-8 -*-

"""
Aula: Entrada de Dados em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre como receber dados
do usuário através do teclado. Abordaremos a função input(), a conversão
de tipos e como lidar com erros de entrada.
"""

# --- 1. A Função `input()` ---
# A função `input()` pausa a execução do programa e espera que o usuário
# digite algo e pressione Enter.
# O texto digitado é SEMPRE retornado como uma string (str).

print("--- 1. A Função `input()` ---")
# O texto dentro dos parênteses do input() é o "prompt", a mensagem
# que aparece para o usuário.
nome = input("Por favor, digite seu nome: ")

print(f"Olá, {nome}! Bem-vindo(a).")
print(f"O tipo da variável 'nome' é: {type(nome)}")
print("\n")


# --- 2. Convertendo a Entrada (Type Casting) ---
# Como o `input()` sempre retorna uma string, se você precisar de um número,
# terá que convertê-lo usando funções como `int()` ou `float()`.

print("--- 2. Convertendo a Entrada ---")
ano_nascimento_str = input("Em que ano você nasceu? ")

# Convertendo a string para um inteiro para poder fazer cálculos
ano_nascimento_int = int(ano_nascimento_str)
idade = 2024 - ano_nascimento_int

print(f"Você tem ou fará aproximadamente {idade} anos em 2024.")
print("\n")


# --- 3. Lidando com Erros de Entrada (try-except) ---
# O que acontece se o usuário digitar "abc" quando pedimos um número?
# A conversão com `int()` vai gerar um erro (ValueError) e quebrar o programa.
# Para evitar isso, usamos um bloco `try-except`.

print("--- 3. Lidando com Erros de Entrada ---")
while True: # Cria um loop que só para quando a entrada for válida
    try:
        altura_str = input("Digite sua altura em metros (ex: 1.75): ")
        # Tenta converter para float
        altura_float = float(altura_str)
        print(f"Sua altura de {altura_float}m foi registrada com sucesso.")
        break # Sai do loop se a conversão deu certo
    except ValueError:
        # Este bloco só é executado se o `try` falhar
        print("Entrada inválida! Por favor, digite um número.")
print("\n")


# --- 4. Exemplo Prático: Preenchendo um Dicionário ---
# Vamos usar o que aprendemos para criar um dicionário com dados do usuário.

print("--- 4. Exemplo Prático: Preenchendo um Dicionário ---")

# Inicializa um dicionário vazio para armazenar os dados do produto
produto = {}

print("Cadastro de Novo Produto:")
# Pede os dados e os adiciona ao dicionário
produto["nome"] = input("Nome do produto: ")
produto["marca"] = input("Marca do produto: ")

# Tratamento de erro para o preço
while True:
    try:
        preco_str = input("Preço do produto (ex: 49.99): ")
        produto["preco"] = float(preco_str)
        break
    except ValueError:
        print("Valor inválido para o preço. Use ponto como separador decimal.")

# Tratamento de erro para a quantidade
while True:
    try:
        qtd_str = input("Quantidade em estoque: ")
        produto["estoque"] = int(qtd_str)
        break
    except ValueError:
        print("Valor inválido para a quantidade. Digite um número inteiro.")


print("\n--- Produto Cadastrado ---")
# Imprime o dicionário resultante
print(produto)

print("\nDetalhes do Produto:")
for chave, valor in produto.items():
    print(f"- {chave.capitalize()}: {valor}")

