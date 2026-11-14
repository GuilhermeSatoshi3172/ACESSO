from backend.app.database import conectar


# Relacionado a criação de usuário e endereço da loja, junto a funçõoes de atualização e remoção de usuário, endereço e loja.
def cria_usuario_loja(nome, senha_hash, email, telefone):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    id_tipo = 2
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, senha_hash, id_tipo)
            VALUES (%s, %s, %s)
            RETURNING id_usuario;
        """, (nome, senha_hash, id_tipo))

        id_usuario = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO dados_usuario (id_usuario, email, telefone)
            VALUES (%s, %s, %s);
        """, (id_usuario, email, telefone))
        connection.commit()

        return id_usuario

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cadastrar usuário: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def remove_usuario_loja(id_usuario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM usuarios
            WHERE id_usuario = %s;
        """, (id_usuario,))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover usuário da loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def endereco_loja(id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO endereco(id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento)
        VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s)
        """, (id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cadastrar endereço: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_endereco_loja(id_endereco, nome_rua, numero_rua, cidade, cep, estado, complemento):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE endereco
            SET nome_rua = %s,
                numero_rua = %s,
                cidade = %s,
                cep = %s,
                estado = %s,
                complemento = %s
            WHERE id_endereco = %s;
        """, (nome_rua, numero_rua, cidade, cep, estado, complemento, id_endereco))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao atualizar endereço da loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def cria_loja(id_usuario, nome_loja, cnpj, email_loja, telefone_loja, id_endereco):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO loja (id_usuario, nome_loja, cnpj, email_loja, telefone_loja, id_endereco)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_loja;
        """, (id_usuario, nome_loja, cnpj, email_loja, telefone_loja, id_endereco))
        id_loja = cursor.fetchone()[0]
        connection.commit()

        return id_loja

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cadastrar loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_dados_loja(id_loja, nome_loja, cnpj, email_loja, telefone_loja):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE loja
            SET nome_loja = %s,
                cnpj = %s,
                email_loja = %s,
                telefone_loja = %s
            WHERE id_loja = %s;
        """, (nome_loja, cnpj, email_loja, telefone_loja, id_loja))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao atualizar dados da loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def remove_loja(id_loja):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM loja
            WHERE id_loja = %s;
        """, (id_loja,))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()

#Relacionado a produtos, pedidos e estoque da loja, junto a funçõoes de atualização e remoção de produtos e pedidos.
def adiciona_produto(id_loja, nome_produto, id_categoria, descricao, preco, quantidade_estoque, unidade_medida, peso):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO produto (id_loja, nome_produto, id_categoria, descricao, preco, quantidade_estoque, unidade_medida, peso)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id_produto;
        """, (id_loja, nome_produto, id_categoria, descricao, preco, quantidade_estoque, unidade_medida, peso))
        id_produto = cursor.fetchone()[0]
        connection.commit()

        return id_produto

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao adicionar produto: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def lista_produtos_loja(id_loja):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM produto
            WHERE id_loja = %s;
        """, (id_loja,))
        produtos = cursor.fetchall()

        return produtos

    except Exception as erro:
        erro = print(f"Erro ao listar produtos da loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_produto(id_produto, nome_produto, id_categoria, descricao, preco, quantidade_estoque, unidade_medida, peso):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE produto
            SET nome_produto = %s,
                id_categoria = %s,
                descricao = %s,
                preco = %s,
                quantidade_estoque = %s,
                unidade_medida = %s,
                peso = %s
            WHERE id_produto = %s;
        """, (nome_produto, id_categoria, descricao, preco, quantidade_estoque, unidade_medida, peso, id_produto))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao atualizar produto: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_estoque_produto(id_produto, nova_quantidade):
    
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE produto
            SET quantidade_estoque = %s
            WHERE id_produto = %s;
        """, (nova_quantidade, id_produto))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao atualizar estoque do produto: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def remove_produto(id_produto):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM produto
            WHERE id_produto = %s;
        """, (id_produto,))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover produto: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def lista_pedidos_loja(id_loja):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM pedidos
            WHERE id_loja = %s;
        """, (id_loja,))
        pedidos = cursor.fetchall()

        return pedidos

    except Exception as erro:
        erro = print(f"Erro ao listar pedidos da loja: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def checa_pedido(id_loja, id_pedido):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM pedido
            WHERE id_loja = %s AND id_pedido = %s;
        """, (id_loja, id_pedido))
        pedido = cursor.fetchone()

        return pedido

    except Exception as erro:
        erro = print(f"Erro ao checar pedido: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_status_pedido(id_pedido, novo_status):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE pedido
            SET status_pedido = %s
            WHERE id_pedido = %s;
        """, (novo_status, id_pedido))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao atualizar status do pedido: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def cancela_pedido(id_loja, id_pedido):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE pedidos
            SET status_pedido = 'CANCELADO'
            WHERE id_loja = %s AND id_pedido = %s;
        """, (id_loja, id_pedido))
        connection.commit()

        return True

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cancelar pedido: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()
