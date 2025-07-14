# -*- coding: utf-8 -*-

"""
Aula: Variáveis em Python - Um Guia Detalhado

Este script é um guia de estudo focado exclusivamente em variáveis na
linguagem Python. Ele explora a criação, nomeação, tipos e o uso
de variáveis com exemplos práticos.
"""

# --- 1. O que é uma Variável? ---
# Pense em uma variável como uma caixa ou um contêiner com uma etiqueta.
# Você usa a etiqueta (o nome da variável) para guardar e recuperar
# dados (o conteúdo da caixa).

# Exemplo: 'nome_do_produto' é a etiqueta, e "Notebook Gamer" é o dado guardado.
nome_do_produto = "Notebook Gamer"
quantidade_em_estoque = 15
preco_unitario = 6500.50

print("--- Conceito de Variável ---")
print("Produto:", nome_do_produto)
print("Quantidade:", quantidade_em_estoque)
print("Preço: R$", preco_unitario)
print("\n")


# --- 2. Regras e Convenções para Nomes de Variáveis ---
# a) Nomes devem começar com uma letra ou um underscore (_).
# b) O restante do nome pode conter letras, números e underscores.
# c) Nomes de variáveis são "case-sensitive" (idade é diferente de Idade).
# d) Não use palavras reservadas do Python (como if, for, def, etc.).

# Convenção (Boa Prática):
# Use nomes em minúsculas, com palavras separadas por underscore.
# Isso é chamado de "snake_case".

# Nomes Válidos (e bons):
meu_nome = "Lucas"
idade_do_usuario = 28
_valor_temporario = 100

# Nomes Válidos (mas não recomendados):
NomeDeUsuario = "Ana" # Isso é "CamelCase", mais comum em outras linguagens.
nomeDoUsuario = "Bia" # Isso é "lowerCamelCase".

# Nomes Inválidos (causarão erro):
# 2anos = 2 -> não pode começar com número
# meu-nome = "Carlos" -> não pode usar hífen
# for = "loop" -> 'for' é uma palavra reservada

print("--- Nomes de Variáveis (Convenção snake_case) ---")
print("Nome:", meu_nome)
print("Idade:", idade_do_usuario)
print("\n")


# --- 3. Tipagem Dinâmica ---
# Python é uma linguagem de tipagem dinâmica. Isso significa que você não
# precisa declarar o tipo de uma variável. Além disso, a mesma variável
# pode armazenar diferentes tipos de dados em momentos diferentes.

dado = "Este é um texto."
print("--- Tipagem Dinâmica ---")
print(f"Valor inicial da variável 'dado': '{dado}'")

# A função type() é muito útil para descobrir o tipo de uma variável.
print("Tipo da variável 'dado':", type(dado))
print("-" * 20) # Linha separadora

# Agora, vamos atribuir um número à mesma variável 'dado'.
dado = 100
print(f"Novo valor da variável 'dado': {dado}")
print("Tipo da variável 'dado' agora:", type(dado))
print("-" * 20)

# E agora, um valor booleano.
dado = False
print(f"Último valor da variável 'dado': {dado}")
print("Tipo final da variável 'dado':", type(dado))
print("\n")


# --- 4. Usando Variáveis em Operações ---
# Você pode usar variáveis em expressões matemáticas, concatenação de texto, etc.

print("--- Usando Variáveis ---")
numero1 = 75
numero2 = 25
soma = numero1 + numero2
print(f"A soma de {numero1} + {numero2} é {soma}")

primeiro_nome = "Joana"
sobrenome = "Santos"
# Usando f-string (string formatada) para combinar variáveis e texto.
# É a forma mais moderna e legível.
nome_completo = f"{primeiro_nome} {sobrenome}"
print(f"Nome completo: {nome_completo}")

# Exemplo prático: Cálculo de total
total_da_venda = quantidade_em_estoque * preco_unitario
print(f"O valor total do estoque de '{nome_do_produto}' é R$ {total_da_venda}")

