# -*- coding: utf-8 -*-

"""
Aula: O Laço `while` em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre o laço de repetição `while`.
Diferente do `for`, que itera sobre uma sequência, o `while` executa um bloco
de código repetidamente ENQUANTO uma determinada condição for verdadeira.
"""

# --- 1. Sintaxe Básica do `while` ---
# O laço `while` precisa de três partes:
# 1. Uma variável de controle inicializada.
# 2. A condição que será verificada a cada iteração.
# 3. Uma atualização da variável de controle dentro do laço para evitar um loop infinito.

print("--- 1. Sintaxe Básica (Contagem até 5) ---")
contador = 1
while contador <= 5:
    print(f"Número: {contador}")
    contador = contador + 1 # ou contador += 1
print("Laço finalizado.")
print("\n")


# --- 2. Usando `while` para Validação de Entrada ---
# O `while` é perfeito para continuar pedindo uma entrada do usuário
# até que ela seja válida.

print("--- 2. Validação de Entrada ---")
senha_correta = "python123"
senha_digitada = "" # Inicializa com um valor que não seja a senha correta

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta! Tente novamente.")

print("Acesso concedido!")
print("\n")


# --- 3. Processando Itens de uma Lista (e Dicionários) ---
# Você pode usar o `while` para percorrer e modificar uma lista.
# Isso é útil quando a condição de parada depende do conteúdo da lista.

print("--- 3. Processando uma Lista ---")
tarefas_pendentes = ["Lavar a louça", "Passear com o cachorro", "Estudar Python"]
print("Tarefas a fazer:", tarefas_pendentes)

while tarefas_pendentes: # O laço continua enquanto a lista não estiver vazia
    tarefa_atual = tarefas_pendentes.pop(0) # Pega e remove a primeira tarefa
    print(f"Realizando tarefa: {tarefa_atual}")

print("Todas as tarefas foram concluídas!")
print("\n")


# --- 4. `break` e `continue` no `while` ---
# Funcionam da mesma forma que no laço `for`.
# `break`: Interrompe o laço imediatamente.
# `continue`: Pula para a próxima verificação da condição.

print("--- 4. `break` e `continue` ---")
numero = 0
print("Exemplo com `continue` (pula o 5) e `break` (para no 8):")
while numero < 10:
    numero += 1
    if numero == 5:
        print("(Pulando o 5)")
        continue # Volta para o topo do laço
    if numero == 8:
        print("Parando no 8!")
        break # Sai do laço
    print(numero, end=" ")
print("\n\n")


# --- 5. O Bloco `else` no `while` ---
# Assim como no `for`, o `else` pode ser usado com `while`. O bloco `else`
# é executado quando a condição do laço se torna falsa (fim natural).
# Ele NÃO é executado se o laço for interrompido por um `break`.

print("--- 5. O Bloco `else` no `while` ---")
contagem_regressiva = 5
while contagem_regressiva > 0:
    print(contagem_regressiva, end=" ")
    contagem_regressiva -= 1
else:
    # Este bloco executa porque a condição (contagem_regressiva > 0) se tornou falsa.
    print("\nLançar!")
print("\n")


# --- 6. Cuidado com Laços Infinitos ---
# Se a condição do `while` nunca se tornar falsa, o programa ficará preso
# em um laço infinito. Certifique-se de que a variável de controle
# seja sempre atualizada de uma forma que eventualmente termine o laço.

# Exemplo de laço infinito (NÃO EXECUTE SEM SABER COMO PARAR: Ctrl+C no terminal)
# while True:
#     print("Estou preso em um laço!")
#     # Sem um 'break' ou mudança na condição, isso nunca para.

