import pytest
from sistema_notas import validar_nota, calcular_media, obter_situacao


def test_validar_nota_limite_inferior():
    assert validar_nota(0) is True


def test_validar_nota_limite_superior():
    assert validar_nota(10) is True


def test_validar_nota_valor_medio_valido():
    assert validar_nota(7.5) is True


def test_validar_nota_abaixo_do_limite():
    assert validar_nota(-0.1) is False


def test_validar_nota_acima_do_limite():
    assert validar_nota(10.1) is False


def test_calcular_media_valores_padrao():
    assert calcular_media([6, 8, 10]) == 8.0

# Exercício 2: Lista vazia

def test_calcular_media_lista_vazia():
    """Verifica se lista vazia levanta ValueError com a mensagem exata especificada."""
    with pytest.raises(ValueError, match="lista de notas vazia"):
        calcular_media([])

# Exercício 3: Fixture notas_exemplo

def test_media_turma_a(notas_exemplo):
    assert calcular_media(notas_exemplo) == 7


def test_media_turma_b(notas_exemplo):
    assert obter_situacao(calcular_media(notas_exemplo)) == "Aprovado"

# Exercício 4: Parametrize e casos limites

@pytest.mark.parametrize(
    "media, situacao_esperada",
    [
        (10.0, "Aprovado"),
        (7.0, "Aprovado"),       # Limite exato: antes falhava na função original (> 7)
        (6.5, "Recuperacao"),
        (5.0, "Recuperacao"),    # Limite exato: antes falhava na função original (> 5)
        (4.9, "Reprovado"),
        (0.0, "Reprovado"),
    ],
)
def test_obter_situacao_parametrizado(media, situacao_esperada):
    assert obter_situacao(media) == situacao_esperada

# Exercício 5: Independência dos Testes

def test_matricula_aluno():
    turma = []
    turma.append("Ana")
    assert len(turma) == 1


def test_matricula_outro_aluno():
    turma = []
    turma.append("Bruno")
    assert len(turma) == 1
