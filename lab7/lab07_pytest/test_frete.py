"""Testes de frete comparando pairwise e exaustivo - Lab 07."""
from itertools import product
from allpairspy import AllPairs
import pytest
from frete import frete, esperado

PARAMS_FRETE = [
    ["leve", "medio", "pesado"],
    ["normal", "expressa"],
    [False, True],
    ["sul", "sudeste", "norte"],
]

casos_pairwise = [list(c) for c in AllPairs(PARAMS_FRETE)]
casos_exaustivo = list(product(*PARAMS_FRETE))


@pytest.mark.parametrize("peso, urgencia, seguro, regiao", casos_pairwise)
def test_frete_pairwise(peso, urgencia, seguro, regiao):
    assert frete(peso, urgencia, seguro, regiao) == esperado(peso, urgencia, seguro, regiao)


@pytest.mark.parametrize("peso, urgencia, seguro, regiao", casos_exaustivo)
def test_frete_exaustivo(peso, urgencia, seguro, regiao):
    assert frete(peso, urgencia, seguro, regiao) == esperado(peso, urgencia, seguro, regiao)
