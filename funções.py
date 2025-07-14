# -*- coding: utf-8 -*-

"""
Aula: Funções em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre funções. Funções são blocos
de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a
organizar o código, evitar repetição e torná-lo mais legível.
"""

# --- 1. Definindo e Chamando uma Função Simples ---
# Uma função é definida com a palavra-chave `def`, seguida pelo nome da função
# e parênteses (). O código da função é indentado.

print("--- 1. Definindo e Chamando uma Função ---")

def exibir_saudacao():
    """Esta é uma docstring. Ela explica o que a função faz."""
    print("Olá! Bem-vindo ao estudo de funções em Python.")

# Para executar o código dentro da função, você precisa "chamá-la".
exibir_saudacao()
print("\n")


# --- 2. Parâmetros e Argumentos ---
# Você pode passar informações para uma função através de parâmetros.
# Parâmetros são as variáveis listadas dentro dos parênteses na definição.
# Argumentos são os valores que você envia para a função ao chamá-la.

print("--- 2. Parâmetros e Argumentos ---")

def saudacao_personalizada(nome): # 'nome' é um parâmetro
    print(f"Olá, {nome}! Tudo bem?")

saudacao_personalizada("Ana") # "Ana" é um argumento
saudacao_personalizada("Marcos") # "Marcos" é um argumento
print("\n")


# --- 3. O Comando `return` ---
# Funções podem processar dados e "retornar" um resultado.
# O comando `return` envia um valor de volta para onde a função foi chamada.

print("--- 3. O Comando `return` ---")

def somar(a, b):
    resultado = a + b
    return resultado

# O valor retornado pode ser armazenado em uma variável.
valor_da_soma = somar(10, 5)
print(f"O resultado da soma é: {valor_da_soma}")
print(f"Você também pode usar o retorno diretamente: {somar(3, 2)}")

# Uma função sem `return` explicitamente retorna `None`.
retorno_da_saudacao = saudacao_personalizada("Lucas")
print(f"O retorno da função de saudação é: {retorno_da_saudacao}")
print("\n")


# --- 4. Parâmetros com Valores Padrão ---
# Você pode definir um valor padrão para um parâmetro. Se nenhum argumento
# for passado para ele, o valor padrão será usado.

print("--- 4. Parâmetros com Valores Padrão ---")

def calcular_potencia(base, expoente=2):
    return base ** expoente

# Chamando sem o segundo argumento (usa o padrão expoente=2)
quadrado = calcular_potencia(10)
print(f"10 ao quadrado é: {quadrado}")

# Chamando com ambos os argumentos
cubo = calcular_potencia(3, 3)
print(f"3 ao cubo é: {cubo}")
print("\n")


# --- 5. Argumentos Nomeados (Keyword Arguments) ---
# Você pode especificar para qual parâmetro cada argumento se destina.
# Isso torna a chamada da função mais clara e a ordem dos argumentos não importa.

print("--- 5. Argumentos Nomeados ---")

def descrever_pet(tipo_animal, nome_animal):
    print(f"Eu tenho um {tipo_animal} chamado {nome_animal}.")

# Chamando com argumentos nomeados
descrever_pet(nome_animal="Rex", tipo_animal="cachorro")
print("\n")


# --- 6. Usando Funções com Dicionários ---
# Funções são excelentes para manipular dicionários.

print("--- 6. Usando Funções com Dicionários ---")

def exibir_info_usuario(usuario_dict):
    """Recebe um dicionário de usuário e exibe suas informações."""
    print("Informações do Usuário:")
    for chave, valor in usuario_dict.items():
        print(f"- {chave.capitalize()}: {valor}")

usuario = {
    "username": "bia_silva",
    "nome_completo": "Beatriz Silva",
    "ativo": True
}
exibir_info_usuario(usuario)


def criar_usuario(nome, email, cidade):
    """Cria e retorna um dicionário de usuário com base nos parâmetros."""
    novo_usuario = {
        "nome": nome,
        "email": email,
        "cidade": cidade
    }
    return novo_usuario

usuario_criado = criar_usuario("Pedro", "pedro@email.com", "Rio de Janeiro")
print("\nNovo usuário criado:")
print(usuario_criado)
print("\n")


# --- 7. Escopo de Variáveis (Local vs. Global) ---
# Variáveis criadas dentro de uma função (escopo local) só existem dentro dela.
# Variáveis criadas fora de qualquer função (escopo global) podem ser acessadas
# de qualquer lugar, mas não devem ser modificadas dentro de uma função
# sem usar a palavra-chave `global` (o que geralmente não é uma boa prática).

print("--- 7. Escopo de Variáveis ---")
variavel_global = "Eu sou global"

def minha_funcao_de_escopo():
    variavel_local = "Eu sou local"
    print(f"Dentro da função, posso ver a variável local: '{variavel_local}'")
    print(f"Dentro da função, também posso ver a variável global: '{variavel_global}'")

minha_funcao_de_escopo()

print(f"\nFora da função, posso ver a variável global: '{variavel_global}'")
try:
    # A linha abaixo vai gerar um erro (NameError)
    print(f"Fora da função, não posso ver a variável local: '{variavel_local}'")
except NameError as e:
    print(f"ERRO: {e}")

