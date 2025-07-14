# -*- coding: utf-8 -*-

"""
Aula: Texto (Strings) em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre como manipular strings,
o tipo de dado usado para representar texto em Python. Ele explora a criação,
formatação e os métodos mais comuns para trabalhar com texto.
"""

# --- 1. Criando Strings ---
# Strings podem ser criadas com aspas simples, duplas ou triplas.

string_simples = 'Olá, mundo!'
string_dupla = "Python é poderoso."

# Aspas triplas são úteis para strings que ocupam múltiplas linhas.
string_multilinha = """Esta é uma string
que se estende por
várias linhas."""

print("--- Criando Strings ---")
print("Com aspas simples:", string_simples)
print("Com aspas duplas:", string_dupla)
print("Com aspas triplas:\n" + string_multilinha)
print("\n")


# --- 2. Concatenação e Repetição ---
# Você pode "somar" strings para juntá-las (concatenar)
# ou "multiplicá-las" para repetir.

primeiro_nome = "José"
ultimo_nome = "da Silva"

# Concatenação com o operador +
nome_completo = primeiro_nome + " " + ultimo_nome

# Repetição com o operador *
eco = "Eco! " * 3

print("--- Concatenação e Repetição ---")
print("Nome completo:", nome_completo)
print("Repetição:", eco)
print("\n")


# --- 3. Indexação e Fatiamento (Slicing) ---
# Strings são sequências, o que significa que você pode acessar
# caracteres individuais por sua posição (índice).

# Índices: P  y  t  h  o  n
#          0  1  2  3  4  5
#         -6 -5 -4 -3 -2 -1
palavra = "Python"

primeira_letra = palavra[0]  # Pega o caractere no índice 0
ultima_letra = palavra[-1] # Pega o último caractere

# Fatiamento (slicing) para pegar um pedaço da string: [início:fim:passo]
# O 'fim' não é incluído no resultado.
primeiras_tres_letras = palavra[0:3] # ou simplesmente [:3]
letras_do_meio = palavra[2:4]
letras_alternadas = palavra[::2] # Pega caracteres com passo 2

print("--- Indexação e Fatiamento ---")
print("Palavra:", palavra)
print("Primeira letra (palavra[0]):", primeira_letra)
print("Última letra (palavra[-1]):", ultima_letra)
print("Primeiras três letras (palavra[:3]):", primeiras_tres_letras)
print("Letras do meio (palavra[2:4]):", letras_do_meio)
print("Letras alternadas (palavra[::2]):", letras_alternadas)
print("\n")


# --- 4. Formatação de Strings (f-strings) ---
# A forma mais moderna e recomendada de inserir variáveis em strings.
# Basta colocar um 'f' antes da string e as variáveis entre {}.

item = "café"
preco = 8.50
quantidade = 2
total = preco * quantidade

mensagem = f"O item '{item}' custa R${preco:.2f}. {quantidade} unidades saem por R${total:.2f}."
# Note o :.2f dentro das chaves para formatar o número com 2 casas decimais.

print("--- Formatação com f-strings ---")
print(mensagem)
print("\n")


# --- 5. Métodos Úteis de Strings ---
# Strings vêm com muitas "funções" embutidas, chamadas métodos.

frase = "  Aprender Python é DIVERTIDO!  "

# len() - não é um método, mas uma função que retorna o comprimento
comprimento = len(frase)

# Métodos para mudar a caixa (maiúsculas/minúsculas)
toda_minuscula = frase.lower()
toda_maiuscula = frase.upper()
primeira_letra_maiuscula = frase.strip().capitalize() # Tira espaços e capitaliza
titulo = frase.strip().title() # Tira espaços e coloca cada palavra com inicial maiúscula

# Métodos para remover espaços em branco
sem_espacos_laterais = frase.strip()
sem_espacos_esquerda = frase.lstrip()
sem_espacos_direita = frase.rstrip()

# Métodos de busca e substituição
tem_python = "Python" in frase # Operador 'in' verifica a existência
posicao = frase.find("Python") # Retorna o índice inicial ou -1 se não encontrar
contagem = frase.lower().count('e') # Conta quantas vezes 'e' aparece
frase_substituida = frase.replace("DIVERTIDO", "INCRÍVEL")

# Métodos para dividir e juntar
palavras_da_frase = frase.strip().split(' ') # Divide a string em uma lista de palavras
lista_de_itens = ["maçã", "banana", "laranja"]
string_com_virgulas = ", ".join(lista_de_itens) # Junta itens de uma lista em uma string

print("--- Métodos de Strings ---")
print(f"Frase original: '{frase}' (Comprimento: {comprimento})")
print(f"lower(): '{toda_minuscula}'")
print(f"upper(): '{toda_maiuscula}'")
print(f"strip() e capitalize(): '{primeira_letra_maiuscula}'")
print(f"strip() e title(): '{titulo}'")
print(f"strip(): '{sem_espacos_laterais}'")
print(f"replace(): '{frase_substituida}'")
print(f"split(' '): {palavras_da_frase}")
print(f"join(): '{string_com_virgulas}'")
print(f"Posição de 'Python': {posicao}")
print(f"Contagem da letra 'e': {contagem}")
print("\n")

# --- 6. Caracteres de Escape ---
# Para usar caracteres que têm um significado especial, como quebras de linha ou aspas.
# \n - Nova linha
# \t - Tabulação
# \\ - Barra invertida
# \' - Aspa simples
# \" - Aspa dupla

caminho_arquivo = "C:\\usuarios\\documentos\\relatorio.txt"
citacao = 'Ele disse: "Olá, mundo!".'
citacao_com_escape = "Ele disse: \"Olá, mundo!\"."

print("--- Caracteres de Escape ---")
print("Caminho de arquivo:", caminho_arquivo)
print("Citação:", citacao)
print("Citação com escape:", citacao_com_escape)

