import pytest
def imprimir_oi(nome):
    print(f'Oi, {nome}')  # Press Ctrl+F8 to toggle the breakpoint.


def somar(num1, num2):
    return num1 + num2


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não existe divisão por zero'


if __name__ == '__main__':
    imprimir_oi ('Letícia')


    resultado = somar(7,5)
    print(f'Resultado = {resultado}')

    # Escrevi isso no GITHub
    # Eu vi  - kkkkkkk
    # Mais um comentário escrito no GIT



