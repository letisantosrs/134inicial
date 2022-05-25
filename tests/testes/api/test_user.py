# Done: 1 - Criar um tste que adicione um usuário
# Done: 2 - Realizar o login e extrair o token da resposta

import json
import requests


url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token =''


def teste_incluir_usuario():
    # Configura
    # Dados de entrada
    # Virão do arquivo usuario1.json


    # Resultado esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '9531857'


    # executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\leticias.santos\\PycharmProjects\\134inicial\\vendors\\json\\usuario1.json')
    )


    # valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido ['message'] == mensagem_esperada


def teste_login():
    # Configura
    # Dados de entrada
    username = 'juca'
    password = 'bala'

    # Resultado esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])


    # Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get("message")
    print(f'A mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23:36] # [inicio:fim]
    print (f'O token = {token}')





