# -*- coding: utf-8 -*-

"""
Aula: Listas em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre listas, uma das estruturas de
dados mais importantes e flexíveis do Python. Listas são coleções ordenadas
e mutáveis de itens.
"""

# --- 1. Criando Listas ---
# Uma lista é criada com colchetes [] e os itens são separados por vírgulas.
# Listas podem conter diferentes tipos de dados.

lista_de_frutas = ["maçã", "banana", "laranja", "uva"]
lista_de_numeros = [1, 2, 3, 4, 5]
lista_mista = ["texto", 10, True, 3.14]
lista_vazia = []

print("--- 1. Criando Listas ---")
print("Lista de Frutas:", lista_de_frutas)
print("Lista de Números:", lista_de_numeros)
print("Lista Mista:", lista_mista)
print("Lista Vazia:", lista_vazia)
print("\n")


# --- 2. Acessando Itens da Lista (Indexação) ---
# Você acessa os itens de uma lista por sua posição (índice), que começa em 0.
# Índices negativos contam a partir do final da lista.

# Índices: maçã | banana | laranja | uva
#          0   |    1   |    2    |  3
#         -4   |   -3   |   -2    | -1

primeira_fruta = lista_de_frutas[0]
terceira_fruta = lista_de_frutas[2]
ultima_fruta = lista_de_frutas[-1]

print("--- 2. Acessando Itens ---")
print("Primeira fruta (índice 0):", primeira_fruta)
print("Terceira fruta (índice 2):", terceira_fruta)
print("Última fruta (índice -1):", ultima_fruta)
print("\n")


# --- 3. Fatiando Listas (Slicing) ---
# Você pode pegar um "pedaço" da lista, criando uma nova sub-lista.
# A sintaxe é [inicio:fim:passo]. O item no índice 'fim' não é incluído.

primeiras_duas_frutas = lista_de_frutas[0:2] # ou [:2]
da_segunda_ate_o_final = lista_de_frutas[1:]
frutas_invertidas = lista_de_frutas[::-1] # Um truque comum para inverter a lista

print("--- 3. Fatiando Listas ---")
print("Lista original:", lista_de_frutas)
print("As duas primeiras ([:2]):", primeiras_duas_frutas)
print("Da segunda em diante ([1:]):", da_segunda_ate_o_final)
print("Lista invertida ([::-1]):", frutas_invertidas)
print("\n")


# --- 4. Modificando Listas ---
# Listas são mutáveis, o que significa que você pode alterar seu conteúdo.

print("--- 4. Modificando Listas ---")
print("Lista original:", lista_de_frutas)

# Alterar um item
lista_de_frutas[1] = "morango"
print("Após alterar o índice 1 para 'morango':", lista_de_frutas)

# Adicionar um item ao final (append)
lista_de_frutas.append("abacaxi")
print("Após append('abacaxi'):", lista_de_frutas)

# Inserir um item em uma posição específica (insert)
lista_de_frutas.insert(1, "banana") # Insere "banana" no índice 1
print("Após insert(1, 'banana'):", lista_de_frutas)

# Remover um item pelo valor (remove)
lista_de_frutas.remove("laranja")
print("Após remove('laranja'):", lista_de_frutas)

# Remover um item pela posição (pop)
fruta_removida = lista_de_frutas.pop(2) # Remove e retorna o item do índice 2
print(f"Após pop(2), a fruta removida foi '{fruta_removida}'")
print("Lista atual:", lista_de_frutas)

# Remover um item pela posição com 'del'
del lista_de_frutas[0]
print("Após del lista_de_frutas[0]:", lista_de_frutas)
print("\n")


# --- 5. Métodos e Funções Úteis para Listas ---
numeros = [5, 1, 9, 3, 7]
print("--- 5. Métodos e Funções Úteis ---")
print("Lista de números original:", numeros)

# len(): Retorna o tamanho da lista
print("Tamanho da lista (len):", len(numeros))

# sort(): Ordena a lista original (in-place)
numeros.sort()
print("Lista ordenada (sort):", numeros)
numeros.sort(reverse=True) # Ordena em ordem decrescente
print("Lista ordenada decrescente (sort(reverse=True)):", numeros)

# sorted(): Retorna uma NOVA lista ordenada, sem alterar a original
numeros_desordenados = [8, 2, 6, 4]
numeros_ordenados_copia = sorted(numeros_desordenados)
print("Nova lista ordenada (sorted):", numeros_ordenados_copia)
print("Lista original permaneceu igual:", numeros_desordenados)

# sum(), min(), max()
print("Soma dos números:", sum(numeros_desordenados))
print("Menor número:", min(numeros_desordenados))
print("Maior número:", max(numeros_desordenados))
print("\n")


# --- 6. Listas de Listas (Listas Aninhadas) ---
# Você pode ter listas como itens de outra lista, criando uma estrutura de matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("--- 6. Listas Aninhadas (Matriz) ---")
print("Matriz completa:", matriz)

# Para acessar um elemento, você usa dois índices: [linha][coluna]
elemento_central = matriz[1][1] # Linha 1, coluna 1 (o número 5)
print("Elemento central (matriz[1][1]):", elemento_central)

