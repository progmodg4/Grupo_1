import time
from auth import *

test_username = 'Teste ' + time.ctime()

def test_cadastro_sucesso():
  assert cadastro_login(test_username, 'abc') == { 'status': 'success', 'message': 'Cadastro realizado com sucesso.'}

def test_cadastro_erro():
  assert cadastro_login(test_username, 'abc') == { 'status': 'error', 'message': 'Usuário já existente.'}

def test_login_sucesso():
  assert verifica_login(test_username, 'abc') == {'status': 'success', 'message': 'Login realizado com sucesso.'}

def test_login_erro():
  assert verifica_login(test_username, 'abcd') == {'status': 'error', 'message': 'Usuário ou senha inválidos.'}