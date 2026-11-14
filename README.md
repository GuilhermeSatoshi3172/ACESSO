# ACESSO

Backend do projeto ACESSO.

## Estrutura atual

- `backend/app/repositories/`: acesso e operações com o banco de dados.
- Services e routes: em desenvolvimento por outro colaborador.

## Configuração

1. Instale as dependências: `pip install -r requirements.txt`.
2. Configure `DATABASE_URL` no arquivo `.env` com a conexão do banco.
3. Não inclua credenciais reais neste arquivo nem no controle de versão.

## Integração

A camada de services deve chamar as funções dos repositories. Antes da integração,
alinhe com os responsáveis os parâmetros, os valores retornados e como os erros
serão sinalizados.

## Status

Este README descreve apenas a camada de repositories; endpoints e regras de
negócio serão documentados quando estiverem implementados.