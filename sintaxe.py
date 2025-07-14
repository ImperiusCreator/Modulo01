# -*- coding: utf-8 -*-

"""
Este é um exemplo de um script Python que demonstra a sintaxe básica.
Comentários de múltiplas linhas (docstrings) como este são úteis para
descrever o propósito geral de um módulo ou função.
"""

# --- 1. Variáveis e Tipos de Dados ---

# Em Python, você não precisa declarar o tipo de uma variável.
# O interpretador infere o tipo com base no valor atribuído.

# Inteiro (int)
idade = 30
print("--- Variáveis e Tipos de Dados ---")
print("Idade (Inteiro):", idade)

# Ponto Flutuante (float)
altura = 1.75
print("Altura (Ponto Flutuante):", altura)

# String (str) - pode usar aspas simples ou duplas
nome = "Maria"
sobrenome = 'Silva'
print("Nome Completo (String):", nome, sobrenome)

# Booleano (bool) - True ou False (com a primeira letra maiúscula)
e_estudante = True
print("É estudante? (Booleano):", e_estudante)

# NoneType (None) - representa a ausência de valor
valor_nulo = None
print("Valor Nulo (NoneType):", valor_nulo)
print("\n") # Imprime uma linha em branco para separar as seções


# --- 2. Operadores ---

# Operadores Aritméticos
soma = 10 + 5       # Adição
subtracao = 10 - 5  # Subtração
multiplicacao = 10 * 5 # Multiplicação
divisao = 10 / 5      # Divisão (resulta em float)
divisao_inteira = 10 // 3 # Divisão inteira (descarta a parte decimal)
exponenciacao = 2 ** 3  # Potência (2 elevado a 3)
modulo = 10 % 3       # Resto da divisão

print("--- Operadores ---")
print("Soma (10 + 5):", soma)
print("Divisão (10 / 5):", divisao)
print("Divisão Inteira (10 // 3):", divisao_inteira)
print("Módulo (10 % 3):", modulo)
print("\n")


# --- 3. Estruturas de Dados ---

# Listas (list) - mutáveis, ordenadas, permitem duplicados
frutas = ["maçã", "banana", "laranja"]
print("--- Estruturas de Dados ---")
print("Lista de frutas inicial:", frutas)
# Acessando um item pelo índice (começa em 0)
print("Primeira fruta:", frutas[0])
# Adicionando um item ao final da lista
frutas.append("uva")
print("Lista após adicionar 'uva':", frutas)

# Dicionários (dict) - coleção de pares chave-valor, mutáveis
pessoa = {
    "nome": "Carlos",
    "idade": 42,
    "cidade": "São Paulo"
}
print("\nDicionário 'pessoa':", pessoa)
# Acessando um valor pela chave
print("Idade de Carlos:", pessoa["idade"])
# Adicionando um novo par chave-valor
pessoa["profissao"] = "Engenheiro"
print("Dicionário após adicionar profissão:", pessoa)
print("\n")


# --- 4. Controle de Fluxo (Condicionais) ---

# A indentação (espaços no início da linha) é crucial em Python.
# Ela define os blocos de código.
print("--- Controle de Fluxo (if/elif/else) ---")
temperatura = 25

if temperatura > 30:
    print("Está muito quente!")
elif temperatura > 20: # 'elif' é a contração de 'else if'
    print("O tempo está agradável.")
else:
    print("Está frio, pegue um casaco.")
print("\n")


# --- 5. Laços de Repetição (Loops) ---

# Laço 'for' - para iterar sobre uma sequência (como uma lista)
print("--- Laços de Repetição ---")
print("Iterando sobre a lista de frutas com 'for':")
for fruta in frutas:
    print("-", fruta)

# Laço 'for' com a função range()
print("\nContando de 0 a 4 com 'for' e 'range(5)':")
for i in range(5):
    print(i)

# Laço 'while' - executa enquanto uma condição for verdadeira
print("\nContagem regressiva com 'while':")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1 # Equivalente a: contador = contador - 1
print("Fogo!")
print("\n")


# --- 6. Funções ---

# Funções são definidas com a palavra-chave 'def'
print("--- Funções ---")

def saudacao(nome_da_pessoa):
    """Esta função recebe um nome e imprime uma saudação."""
    return f"Olá, {nome_da_pessoa}! Bem-vindo(a)."

# Chamando a função e imprimindo o resultado
mensagem_saudacao = saudacao("Ana")
print(mensagem_saudacao)

# Função com parâmetros padrão
def potencia(base, expoente=2):
    """Calcula a potência de um número. O expoente padrão é 2."""
    return base ** expoente

print("Potência com expoente padrão (5^2):", potencia(5))
print("Potência com expoente definido (3^4):", potencia(3, 4))
print("\n")


# --- 7. Entrada do Usuário ---

# A função input() lê uma linha da entrada (teclado),
# convertendo-a para uma string.
print("--- Entrada do Usuário ---")
nome_usuario = input("Por favor, dig