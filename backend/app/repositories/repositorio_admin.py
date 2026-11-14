
from backend.app.database import conectar


def cria_admin(id_usuario, nome, senha_hash, email, telefone):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    id_tipo = 3
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO usuarios (id_usuario, nome, senha_hash, id_tipo)
            VALUES (%s, %s, %s, %s);
        """, (id_usuario, nome, senha_hash, id_tipo))

        cursor.execute("""
            INSERT INTO dados_usuario (id_usuario, email, telefone)
            VALUES (%s, %s, %s);
        """, (id_usuario, email, telefone))
        connection.commit()

        return id_usuario

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao cadastrar usuário administrador: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def lista_usuarios():
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT u.id_usuario, u.nome, u.id_tipo, d.email, d.telefone
            FROM usuarios u
            JOIN dados_usuario d ON u.id_usuario = d.id_usuario;
        """)
        usuarios = cursor.fetchall()
        return usuarios

    except Exception as erro:
        erro = print(f"Erro ao listar usuários: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def lista_lojas():
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT l.id_loja, u.nome, d.email, d.telefone
            FROM lojas l
            JOIN usuarios u ON l.id_usuario = u.id_usuario
            JOIN dados_usuario d ON u.id_usuario = d.id_usuario;
        """)
        lojas = cursor.fetchall()
        return lojas

    except Exception as erro:
        erro = print(f"Erro ao listar lojas: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()


def remove_usuario(id_usuario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM dados_usuario WHERE id_usuario = %s;
        """, (id_usuario,))
        cursor.execute("""
            DELETE FROM usuarios WHERE id_usuario = %s;
        """, (id_usuario,))
        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover usuário: {erro}")
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
            DELETE FROM loja WHERE id_loja = %s;
        """, (id_loja,))
        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover loja: {erro}")
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
            DELETE FROM produtos WHERE id_prod = %s;
        """, (id_produto,))
        connection.commit()

    except Exception as erro:
        connection.rollback()
        erro = print(f"Erro ao remover produto: {erro}")
        return erro

    finally:
        if cursor:
            cursor.close()
        connection.close()

