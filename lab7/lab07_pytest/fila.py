"""Fila circular com defeito corrigido - Lab 07 (Exercício 5)."""

class FilaCircular:
    def __init__(self, capacidade):
        self.itens = [None] * capacidade
        self.inicio = 0
        self.tamanho = 0

    def enfileirar(self, x):
        if self.tamanho == len(self.itens):
            raise OverflowError("fila cheia")
        # Correção: aplicar módulo para circular pelo vetor
        fim = (self.inicio + self.tamanho) % len(self.itens)
        self.itens[fim] = x
        self.tamanho += 1

    def desenfileirar(self):
        if self.tamanho == 0:
            raise IndexError("fila vazia")
        x = self.itens[self.inicio]
        self.inicio = (self.inicio + 1) % len(self.itens)
        self.tamanho -= 1
        return x
