# -*- coding: utf-8 -*-

"""
Aula: Blocos de Tratamento de Erros (try/except) em Python

Este script é um guia de estudo detalhado sobre como lidar com exceções
(erros que ocorrem durante a execução do programa) usando os blocos
`try`, `except`, `else` e `finally`.
"""

# --- 1. O que é uma Exceção? ---
# Uma exceção é um erro que acontece durante a execução de um programa.
# Se não for tratada, ela interrompe o fluxo normal e encerra o programa.

print("--- 1. Exemplo de Erro não Tratado ---")
# A linha abaixo, se descomentada, causaria um ZeroDivisionError:
# resultado = 10 / 0

# Acessar uma chave que não existe em um dicionário causa um KeyError.
dicionario_exemplo = {"nome": "Ana"}
# A linha abaixo, se descomentada, causaria um KeyError:
# print(dicionario_exemplo["idade"])
print("Se os erros acima não fossem comentados, o programa pararia aqui.")
print("\n")


# --- 2. O Bloco `try...except` ---
# Para evitar que o programa quebre, colocamos o código "perigoso"
# dentro de um bloco `try`. Se um erro ocorrer, o bloco `except` é executado.

print("--- 2. O Bloco `try...except` ---")
try:
    numero_str = input("Digite um número inteiro: ")
    numero_int = int(numero_str)
    print(f"O número digitado foi {numero_int}.")
except:
    # Este bloco `except` genérico captura QUALQUER erro.
    print("Ocorreu um erro! Você provavelmente não digitou um número inteiro.")
print("\n")


# --- 3. Capturando Exceções Específicas ---
# É uma boa prática capturar apenas os erros que você espera.
# Isso evita esconder bugs inesperados.

print("--- 3. Capturando Exceções Específicas ---")
usuario = {"username": "carla", "acessos": 5}

try:
    # Tentativa de acessar uma chave que não existe
    print(f"Email do usuário: {usuario['email']}")
except KeyError:
    # Este bloco só executa se um KeyError ocorrer.
    print("Erro: A chave 'email' não foi encontrada no dicionário do usuário.")
except TypeError:
    # Este bloco só executa se um TypeError ocorrer.
    print("Erro: Ocorreu um erro de tipo nos dados.")

# Exemplo com múltiplos tipos de erro
try:
    valor = int(input("Digite um número para dividir 10: "))
    resultado = 10 / valor
    print(f"O resultado é {resultado}")
except ValueError:
    print("Erro: Você precisa digitar um número válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
print("\n")


# --- 4. O Bloco `else` ---
# O bloco `else` é opcional e é executado somente se o bloco `try`
# for concluído com sucesso, SEM gerar nenhuma exceção.

print("--- 4. O Bloco `else` ---")
try:
    idade_str = input("Digite sua idade: ")
    idade = int(idade_str)
except ValueError:
    print("Idade inválida. Por favor, insira apenas números.")
else:
    # Este código só roda se a conversão para int() deu certo.
    print(f"Sua idade de {idade} anos foi registrada com sucesso.")
    if idade >= 18:
        print("Você é maior de idade.")
print("\n")


# --- 5. O Bloco `finally` ---
# O bloco `finally` também é opcional e é SEMPRE executado,
# independentemente de ter ocorrido um erro ou não.
# É útil para tarefas de "limpeza", como fechar um arquivo ou conexão.

print("--- 5. O Bloco `finally` ---")
try:
    dados = {"valor": 100}
    print("Tentando acessar a chave 'valor'...")
    print(dados["valor"])
except KeyError:
    print("A chave não foi encontrada.")
finally:
    # Este bloco sempre será executado.
    print("Este é o bloco 'finally'. A verificação de dados foi concluída.")

