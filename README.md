# ACESSO

Backend do projeto ACESSO.

## Estrutura atual

- `backend/app/repositories/`: acesso e operações com o banco de dados.
- `backend/app/services/`: validação básica e regras de negócio que chamam os repositories.
- Routes: ainda não implementadas.

## Configuração

1. Instale as dependências: `pip install -r requirements.txt`.
2. Configure `DATABASE_URL` no arquivo `.env` com a conexão do banco.
3. Não inclua credenciais reais neste arquivo nem no controle de versão.

## Integração

Os services usam os parâmetros definidos nos repositories e retornam seus resultados.
Configure `DATABASE_URL` com a connection string PostgreSQL do Supabase. O arquivo
`.env` não deve ser preenchido com credenciais reais no controle de versão.

Antes de publicar endpoints, revise o esquema real do Supabase e padronize o
tratamento de erros e os retornos dos repositories. No momento, alguns repositories
convertem erros em `None` e há divergências nos nomes de tabelas/colunas, que podem
impedir operações específicas. O total do pedido também deve ser calculado no
backend, nunca aceito diretamente do navegador.

## Status

Este README descreve apenas a camada de repositories; endpoints e regras de
negócio serão documentados quando estiverem implementados.