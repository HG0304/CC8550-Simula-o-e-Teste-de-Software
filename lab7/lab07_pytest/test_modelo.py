"""Testes para o Exercício 1 - Lab 07."""
from itertools import product
from allpairspy import AllPairs
from modelo import PARAMS, pares_de


def test_quantidade_pairwise_allpairspy():
    """Gera o conjunto pairwise com allpairspy e verifica que possui entre 9 e 15 casos."""
    casos = [list(c) for c in AllPairs(PARAMS)]
    # O mínimo teórico é 3 x 3 = 9 casos. O allpairspy costuma gerar entre 10 e 13 casos.
    assert len(casos) >= 9
    assert len(casos) <= 15


def test_cobertura_completa_pares():
    """Confirma que o conjunto pairwise cobre todos os pares do produto cartesiano completo."""
    produto_completo = list(product(*PARAMS))
    universo_pares = pares_de(produto_completo)

    casos_pw = [list(c) for c in AllPairs(PARAMS)]
    pares_cobertos = pares_de(casos_pw)

    assert pares_cobertos == universo_pares


def test_verificador_detecta_pares_descobertos_com_poucos_casos():
    """Com apenas 3 casos, o verificador deve apontar que faltam pares a serem cobertos."""
    produto_completo = list(product(*PARAMS))
    universo_pares = pares_de(produto_completo)

    casos_pw = [list(c) for c in AllPairs(PARAMS)]
    amostra_incompleta = casos_pw[:3]

    pares_amostra = pares_de(amostra_incompleta)
    pares_faltantes = universo_pares - pares_amostra

    assert len(pares_faltantes) > 0
