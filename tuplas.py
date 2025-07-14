# -*- coding: utf-8 -*-

"""
Aula: Tuplas em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre tuplas. Tuplas são coleções
ordenadas e IMUTÁVEIS de itens. Pense nelas como "listas que não podem ser
alteradas".
"""

# --- 1. Criando Tuplas ---
# Uma tupla é criada com parênteses () e os itens são separados por vírgulas.

coordenadas_gps = (34.0522, -118.2437) # Ex: Latitude e Longitude
cores_rgb = ("vermelho", "verde", "azul")
tupla_mista = ("janeiro", 1, True)

# Para criar uma tupla com um único item, você DEVE usar uma vírgula no final.
tupla_de_um_item = (99,)
nao_e_uma_tupla = (99) # Isso é apenas o número 99 dentro de parênteses.

print("--- 1. Criando Tuplas ---")
print("Coordenadas GPS:", coordenadas_gps)
print("Cores RGB:", cores_rgb)
print(f"Tupla de um item: {tupla_de_um_item} (Tipo: {type(tupla_de_um_item)})")
print(f"Isto não é uma tupla: {nao_e_uma_tupla} (Tipo: {type(nao_e_uma_tupla)})")
print("\n")


# --- 2. Acessando Itens (Indexação e Fatiamento) ---
# Funciona exatamente como nas listas. Você acessa os itens por sua posição (índice).

# Índices: vermelho | verde | azul
#             0     |   1   |   2
#            -3     |  -2   |  -1

cor_primaria = cores_rgb[0]
ultima_cor = cores_rgb[-1]
fatia_de_cores = cores_rgb[0:2]

print("--- 2. Acessando Itens ---")
print("Tupla de cores:", cores_rgb)
print("Primeira cor (índice 0):", cor_primaria)
print("Última cor (índice -1):", ultima_cor)
print("Fatia das duas primeiras cores ([0:2]):", fatia_de_cores)
print("\n")


# --- 3. Imutabilidade: A Grande Diferença ---
# Esta é a característica principal das tuplas. Uma vez criada, você NÃO PODE
# alterar, adicionar ou remover itens.

print("--- 3. Imutabilidade ---")
print("Tentando alterar a tupla de cores...")

try:
    # A linha abaixo vai gerar um erro (TypeError)!
    cores_rgb[0] = "amarelo"
except TypeError as e:
    print(f"ERRO: {e}")
    print("Tuplas são imutáveis e não suportam atribuição de item.")

# Você também não pode usar métodos como .append(), .remove() ou .pop().
# Se precisar modificar os dados, você deve primeiro convertê-los para uma lista.
lista_de_cores = list(cores_rgb)
lista_de_cores.append("amarelo")
nova_tupla_de_cores = tuple(lista_de_cores)

print("Tupla original:", cores_rgb)
print("Nova tupla após conversão e modificação:", nova_tupla_de_cores)
print("\n")


# --- 4. Métodos de Tuplas ---
# Tuplas têm apenas dois métodos, pois não podem ser modificadas.

dados = (10, 20, 30, 20, 40, 20)
print("--- 4. Métodos de Tuplas ---")
print("Tupla de dados:", dados)

# .count(): Conta quantas vezes um item aparece na tupla.
contagem_do_20 = dados.count(20)
print(f"O número 20 aparece {contagem_do_20} vezes.")

# .index(): Retorna o índice da primeira ocorrência de um item.
indice_do_30 = dados.index(30)
print(f"O número 30 está no índice {indice_do_30}.")
print("\n")


# --- 5. Desempacotamento de Tuplas (Tuple Unpacking) ---
# Uma forma elegante e muito "pythônica" de atribuir os valores de uma tupla
# a múltiplas variáveis de uma só vez.

ponto = (5, 10, 15) # Representa um ponto no espaço 3D

# Desempacotando a tupla nas variáveis x, y, e z
x, y, z = ponto

print("--- 5. Desempacotamento de Tuplas ---")
print("Tupla 'ponto':", ponto)
print(f"Valor de x: {x}")
print(f"Valor de y: {y}")
print(f"Valor de z: {z}")
print("\n")


# --- 6. Por que e Quando Usar Tuplas? ---
# 1. Integridade dos Dados: Se você tem dados que não devem mudar
#    (ex: coordenadas, constantes, registros de banco de dados),
#    usar uma tupla garante que eles não serão alterados acidentalmente.

# 2. Performance: Tuplas são ligeiramente mais rápidas e consomem menos
#    memória que listas, pois são mais simples.

# 3. Chaves de Dicionário: Como são imutáveis, tuplas podem ser usadas como
#    chaves em um dicionário, enquanto listas não podem.
dicionario_de_localizacoes = {
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "Nova York"
}
print("--- 6. Quando Usar Tuplas ---")
print("Tupla como chave de dicionário:", dicionario_de_localizacoes)

