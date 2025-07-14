# -*- coding: utf-8 -*-

"""
Aula: Dicionários em Python - Um Guia Completo

Este script é um guia de estudo detalhado sobre dicionários (dict).
Dicionários são coleções não ordenadas*, mutáveis e que armazenam dados
no formato de pares chave-valor.

*A partir do Python 3.7, os dicionários mantêm a ordem de inserção,
mas é uma boa prática não depender dessa característica para compatibilidade.
"""

# --- 1. Criando Dicionários ---
# Um dicionário é criado com chaves {} e os pares chave:valor são
# separados por vírgulas. As chaves devem ser únicas e de um tipo imutável
# (como string, número ou tupla).

aluno = {
    "nome": "Carlos",
    "idade": 22,
    "curso": "Engenharia de Software",
    "ativo": True
}
dicionario_vazio = {}

print("--- 1. Criando Dicionários ---")
print("Dicionário 'aluno':", aluno)
print("Dicionário Vazio:", dicionario_vazio)
print("\n")


# --- 2. Acessando Itens ---
# Você acessa um valor através de sua chave correspondente.

nome_do_aluno = aluno["nome"]
idade_do_aluno = aluno["idade"]

# Usar o método .get() é mais seguro, pois não gera um erro se a chave
# não existir. Em vez disso, retorna None ou um valor padrão que você definir.
curso_do_aluno = aluno.get("curso")
nota_do_aluno = aluno.get("nota", "Nota não cadastrada") # Valor padrão

print("--- 2. Acessando Itens ---")
print("Nome do aluno (usando colchetes):", nome_do_aluno)
print("Curso do aluno (usando .get()):", curso_do_aluno)
print("Nota do aluno (usando .get() com padrão):", nota_do_aluno)
print("\n")


# --- 3. Modificando Dicionários ---
# Dicionários são mutáveis. Você pode adicionar, alterar e remover pares chave-valor.

print("--- 3. Modificando Dicionários ---")
print("Dicionário original:", aluno)

# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print("Após adicionar a cidade:", aluno)

# Alterando um valor existente
aluno["idade"] = 23
print("Após alterar a idade:", aluno)

# Removendo um par com 'pop' (remove e retorna o valor)
curso_removido = aluno.pop("curso")
print(f"Após remover o curso (curso removido: '{curso_removido}'):", aluno)

# Removendo um par com 'del'
del aluno["ativo"]
print("Após remover a chave 'ativo' com 'del':", aluno)
print("\n")


# --- 4. Iterando sobre Dicionários ---
# Você pode percorrer as chaves, os valores ou os pares chave-valor.

print("--- 4. Iterando sobre Dicionários ---")

# Iterando sobre as chaves (comportamento padrão)
print("\nIterando sobre as chaves:")
for chave in aluno:
    print(f"- Chave: {chave}, Valor: {aluno[chave]}")

# Iterando sobre os valores com .values()
print("\nIterando sobre os valores:")
for valor in aluno.values():
    print(f"- {valor}")

# Iterando sobre os pares chave-valor com .items() (forma mais comum)
print("\nIterando sobre os itens (chave, valor):")
for chave, valor in aluno.items():
    print(f"- {chave}: {valor}")
print("\n")


# --- 5. Métodos e Funções Úteis ---
print("--- 5. Métodos e Funções Úteis ---")
# .keys(): Retorna uma visão das chaves do dicionário
chaves = aluno.keys()
print("Visão das chaves (.keys()):", chaves)

# .values(): Retorna uma visão dos valores
valores = aluno.values()
print("Visão dos valores (.values()):", valores)

# .items(): Retorna uma visão dos pares (chave, valor)
itens = aluno.items()
print("Visão dos itens (.items()):", itens)

# len(): Retorna o número de pares chave-valor
print("Tamanho do dicionário (len):", len(aluno))
print("\n")


# --- 6. Dicionários Aninhados ---
# Você pode ter dicionários como valores dentro de outro dicionário.

usuarios = {
    "usuario1": {
        "nome": "Ana",
        "email": "ana@exemplo.com"
    },
    "usuario2": {
        "nome": "Bruno",
        "email": "bruno@exemplo.com"
    }
}

print("--- 6. Dicionários Aninhados ---")
print("Dicionário de usuários:", usuarios)

# Acessando um dado aninhado
email_da_ana = usuarios["usuario1"]["email"]
print("Email do usuário 1:", email_da_ana)

