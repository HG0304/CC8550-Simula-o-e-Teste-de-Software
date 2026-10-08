def validar_nota(nota: float) -> bool:
    return 0.0 <= nota <= 10.0


def calcular_media(notas: list) -> float:
    if not notas:
        raise ValueError("lista de notas vazia")
    return sum(notas) / len(notas)


def obter_situacao(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"
