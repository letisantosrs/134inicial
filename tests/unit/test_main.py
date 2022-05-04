from main import somar, dividir

def teste_somar():
    # 1 - configura
    num1 = 8
    num2 = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(num1, num2)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido


def teste_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de entrada
    num1 = 27
    num2 = 3

    # 1.2 - Resultado esperado
    resultado_esperado = 9


    # 2 - Executa
    resultado_obtido = dividir(num1, num2)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def teste_dividir_negativo():
        # 1 - Configura
        # 1.1 - Dados de entrada
        num1 = 27
        num2 = 0

        # 1.2 - Resultado esperado
        resultado_esperado = 'Não existe divisão por zero'

        # 2 - Executa
        resultado_obtido = dividir(num1, num2)

        # 3 - Valida
        assert resultado_obtido == resultado_esperado