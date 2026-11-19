from decimal import Decimal, InvalidOperation

import bcrypt


def texto_obrigatorio(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} é obrigatório.")
    return valor.strip()


def identificador_obrigatorio(valor, campo):
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise ValueError(f"{campo} é obrigatório.")
    return valor


def numero_nao_negativo(valor, campo):
    try:
        numero = Decimal(str(valor))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{campo} deve ser numérico.") from None

    if not numero.is_finite() or numero < 0:
        raise ValueError(f"{campo} deve ser maior ou igual a zero.")
    return numero


def numero_positivo(valor, campo):
    numero = numero_nao_negativo(valor, campo)
    if numero == 0:
        raise ValueError(f"{campo} deve ser maior que zero.")
    return numero


def gerar_hash_senha(senha):
    senha = texto_obrigatorio(senha, "Senha")
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("ascii")
