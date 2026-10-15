"""Teste baseado em propriedades com oráculo deque para Fila Circular - Lab 07."""
from collections import deque
import hypothesis.strategies as st
from hypothesis import given
from fila import FilaCircular


@given(st.lists(st.integers(-1, 9), max_size=100))
def test_fila_circular_com_oraculo_deque(operacoes):
    """
    Testa a FilaCircular de capacidade 3 contra uma deque padrão.
    Valores >= 0 enfileiram; valor -1 desenfileira.
    Verifica comportamento, valores retornados, tamanho e exceções.
    """
    capacidade = 3
    fila = FilaCircular(capacidade)
    oraculo = deque()

    for op in operacoes:
        if op >= 0:
            if len(oraculo) == capacidade:
                # Fila deve estar cheia
                try:
                    fila.enfileirar(op)
                    assert False, "Deveria ter levantado OverflowError"
                except OverflowError:
                    pass
            else:
                fila.enfileirar(op)
                oraculo.append(op)
        else:
            # op == -1 -> desenfileirar
            if len(oraculo) == 0:
                # Fila deve estar vazia
                try:
                    fila.desenfileirar()
                    assert False, "Deveria ter levantado IndexError"
                except IndexError:
                    pass
            else:
                item_fila = fila.desenfileirar()
                item_oraculo = oraculo.popleft()
                assert item_fila == item_oraculo

        assert fila.tamanho == len(oraculo)
