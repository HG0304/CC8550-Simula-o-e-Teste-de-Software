from typing import List, Tuple, Any


def classificar_por_faixas(valor: float, faixas: List[Tuple[float, str]], rotulo_padrao: str = "") -> str:
    """
    Classifica um valor numérico em faixas pré-definidas.
    faixas: lista ordenada de tuplas (limite_superior, rotulo).
    Se valor < limite_superior, retorna o respectivo rotulo.
    Caso não caia em nenhuma faixa, retorna rotulo_padrao.
    """
    for limite, rotulo in faixas:
        if valor < limite:
            return rotulo
    return rotulo_padrao


FAIXAS_IMC = [
    (18.5, "abaixo do peso"),
    (25.0, "peso normal"),
    (30.0, "sobrepeso"),
]

FAIXAS_VENTO = [
    (20.0, "calmo"),
    (40.0, "moderado"),
    (60.0, "forte"),
]


def categorizar_imc(imc: float) -> str:
    """Classifica o valor do IMC utilizando a função genérica."""
    return classificar_por_faixas(imc, FAIXAS_IMC, rotulo_padrao="obesidade")


def classificar_vento(velocidade: float) -> str:
    """Classifica a velocidade do vento utilizando a função genérica."""
    return classificar_por_faixas(velocidade, FAIXAS_VENTO, rotulo_padrao="tempestade")


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula o IMC: peso / (altura ** 2).
    Exercício 2: Levanta ValueError se peso ou altura não forem positivos (> 0).
    """
    if peso <= 0 or altura <= 0:
        raise ValueError("peso e altura devem ser valores positivos")
    return peso / (altura ** 2)


def classificar_pessoa(peso: float, altura: float) -> str:
    """Calcula o IMC e retorna sua respectiva classificação textual."""
    imc = calcular_imc(peso, altura)
    return categorizar_imc(imc)


def tem_frete_gratis(valor_compra: float, cliente_premium: bool, peso: float) -> bool:
    """
    Regra de negócio do Exercício 4:
    Frete grátis apenas se:
    - valor_compra >= 200
    - cliente_premium is True
    - peso <= 30
    """
    return (valor_compra >= 200.0) and bool(cliente_premium) and (peso <= 30.0)
