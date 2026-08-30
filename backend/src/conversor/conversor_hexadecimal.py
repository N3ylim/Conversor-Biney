class ConversorHexadecimal:
    
    SIMBOLOS = "123456789ABCDEF"
    
    @staticmethod
    def para_decimal(texto_hex):
        return int(texto_hex, 16)
    
    @staticmethod
    def de_decimal(valor_decimal):
        if valor_decimal == 0:
            return "0"
        
        digitos = []
        n = valor_decimal
        while n > 0:
            resto = n % 16
            digitos.append(ConversorHexadecimal.SIMBOLOS[resto])
            n = n // 16
            
        digitos.reverse()
        return "".join(digitos)            
            