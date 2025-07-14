# -*- coding: utf-8 -*-

"""
Aula: O Laço `for` em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre o laço de repetição `for`.
O laço `for` é usado para iterar sobre uma sequência (como uma lista, tupla,
dicionário, string ou um objeto range).
"""

# --- 1. Iterando sobre uma Sequência ---
# O uso mais comum do `for` é para percorrer cada item de uma sequência.

print("--- 1. Iterando sobre uma Lista ---")
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(f"- {fruta.capitalize()}")
print("\n")

print("--- Iterando sobre uma String ---")
for letra in "Python":
    print(letra, end=" ") # O argumento 'end' muda o que é impresso no final
print("\n\n")


# --- 2. A Função `range()` ---
# A função `range()` gera uma sequência de números, o que é muito útil para
# executar um laço um número específico de vezes.

# range(fim): Gera números de 0 até fim-1
print("--- 2. A Função `range()` ---")
print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

# range(inicio, fim): Gera números de inicio até fim-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print("\n")

# range(inicio, fim, passo): Gera números de inicio até fim-1, pulando de 'passo' em 'passo'
print("\nrange(0, 11, 2) - Pares de 0 a 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n\n")


# --- 3. Iterando sobre Dicionários ---
# O laço `for` é extremamente útil para trabalhar com dicionários.

aluno = {
    "nome": "Fernanda",
    "idade": 25,
    "curso": "Biologia"
}
print("--- 3. Iterando sobre Dicionários ---")
print("Dicionário 'aluno':", aluno)

# Por padrão, iterar sobre um dicionário percorre suas chaves
print("\nIterando sobre as chaves:")
for chave in aluno:
    print(f"- Chave: '{chave}' (Valor: {aluno[chave]})")

# Para iterar sobre os valores, use .values()
print("\nIterando sobre os valores com .values():")
for valor in aluno.values():
    print(f"- {valor}")

# A forma mais comum é iterar sobre os pares (chave, valor) com .items()
print("\nIterando sobre os itens com .items():")
for chave, valor in aluno.items():
    print(f"- {chave.capitalize()}: {valor}")
print("\n")


# --- 4. `break` e `continue` ---
# Você pode controlar o fluxo de um laço.

print("--- 4. `break` e `continue` ---")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# `break`: Interrompe o laço completamente.
print("Exemplo com `break` (para quando encontrar um número > 5):")
for numero in numeros:
    if numero > 5:
        break
    print(numero, end=" ")
print("\n")

# `continue`: Pula para a próxima iteração do laço.
print("\nExemplo com `continue` (pula os números pares):")
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
print("\n\n")


# --- 5. O Bloco `else` em um Laço `for` ---
# Um `else` pode ser executado no final de um laço `for`, mas somente se
# o laço terminar naturalmente (sem ser interrompido por um `break`).

print("--- 5. O Bloco `else` em um Laço `for` ---")
print("Procurando o número 11 na lista:", numeros)
for numero in numeros:
    if numero == 11:
        print("Número 11 encontrado!")
        break
else:
    # Este bloco só executa porque o 'break' nunca foi acionado.
    print("O laço terminou e o número 11 não foi encontrado.")
print("\n")


# --- 6. Laços Aninhados (Nested Loops) ---
# Você pode colocar um laço dentro de outro. É útil para trabalhar com
# estruturas de dados aninhadas, como matrizes (listas de listas).

print("--- 6. Laços Aninhados ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Imprimindo a matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t") # \t é um caractere de tabulação
    print() # Pula para a próxima linha no final de cada linha da matriz

