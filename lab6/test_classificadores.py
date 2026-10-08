"""Suíte de testes de Caixa-Preta (Partição de Equivalência, Valor-Limite e Tabela de Decisão)."""
import pytest
from classificadores import (
    calcular_imc,
    categorizar_imc,
    classificar_pessoa,
    classificar_vento,
    tem_frete_gratis,
)


# ==============================================================================
# Exercício 1: IMC - Classes de Equivalência Válidas
# 1 representante para cada uma das 4 partições válidas
# ==============================================================================

def test_classificar_pessoa_abaixo_do_peso():
    # IMC: 50 / (1.80^2) ≈ 15.43 (< 18.5)
    assert classificar_pessoa(50.0, 1.80) == "abaixo do peso"


def test_classificar_pessoa_peso_normal():
    # IMC: 70 / (1.75^2) ≈ 22.86 (18.5 <= IMC < 25)
    assert classificar_pessoa(70.0, 1.75) == "peso normal"


def test_classificar_pessoa_sobrepeso():
    # IMC: 85 / (1.75^2) ≈ 27.76 (25 <= IMC < 30)
    assert classificar_pessoa(85.0, 1.75) == "sobrepeso"


def test_classificar_pessoa_obesidade():
    # IMC: 110 / (1.75^2) ≈ 35.92 (>= 30)
    assert classificar_pessoa(110.0, 1.75) == "obesidade"


# ==============================================================================
# Exercício 2: Análise do Valor-Limite (Fronteiras 18.5, 25.0 e 30.0) e Entradas Inválidas
# ==============================================================================

@pytest.mark.parametrize(
    "imc, resultado_esperado",
    [
        (18.4, "abaixo do peso"),  # Imediatamente abaixo da fronteira 18.5
        (18.5, "peso normal"),     # Fronteira exata 18.5
        (24.9, "peso normal"),     # Imediatamente abaixo da fronteira 25.0
        (25.0, "sobrepeso"),       # Fronteira exata 25.0
        (29.9, "sobrepeso"),       # Imediatamente abaixo da fronteira 30.0
        (30.0, "obesidade"),       # Fronteira exata 30.0
    ],
    ids=[
        "fronteira_18_5_abaixo",
        "fronteira_18_5_exato",
        "fronteira_25_0_abaixo",
        "fronteira_25_0_exato",
        "fronteira_30_0_abaixo",
        "fronteira_30_0_exato",
    ],
)
def test_categorizar_imc_valores_limite(imc, resultado_esperado):
    assert categorizar_imc(imc) == resultado_esperado


def test_calcular_imc_peso_invalido_lanca_excecao():
    with pytest.raises(ValueError, match="peso e altura devem ser valores positivos"):
        calcular_imc(0.0, 1.75)


def test_calcular_imc_altura_invalida_lanca_excecao():
    with pytest.raises(ValueError, match="peso e altura devem ser valores positivos"):
        calcular_imc(70.0, -1.75)


# ==============================================================================
# Exercício 3: Classificação de Vento (Classes e Fronteiras 20, 40 e 60)
# ==============================================================================

@pytest.mark.parametrize(
    "velocidade, categoria_esperada",
    [
        (10.0, "calmo"),       # Classe Calmo
        (19.9, "calmo"),       # Limite inferior fronteira 20
        (20.0, "moderado"),    # Limite exato fronteira 20
        (30.0, "moderado"),    # Classe Moderado
        (39.9, "moderado"),    # Limite inferior fronteira 40
        (40.0, "forte"),       # Limite exato fronteira 40
        (50.0, "forte"),       # Classe Forte
        (59.9, "forte"),       # Limite inferior fronteira 60
        (60.0, "tempestade"),  # Limite exato fronteira 60
        (80.0, "tempestade"),  # Classe Tempestade
    ],
    ids=[
        "classe_calmo",
        "limite_20_abaixo",
        "limite_20_exato",
        "classe_moderado",
        "limite_40_abaixo",
        "limite_40_exato",
        "classe_forte",
        "limite_60_abaixo",
        "limite_60_exato",
        "classe_tempestade",
    ],
)
def test_classificar_vento(velocidade, categoria_esperada):
    assert classificar_vento(velocidade) == categoria_esperada


# ==============================================================================
# Exercício 4: Tabela de Decisão Completa (8 Regras R1 a R8)
# C1: valor >= 200 | C2: premium == True | C3: peso <= 30
# ==============================================================================

@pytest.mark.parametrize(
    "valor, premium, peso, frete_gratis",
    [
        (250.0, True, 20.0, True),    # R1: V, V, V -> True
        (250.0, True, 35.0, False),   # R2: V, V, F -> False
        (250.0, False, 20.0, False),  # R3: V, F, V -> False
        (250.0, False, 35.0, False),  # R4: V, F, F -> False
        (150.0, True, 20.0, False),   # R5: F, V, V -> False
        (150.0, True, 35.0, False),   # R6: F, V, F -> False
        (150.0, False, 20.0, False),  # R7: F, F, V -> False
        (150.0, False, 35.0, False),  # R8: F, F, F -> False
    ],
    ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"],
)
def test_tabela_decisao_frete_completa(valor, premium, peso, frete_gratis):
    assert tem_frete_gratis(valor, premium, peso) == frete_gratis
