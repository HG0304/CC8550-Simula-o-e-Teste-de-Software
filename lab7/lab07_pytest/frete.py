"""Cálculo de frete corrigido e função esperada - Lab 07."""

def esperado(peso, urgencia, seguro, regiao):
    """
    Oráculo de cálculo do frete de acordo com a especificação:
    - Peso: leve R$10, médio R$20, pesado R$40
    - Região norte: + R$8
    - Urgência expressa: * 1.5
    - Seguro: + R$5 ao final
    """
    base = {"leve": 10.0, "medio": 20.0, "pesado": 40.0}[peso]
    if regiao == "norte":
        base += 8.0
    if urgencia == "expressa":
        base *= 1.5
    if seguro:
        base += 5.0
    return round(base, 2)


def frete(peso, urgencia, seguro, regiao):
    """
    Função de frete corrigida (sem a restrição incorreta de peso != 'leve'
    e sem o teto espúrio de 60).
    """
    base = {"leve": 10.0, "medio": 20.0, "pesado": 40.0}[peso]
    if regiao == "norte":
        base += 8.0
    if urgencia == "expressa":
        base *= 1.5
    if seguro:
        base += 5.0
    return round(base, 2)
