# -*- coding: utf-8 -*-

"""
Aula: Estruturas Condicionais em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre as estruturas condicionais
(if, elif, else). Elas permitem que o programa execute diferentes blocos
de código com base em condições booleanas (True ou False).
"""

# --- 1. A Estrutura `if` ---
# O bloco de código dentro do `if` só é executado se a condição for verdadeira.
# A indentação (espaços no início da linha) é obrigatória e define o bloco.

idade = 20

print("--- 1. A Estrutura `if` ---")
if idade >= 18:
    print("Você é maior de idade.")
    print("Já pode tirar a carteira de motorista.")

temperatura = 30
if temperatura > 25:
    print("Está um dia quente!")
print("\n")


# --- 2. A Estrutura `else` ---
# O `else` define um bloco de código que será executado se a condição do `if`
# for falsa. Ele é opcional e deve vir após o bloco `if`.

print("--- 2. A Estrutura `else` ---")
media_aluno = 5.5

if media_aluno >= 7.0:
    print("Aluno aprovado!")
else:
    print("Aluno em recuperação.")
print("\n")


# --- 3. A Estrutura `elif` (else if) ---
# Permite verificar múltiplas condições em sequência. Assim que uma condição
# `elif` for verdadeira, seu bloco é executado e as demais são ignoradas.

print("--- 3. A Estrutura `elif` ---")
hora_atual = 14

if hora_atual < 12:
    print("Bom dia!")
elif hora_atual < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
print("\n")


# --- 4. Condicionais com Operadores Lógicos (`and`, `or`, `not`) ---
# Você pode criar condições mais complexas combinando operadores lógicos.

print("--- 4. Condicionais com Operadores Lógicos ---")
usuario_logado = True
e_admin = False
tem_cartao_credito = True

# and: ambas as condições devem ser verdadeiras
if usuario_logado and e_admin:
    print("Acesso de administrador concedido.")
else:
    print("Acesso de administrador negado.")

# or: pelo menos uma condição deve ser verdadeira
if usuario_logado or tem_cartao_credito:
    print("Você pode finalizar a compra.")

# not: inverte o resultado da condição
if not e_admin:
    print("Você é um usuário comum.")
print("\n")


# --- 5. Condicionais Aninhadas ---
# Você pode colocar uma estrutura condicional dentro de outra.

print("--- 5. Condicionais Aninhadas ---")
idade_para_votar = 16
tem_titulo_eleitor = True

if idade >= 18:
    print("Voto obrigatório.")
    if tem_titulo_eleitor:
        print("Você está apto a votar.")
    else:
        print("Você precisa tirar seu título de eleitor.")
elif idade >= 16:
    print("Voto facultativo.")
else:
    print("Você ainda não pode votar.")
print("\n")


# --- 6. Operador Ternário (Expressão Condicional) ---
# Uma forma compacta de escrever uma estrutura `if-else` simples em uma única linha.
# Sintaxe: valor_se_verdadeiro if condicao else valor_se_falso

print("--- 6. Operador Ternário ---")
idade_cliente = 25
status = "Maior de idade" if idade_cliente >= 18 else "Menor de idade"
print(f"O status do cliente é: {status}")

nivel_acesso = "VIP" if e_admin else "Padrão"
print(f"Seu nível de acesso é: {nivel_acesso}")
print("\n")


# --- 7. Condicionais com Dicionários e Listas ---
# É muito comum usar condicionais para verificar dados em coleções.

print("--- 7. Condicionais com Dicionários e Listas ---")
frutas = ["maçã", "banana", "laranja"]
aluno = {"nome": "Beatriz", "curso": "Letras"}

# Verificando se um item existe em uma lista
if "banana" in frutas:
    print("Sim, 'banana' está na lista de frutas.")

# Verificando se uma chave existe em um dicionário
if "curso" in aluno:
    print(f"O curso de {aluno['nome']} é {aluno['curso']}.")

if "matricula" not in aluno:
    print("A chave 'matricula' não foi encontrada no dicionário do aluno.")

