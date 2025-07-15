print("exemplo de importação de um módulo padrão")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\n---  Exemplo de criação e utilização de módulo personalizado ---\n")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Gilberto")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")