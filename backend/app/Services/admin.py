from backend.app.repositories import repositorio_admin

from ._validacao import gerar_hash_senha, identificador_obrigatorio, texto_obrigatorio


def cadastrar_admin(id_usuario, nome, senha, email, telefone):
    return repositorio_admin.cria_admin(
        identificador_obrigatorio(id_usuario, "ID do usuário"),
        texto_obrigatorio(nome, "Nome"),
        gerar_hash_senha(senha),
        texto_obrigatorio(email, "E-mail"),
        texto_obrigatorio(telefone, "Telefone"),
    )


def listar_usuarios():
    return repositorio_admin.lista_usuarios()


def listar_lojas():
    return repositorio_admin.lista_lojas()


def remover_usuario(id_usuario):
    return repositorio_admin.remove_usuario(
        identificador_obrigatorio(id_usuario, "ID do usuário")
    )


def remover_loja(id_loja):
    return repositorio_admin.remove_loja(
        identificador_obrigatorio(id_loja, "ID da loja")
    )


def remover_produto(id_produto):
    return repositorio_admin.remove_produto(
        identificador_obrigatorio(id_produto, "ID do produto")
    )
