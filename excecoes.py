# --- CÓDIGO DE EXEMPLO COM TRATAMENTO DE EXCEÇÕES ---

def dividir_numeros():
    """
    Esta função pede dois números ao usuário e realiza a divisão,
    tratando possíveis erros de entrada e de matemática.
    """
    print("--- Calculadora de Divisão Segura ---")

    try:
        # Bloco TRY: Tentamos executar este código "arriscado".
        # O Python vai monitorar esta seção em busca de erros.
        numerador_str = input("Digite o primeiro número (numerador): ")
        numerador = float(numerador_str)  # Esta linha pode gerar um ValueError

        denominador_str = input("Digite o segundo número (denominador): ")
        denominador = float(denominador_str)  # Esta linha também pode gerar um ValueError

        resultado = numerador / denominador  # Esta linha pode gerar um ZeroDivisionError

    except ValueError:
        # Bloco EXCEPT para um erro específico: ValueError.
        # Ele é executado se o usuário digitar um texto (ex: "dez") que não pode
        # ser convertido para um número pela função float().
        print("\n[ERRO] Você digitou um valor inválido. Por favor, insira apenas números.")

    except ZeroDivisionError:
        # Bloco EXCEPT para outro erro específico: ZeroDivisionError.
        # Ele é executado se o usuário tentar dividir por zero (denominador = 0).
        print("\n[ERRO] Não é possível dividir um número por zero.")

    except Exception as e:
        # Bloco EXCEPT genérico: É uma "rede de segurança" que captura
        # qualquer outro tipo de erro que não previmos.
        # A variável 'e' contém a mensagem de erro original do Python, o que ajuda a depurar.
        print(f"\n[ERRO INESPERADO] Ocorreu um problema: {e}")

    else:
        # Bloco ELSE: Este código só é executado se o bloco 'try' for
        # concluído com sucesso, sem gerar nenhuma exceção.
        # É o lugar ideal para colocar o código que depende do sucesso da operação.
        print(f"\n[SUCESSO] O resultado da divisão é: {resultado}")

    finally:
        # Bloco FINALLY: Este código é executado SEMPRE, não importa o que aconteça.
        # É perfeito para ações de "limpeza", como fechar um arquivo ou
        # simplesmente para indicar que a operação terminou.
        print("\n--- Fim da tentativa de cálculo. ---")


# Vamos chamar a função para que ela seja executada quando rodarmos o script.
dividir_numeros()
