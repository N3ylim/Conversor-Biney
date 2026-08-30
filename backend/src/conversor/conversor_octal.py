class ConversorOctal:
    
    @staticmethod
    def para_decimal(texto_octal):
        return int(texto_octal, 8)
    
    @staticmethod 
    def de_decimal(valor_decimal):
        if valor_decimal == 0:
            return "0"
        
        digitos = []
        n = valor_decimal
        while n > 0:
            resto = n % 8
            digitos.append(str(resto))
            n = n // 8
        
        digitos.reverse()
        return "".join(digitos)