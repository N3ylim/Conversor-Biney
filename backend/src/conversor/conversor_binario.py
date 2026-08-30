class ConversorBinario:

    @staticmethod
    def para_decimal(texto_binario):
        return int(texto_binario, 2)

    @staticmethod
    def de_decimal(valor_decimal):
        if valor_decimal == 0:
            return "0"

        digitos = []
        n = valor_decimal
        while n > 0:
            resto = n % 2
            digitos.append(str(resto))
            n = n // 2

        digitos.reverse()
        return "".join(digitos)