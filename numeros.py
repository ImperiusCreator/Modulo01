# -*- coding: utf-8 -*-

"""
Aula: Números em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre os tipos de dados numéricos
em Python. Ele explora inteiros (int), números de ponto flutuante (float),
as operações que podemos realizar com eles e funções úteis.
"""

# --- 1. Tipos de Números ---
# Python lida principalmente com dois tipos de números:
# - Inteiros (int): Números completos, sem parte decimal.
# - Ponto Flutuante (float): Números que contêm uma parte decimal.

# Exemplo de Inteiro (int)
populacao_cidade = 150000

# Exemplo de Ponto Flutuante (float)
pi = 3.14159
preco_do_item = 19.99

print("--- Tipos de Números ---")
print(f"População (int): {populacao_cidade} - Tipo: {type(populacao_cidade)}")
print(f"Valor de PI (float): {pi} - Tipo: {type(pi)}")
print("\n")


# --- 2. Operadores Aritméticos ---
# São os símbolos que usamos para realizar cálculos matemáticos.

a = 10
b = 3

soma = a + b            # Adição
subtracao = a - b       # Subtração
multiplicacao = a * b   # Multiplicação
divisao = a / b         # Divisão (sempre retorna um float)
divisao_inteira = a // b  # Divisão inteira (descarta a parte decimal)
modulo = a % b          # Módulo (retorna o resto da divisão)
exponenciacao = a ** b    # Potência (a elevado a b)

print("--- Operadores Aritméticos (usando a=10, b=3) ---")
print(f"Soma (a + b): {soma}")
print(f"Subtração (a - b): {subtracao}")
print(f"Multiplicação (a * b): {multiplicacao}")
print(f"Divisão (a / b): {divisao}")
print(f"Divisão Inteira (a // b): {divisao_inteira}")
print(f"Módulo (a % b): {modulo}")
print(f"Exponenciação (a ** b): {exponenciacao}")
print("\n")


# --- 3. Ordem das Operações (Precedência) ---
# Python segue a ordem matemática padrão (PEMDAS/BODMAS):
# 1. Parênteses ()
# 2. Expoentes **
# 3. Multiplicação *, Divisão /, Divisão Inteira //, Módulo %
# 4. Adição +, Subtração -

resultado = 5 + 2 * 3  # Primeiro 2 * 3 = 6, depois 5 + 6 = 11
resultado_com_parenteses = (5 + 2) * 3 # Primeiro 5 + 2 = 7, depois 7 * 3 = 21

print("--- Ordem das Operações ---")
print(f"Resultado de 5 + 2 * 3: {resultado}")
print(f"Resultado de (5 + 2) * 3: {resultado_com_parenteses}")
print("\n")


# --- 4. Conversão de Tipos (Type Casting) ---
# Às vezes, você precisa converter um número de um tipo para outro.

numero_float = 5.8
numero_int = 10

# Convertendo float para int (a parte decimal é truncada, não arredondada)
float_para_int = int(numero_float)

# Convertendo int para float
int_para_float = float(numero_int)

print("--- Conversão de Tipos ---")
print(f"Float {numero_float} convertido para int: {float_para_int}")
print(f"Int {numero_int} convertido para float: {int_para_float}")
print("\n")


# --- 5. Funções Numéricas Embutidas (Built-in) ---
# Python oferece algumas funções úteis para trabalhar com números.

# abs(): Retorna o valor absoluto (remove o sinal negativo)
valor_absoluto = abs(-150)

# round(): Arredonda um número para o inteiro mais próximo ou para um
# número específico de casas decimais.
numero_arredondado_int = round(3.7)
numero_arredondado_float = round(3.14159, 2) # Arredonda para 2 casas decimais

# max() e min(): Retornam o maior e o menor valor de uma sequência.
maior_valor = max(5, 12, 3, 99)
menor_valor = min(5, 12, 3, 99)

print("--- Funções Embutidas ---")
print(f"Valor absoluto de -150: {valor_absoluto}")
print(f"3.7 arredondado: {numero_arredondado_int}")
print(f"3.14159 arredondado para 2 casas: {numero_arredondado_float}")
print(f"Maior valor entre (5, 12, 3, 99): {maior_valor}")
print(f"Menor valor entre (5, 12, 3, 99): {menor_valor}")
print("\n")


# --- 6. O Módulo `math` ---
# Para funções matemáticas mais avançadas, precisamos importar o módulo `math`.

import math

# Raiz quadrada
raiz_quadrada = math.sqrt(81)

# Pi (uma constante mais precisa)
pi_preciso = math.pi

# Seno (o argumento é em radianos)
seno_de_90_graus = math.sin(math.pi / 2)

# Fatorial
fatorial_de_5 = math.factorial(5)

print("--- Módulo `math` ---")
print(f"Raiz quadrada de 81: {raiz_quadrada}")
print(f"Valor de Pi do módulo math: {pi_preciso}")
print(f"Seno de 90 graus (pi/2): {seno_de_90_graus}")
print(f"Fatorial de 5 (5!): {fatorial_de_5}")

