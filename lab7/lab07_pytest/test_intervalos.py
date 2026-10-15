"""Testes baseados em propriedades com Hypothesis - Lab 07."""
import hypothesis.strategies as st
from hypothesis import given
from intervalos import mesclar, normalizar

estrategia_intervalos = st.lists(
    st.tuples(st.integers(0, 50), st.integers(0, 50))
).map(normalizar)


@given(estrategia_intervalos)
def test_propriedade_idempotencia(intervalos):
    """Propriedade 1: mesclar(mesclar(x)) == mesclar(x)."""
    uma_vez = mesclar(intervalos)
    duas_vezes = mesclar(uma_vez)
    assert uma_vez == duas_vezes


@given(estrategia_intervalos)
def test_propriedade_ordenado_e_sem_sobreposicao(intervalos):
    """Propriedade 2: O resultado é ordenado e nenhum intervalo sobrepõe o próximo."""
    resultado = mesclar(intervalos)
    for i in range(len(resultado) - 1):
        assert resultado[i][1] < resultado[i + 1][0]


@given(estrategia_intervalos)
def test_propriedade_cobertura_todos_intervalos_contidos(intervalos):
    """Propriedade 3: Todo intervalo original está contido em algum intervalo do resultado."""
    resultado = mesclar(intervalos)
    for ini, fim in intervalos:
        contido = any(r_ini <= ini and fim <= r_fim for r_ini, r_fim in resultado)
        assert contido is True
