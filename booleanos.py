# -*- coding: utf-8 -*-

"""
Aula: Booleanos em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre o tipo de dado booleano (bool)
em Python. Ele explora os valores True e False, operadores de comparação,
operadores lógicos e o conceito de "Truthiness".
"""

# --- 1. O que são Booleanos? ---
# O tipo booleano (bool) tem apenas dois valores possíveis: True e False.
# Eles são a base para a tomada de decisões em programação.
# Importante: Em Python, eles são escritos com a primeira letra maiúscula.

tem_sol = True
esta_chovendo = False

print("--- O que são Booleanos? ---")
print(f"O valor de 'tem_sol' é: {tem_sol} (Tipo: {type(tem_sol)})")
print(f"O valor de 'esta_chovendo' é: {esta_chovendo} (Tipo: {type(esta_chovendo)})")
print("\n")


# --- 2. Operadores de Comparação ---
# São usados para comparar valores e o resultado da comparação é sempre um booleano.

idade = 20
idade_para_dirigir = 18
temperatura = 25

# == (Igual a)
e_igual = (5 == 5) # True

# != (Diferente de)
e_diferente = (5 != 6) # True

# > (Maior que)
e_maior = (idade > idade_para_dirigir) # True

# < (Menor que)
e_menor = (temperatura < 10) # False

# >= (Maior ou igual a)
e_maior_ou_igual = (idade >= 18) # True

# <= (Menor ou igual a)
e_menor_ou_igual = (temperatura <= 25) # True

print("--- Operadores de Comparação ---")
print(f"5 == 5 é {e_igual}")
print(f"5 != 6 é {e_diferente}")
print(f"A idade {idade} é maior que {idade_para_dirigir}? {e_maior}")
print(f"A temperatura {temperatura} é menor que 10? {e_menor}")
print(f"A idade {idade} é maior ou igual a 18? {e_maior_ou_igual}")
print(f"A temperatura {temperatura} é menor ou igual a 25? {e_menor_ou_igual}")
print("\n")


# --- 3. Operadores Lógicos ---
# Combinam expressões booleanas para criar condições mais complexas.

# and: Retorna True somente se AMBAS as condições forem verdadeiras.
pode_sair_de_camiseta = tem_sol and (temperatura > 22) # True and True -> True

# or: Retorna True se PELO MENOS UMA das condições for verdadeira.
levar_guarda_chuva = esta_chovendo or (temperatura < 15) # False or False -> False

# not: Inverte o valor booleano. True vira False, e False vira True.
nao_tem_sol = not tem_sol # not True -> False

print("--- Operadores Lógicos ---")
print(f"Tem sol E a temperatura é maior que 22? {pode_sair_de_camiseta}")
print(f"Está chovendo OU a temperatura é menor que 15? {levar_guarda_chuva}")
print(f"Não tem sol? {nao_tem_sol}")
print("\n")


# --- 4. O Conceito de "Truthiness" e "Falsiness" ---
# Em um contexto booleano (como um if), outros tipos de dados podem ser
# avaliados como True ou False.

# Valores considerados "Falsy" (falsos):
# - O número 0 (int e float)
# - Strings vazias ""
# - Listas, dicionários e outras coleções vazias
# - O valor None

# Quase todo o resto é considerado "Truthy" (verdadeiro).

print("--- Truthiness e Falsiness ---")
print("Avaliando o número 0:", bool(0))
print("Avaliando o número 5:", bool(5))
print("Avaliando uma string vazia:", bool(""))
print("Avaliando a string 'Python':", bool("Python"))
print("Avaliando uma lista vazia:", bool([]))
print("Avaliando o valor None:", bool(None))
print("\n")


# --- 5. Booleanos em Estruturas de Controle ---
# O uso mais comum de booleanos é para decidir qual bloco de código executar.

usuario_logado = True
e_admin = False

print("--- Booleanos em Controle de Fluxo (if/else) ---")
if usuario_logado:
    print("Bem-vindo, usuário!")
    if e_admin:
        print("Você tem acesso ao painel de administração.")
    else:
        print("Você é um usuário padrão.")
else:
    print("Por favor, faça o login para continuar.")

