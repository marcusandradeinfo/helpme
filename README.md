# help-me
Projeto próprio para gerenciamento de Chamados de TI

# Sobre o Sistema 
O Sistema Help-me é um sistema de gerenciamento de chamados que permite ao usuário realizar o controle de chamados de TI indicando o técnico responsável para o atendimento. 

## Objetivo
Ter ums sistema que consiga gerenciar não somente os chamados de ti como também os clientes e os técnicos, podendo categorizar os chamados e os técnicos por nível de atendimneto.

## Tecnologias
- Python 3.11

- Django 5.2.3
- Django RestFramework
- Autenticacao via JWT
- PostgreSQL
- Docker

## Como utilizar Sistema:
O sistema encontra-se dentro do domínio www.marcusandradeinfo.com.br/helpme.
Ao realizar o acesso ao sistema você pode efetuar o login as credenciais abaixo:
usuario: visitante
senha: 123@Mudar

## API de consulta de Chamados:

No sistema existe uma API de consulta de Chamados que o Usuário pode consultar todos os chamados abertos:

Para verificar o funcionamento da API basta realizar um POST para:

https://www.marcusandradeinfo.com.br/api/v1/authentication/token/

Passando no corpo da requisição as credencias de autenticação do sistema:

{
    "username":"visitante",
    "password":"123@Mudar"
}



Isso retornará um token que deverá ser informado como bearer token na requisição de GET no endereço abaixo para o endereço abaixo:


https://www.marcusandradeinfo.com.br)/api/v1/chamados/

Isso retornará os dados dos chamados abertos.



#Versão
1.0.0
