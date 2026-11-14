
from backend.app.database import conectar

# Relacionado a criação de usuário e endereço do cliente, junto a funçõoes de atualização e remoção de usuário, endereço e cliente.
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
        erro = print(f"Erro ao cadastrar usuário: {erro}")
        return erro

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
            WHERE id_carrinho = %s;
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


def adiciona_ic(id_carrinho, id_produto, quantidade_produto, preco_unitario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO item_carrinho(id_carrinho, id_prod, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
        RETURNING id_ic;
        """,(id_carrinho, id_produto, quantidade_produto, preco_unitario))

        id_ic = cursor.fetchone()[0]
        connection.commit()
        return id_ic

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao adicionar itens ao carrinho: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def remover_ic(id_carrinho, id_produto):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try: 
        cursor = connection.cursor()
        cursor.execute("""
        DELETE FROM item_carrinho
        WHERE id_carrinho = %s 
        AND id_prod = %s;
        """,(id_carrinho, id_produto))

        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover itens do carrinho: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def realiza_pedido(id_usuario, id_endereco, id_carrinho, id_loja, precoTotal, id_produto, quantidade, preco_unitario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try: 
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO pedidos(id_usuario, id_endereco, id_carrinho, id_loja, preco_total)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_pedido;
        """,(id_usuario, id_endereco, id_carrinho, id_loja, precoTotal))

        id_pedido = cursor.fetchone()[0]

        cursor.execute("""
            SELECT id_produto, quantidade, preco_unitario
            FROM item_carrinho
            WHERE id_carrinho = %s;
        """, (id_carrinho,))

        itens = cursor.fetchall()        

        for item in itens:
            id_produto, quantidade, preco_unitario = item

            cursor.execute("""
                INSERT INTO item_pedido
                (id_pedido, id_produto, quantidade, preco_unitario)
                VALUES (%s, %s, %s, %s)
                RETURNING id_item;
            """, (id_pedido, id_produto, quantidade, preco_unitario))

        id_item = cursor.fetchall()

        connection.commit()
        return id_pedido

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro finalizar pedido: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def cancela_pedido(id_pedido):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try: 
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE pedidos
        SET status_pedido = 'CANCELADO'
        WHERE id_pedido = %s;
        """, (id_pedido))

        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cancelar o pedido: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def atualiza_endereco(id_endereco, id_usuario, nome_rua, cidade, cep, estado, complemento):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try: 
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE endereco
        SET nome_rua = %s,
        cidade = %s,
        cep = %s,
        estado = %s,
        complemento = %s,
        WHERE id_endereco = %s,
        AND id_usuario = %s;
        """,(id_endereco, id_usuario, nome_rua, cidade, cep, estado, complemento))


    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao realizar essa ação: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def desativar_conta(id_usuario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try: 
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE usuarios
        SET status_conta = 'INATIVO' 
        WHERE id_usuario = %s;
        """, (id_usuario))

        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao realizar essa ação: {erro} ")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()



#função de teste de conexão com o banco de dados

# def mostra_cliente():
#     connection = conectar()

#     print(connection)
#     if connection is None:
#         return None

#     cursor = None

#     try:
#         cursor = connection.cursor()
#         cursor.execute("""SELECT * FROM usuarios""")

#         lista = cursor.fetchall()

#         return lista

#     except Exception as erro:
#         connection.rollback()
#         print(f"Erro ai: {erro}")
#         return None
    
# resultado = mostra_cliente()

# print(resultado)

