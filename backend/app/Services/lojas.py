from backend.app.repositories import repositorio_lojas

from ._validacao import (
    gerar_hash_senha,
    identificador_obrigatorio,
    numero_nao_negativo,
    numero_positivo,
    texto_obrigatorio,
)


def cadastrar_usuario_loja(nome, senha, email, telefone):
    return repositorio_lojas.cria_usuario_loja(
        texto_obrigatorio(nome, "Nome"),
        gerar_hash_senha(senha),
        texto_obrigatorio(email, "E-mail"),
        texto_obrigatorio(telefone, "Telefone"),
    )


def remover_usuario_loja(id_usuario):
    return repositorio_lojas.remove_usuario_loja(
        identificador_obrigatorio(id_usuario, "ID do usuário")
    )


def cadastrar_endereco_loja(
    id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento=None
):
    return repositorio_lojas.endereco_loja(
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        texto_obrigatorio(nome_rua, "Rua"),
        texto_obrigatorio(str(numero_rua), "Número"),
        texto_obrigatorio(cidade, "Cidade"),
        texto_obrigatorio(cep, "CEP"),
        texto_obrigatorio(estado, "Estado"),
        complemento.strip() if isinstance(complemento, str) else complemento,
    )


def atualizar_endereco_loja(
    id_endereco, nome_rua, numero_rua, cidade, cep, estado, complemento=None
):
    return repositorio_lojas.atualiza_endereco_loja(
        identificador_obrigatorio(id_endereco, "ID do endereço"),
        texto_obrigatorio(nome_rua, "Rua"),
        texto_obrigatorio(str(numero_rua), "Número"),
        texto_obrigatorio(cidade, "Cidade"),
        texto_obrigatorio(cep, "CEP"),
        texto_obrigatorio(estado, "Estado"),
        complemento.strip() if isinstance(complemento, str) else complemento,
    )


def cadastrar_loja(
    id_usuario, nome_loja, cnpj, email_loja, telefone_loja, id_endereco
):
    return repositorio_lojas.cria_loja(
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        texto_obrigatorio(nome_loja, "Nome da loja"),
        texto_obrigatorio(cnpj, "CNPJ"),
        texto_obrigatorio(email_loja, "E-mail da loja"),
        texto_obrigatorio(telefone_loja, "Telefone da loja"),
        identificador_obrigatorio(id_endereco, "ID do endereço"),
    )


def atualizar_dados_loja(id_loja, nome_loja, cnpj, email_loja, telefone_loja):
    return repositorio_lojas.atualiza_dados_loja(
        identificador_obrigatorio(id_loja, "ID da loja"),
        texto_obrigatorio(nome_loja, "Nome da loja"),
        texto_obrigatorio(cnpj, "CNPJ"),
        texto_obrigatorio(email_loja, "E-mail da loja"),
        texto_obrigatorio(telefone_loja, "Telefone da loja"),
    )


def remover_loja(id_loja):
    return repositorio_lojas.remove_loja(
        identificador_obrigatorio(id_loja, "ID da loja")
    )


def adicionar_produto(
    id_loja,
    nome_produto,
    id_categoria,
    descricao,
    preco,
    quantidade_estoque,
    unidade_medida,
    peso,
):
    return repositorio_lojas.adiciona_produto(
        identificador_obrigatorio(id_loja, "ID da loja"),
        texto_obrigatorio(nome_produto, "Nome do produto"),
        identificador_obrigatorio(id_categoria, "ID da categoria"),
        descricao.strip() if isinstance(descricao, str) else descricao,
        numero_positivo(preco, "Preço"),
        numero_nao_negativo(quantidade_estoque, "Estoque"),
        texto_obrigatorio(unidade_medida, "Unidade de medida"),
        numero_nao_negativo(peso, "Peso"),
    )


def listar_produtos(id_loja):
    return repositorio_lojas.lista_produtos_loja(
        identificador_obrigatorio(id_loja, "ID da loja")
    )


def atualizar_produto(
    id_produto,
    nome_produto,
    id_categoria,
    descricao,
    preco,
    quantidade_estoque,
    unidade_medida,
    peso,
):
    return repositorio_lojas.atualiza_produto(
        identificador_obrigatorio(id_produto, "ID do produto"),
        texto_obrigatorio(nome_produto, "Nome do produto"),
        identificador_obrigatorio(id_categoria, "ID da categoria"),
        descricao.strip() if isinstance(descricao, str) else descricao,
        numero_positivo(preco, "Preço"),
        numero_nao_negativo(quantidade_estoque, "Estoque"),
        texto_obrigatorio(unidade_medida, "Unidade de medida"),
        numero_nao_negativo(peso, "Peso"),
    )


def atualizar_estoque(id_produto, nova_quantidade):
    return repositorio_lojas.atualiza_estoque_produto(
        identificador_obrigatorio(id_produto, "ID do produto"),
        numero_nao_negativo(nova_quantidade, "Estoque"),
    )


def remover_produto(id_produto):
    return repositorio_lojas.remove_produto(
        identificador_obrigatorio(id_produto, "ID do produto")
    )


def listar_pedidos(id_loja):
    return repositorio_lojas.lista_pedidos_loja(
        identificador_obrigatorio(id_loja, "ID da loja")
    )


def obter_pedido(id_loja, id_pedido):
    return repositorio_lojas.checa_pedido(
        identificador_obrigatorio(id_loja, "ID da loja"),
        identificador_obrigatorio(id_pedido, "ID do pedido"),
    )


def atualizar_status_pedido(id_pedido, novo_status):
    return repositorio_lojas.atualiza_status_pedido(
        identificador_obrigatorio(id_pedido, "ID do pedido"),
        texto_obrigatorio(novo_status, "Status"),
    )


def cancelar_pedido(id_loja, id_pedido):
    return repositorio_lojas.cancela_pedido(
        identificador_obrigatorio(id_loja, "ID da loja"),
        identificador_obrigatorio(id_pedido, "ID do pedido"),
    )
