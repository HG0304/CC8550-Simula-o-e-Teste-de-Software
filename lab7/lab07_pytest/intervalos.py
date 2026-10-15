"""Função de mesclar intervalos corrigida - Lab 07."""

def normalizar(intervalos):
    """Garante que cada intervalo esteja na forma (ini, fim) com ini <= fim."""
    return [(min(a, b), max(a, b)) for a, b in intervalos]


def mesclar(intervalos):
    """
    Une intervalos que se sobrepõem.
    Correção: usa max(resultado[-1][1], fim) para evitar encolher o intervalo
    quando o intervalo seguinte estiver contido no anterior.
    """
    resultado = []
    for ini, fim in sorted(intervalos):
        if resultado and ini <= resultado[-1][1]:
            resultado[-1] = (resultado[-1][0], max(resultado[-1][1], fim))
        else:
            resultado.append((ini, fim))
    return resultado
