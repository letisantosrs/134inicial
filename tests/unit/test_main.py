import pytest

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


# Lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]

@pytest.mark.parametrize('num1, num2, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(num1, num2, resultado_esperado):
    # 1 - configura
    # Utilizamos a lista como massa de teste, removendo deste trecho

    # 2 - Executa
    resultado_obtido = somar(num1, num2)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido