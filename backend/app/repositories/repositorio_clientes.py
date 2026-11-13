
from database import conectar


def cria_cliente(nome, senha_hash, email, telefone):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    id_tipo = 1
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, senha_hash, id_tipo)
            VALUES (%s, %s, %s)
            RETURNING id_usuario;
        """, (nome, senha_hash, id_tipo))

        id_usuario = cursor.fetchone()[0]

        cursor.execute("""
        INSERT INTO carrinho(id_usuario, status_carrinho)
        VALUES (%s, 'ATIVO')
        RETURNING id_carrinho;
        """,(id_usuario))
        id_carrinho = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO dados_usuario (id_usuario, email, telefone)
            VALUES (%s, %s, %s);
        """, (id_usuario, email, telefone))
        connection.commit()

        return id_usuario, id_carrinho

    except Exception as erro:
        connection.rollback()
        print(f"Erro ao cadastrar usuário: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()


def endereco_cliente(id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO endereco(id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento)
        VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s)
        RETURNING id_endereco;
        """, (id_usuario, nome_rua, numero_rua, cidade, cep, estado, complemento))
        id_endereco = cursor.fetchone()[0]
        connection.commit()
        return id_endereco
    
    except Exception as erro:
        connection.rollback()
        print(f"Erro ao cadastrar endereço: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()


def carrinho_cliente(id_carrinho):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM item_carrinho
            WHERE id_carrinho = %s
        """, (id_carrinho,))

        itens = cursor.fetchall()
        return itens

    except Exception as erro:
        connection.rollback()
        print(f"Erro ao buscar itens do carrinho: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()


def adiciona_carrinho(id_carrinho, id_produto, quantidade_produto, preco_unitario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO item_carrinho(id_carrinho, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
        RETURNING id_ic;
        """,(id_carrinho, id_produto, quantidade_produto, preco_unitario))

        id_ic = cursor.fetchone()[0]
        connection.commit()
        return id_ic

