class Numero:
    """Representa um número guardado sempre em sua forma decimal."""

    def __init__(self, valor_decimal):
        self.valor_decimal = valor_decimal

    def __str__(self):
        return f"{self.valor_decimal}"

    def __repr__(self):
        return f"Numero(valor_decimal={self.valor_decimal})"
