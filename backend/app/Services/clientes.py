from backend.app.repositories import repositorio_clientes

from ._validacao import (
    gerar_hash_senha,
    identificador_obrigatorio,
    numero_positivo,
    texto_obrigatorio,
)


def cadastrar_cliente(nome, senha, email, telefone):
    return repositorio_clientes.cria_cliente(
        texto_obrigatorio(nome, "Nome"),
        gerar_hash_senha(senha),
        texto_obrigatorio(email, "E-mail"),
        texto_obrigatorio(telefone, "Telefone"),
    )


def cadastrar_endereco(
    id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento=None
):
    return repositorio_clientes.endereco_cliente(
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        texto_obrigatorio(nome_rua, "Rua"),
        texto_obrigatorio(str(numero_rua), "Número"),
        texto_obrigatorio(cidade, "Cidade"),
        texto_obrigatorio(cep, "CEP"),
        texto_obrigatorio(estado, "Estado"),
        complemento.strip() if isinstance(complemento, str) else complemento,
    )


def obter_itens_carrinho(id_carrinho):
    return repositorio_clientes.carrinho_cliente(
        identificador_obrigatorio(id_carrinho, "ID do carrinho")
    )


def adicionar_item_carrinho(id_carrinho, id_produto, quantidade, preco_unitario):
    return repositorio_clientes.adiciona_ic(
        identificador_obrigatorio(id_carrinho, "ID do carrinho"),
        identificador_obrigatorio(id_produto, "ID do produto"),
        numero_positivo(quantidade, "Quantidade"),
        numero_positivo(preco_unitario, "Preço unitário"),
    )


def remover_item_carrinho(id_carrinho, id_produto):
    return repositorio_clientes.remover_ic(
        identificador_obrigatorio(id_carrinho, "ID do carrinho"),
        identificador_obrigatorio(id_produto, "ID do produto"),
    )


def finalizar_pedido(
    id_usuario,
    id_endereco,
    id_carrinho,
    id_loja,
    preco_total_calculado,
    id_produto=None,
    quantidade=None,
    preco_unitario=None,
):
    return repositorio_clientes.realiza_pedido(
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        identificador_obrigatorio(id_endereco, "ID do endereço"),
        identificador_obrigatorio(id_carrinho, "ID do carrinho"),
        identificador_obrigatorio(id_loja, "ID da loja"),
        numero_positivo(preco_total_calculado, "Total do pedido"),
        id_produto,
        quantidade,
        preco_unitario,
    )


def cancelar_pedido(id_pedido):
    return repositorio_clientes.cancela_pedido(
        identificador_obrigatorio(id_pedido, "ID do pedido")
    )


def atualizar_endereco(
    id_endereco, id_usuario, nome_rua, cidade, cep, estado, complemento=None
):
    return repositorio_clientes.atualiza_endereco(
        identificador_obrigatorio(id_endereco, "ID do endereço"),
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        texto_obrigatorio(nome_rua, "Rua"),
        texto_obrigatorio(cidade, "Cidade"),
        texto_obrigatorio(cep, "CEP"),
        texto_obrigatorio(estado, "Estado"),
        complemento.strip() if isinstance(complemento, str) else complemento,
    )


def desativar_conta(id_usuario):
    return repositorio_clientes.desativar_conta(
        identificador_obrigatorio(id_usuario, "ID do usuário")
    )
