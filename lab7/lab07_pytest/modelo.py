"""Parâmetros e funções de conferência pairwise - Lab 07 (CC8550)."""
from itertools import combinations

PARAMS = [
    ["Correios", "Jadlog", "Loggi"],
    ["caixa", "envelope", "tubo"],
    ["com seguro", "sem seguro"],
    ["normal", "expressa", "agendada"],
]


def pares_de(casos):
    """
    Retorna o conjunto de pares de valores cobertos por uma lista de casos.
    Identifica cada valor por (índice_parâmetro, valor) para evitar colisões
    entre valores iguais de parâmetros distintos.
    """
    pares = set()
    for caso in casos:
        for p1, p2 in combinations(enumerate(caso), 2):
            pares.add((p1, p2))
    return pares
