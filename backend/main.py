from src.conversor.numero_base import Numero
from src.conversor.conversor_binario import ConversorBinario
from src.conversor.conversor_octal import ConversorOctal
from src.conversor.conversor_hexadecimal import ConversorHexadecimal


def main():
    while True:
        print()
        print("=== Conversor de Números ===")
        print("1 - Binário")
        print("2 - Octal")
        print("3 - Decimal")
        print("4 - Hexadecimal")
        print("5 - Sair")

        opcao = input("Escolha a base do número que você vai digitar: ")

        if opcao == "5":
            print("Encerrando o programa...")
            break

        if opcao == "1":
            texto = input("Digite o número binário: ")
            valor_decimal = ConversorBinario.para_decimal(texto)
        elif opcao == "2":
            texto = input("Digite o número octal: ")
            valor_decimal = ConversorOctal.para_decimal(texto)
        elif opcao == "3":
            texto = input("Digite o número decimal: ")
            valor_decimal = int(texto)
        elif opcao == "4":
            texto = input("Digite o número hexadecimal: ")
            valor_decimal = ConversorHexadecimal.para_decimal(texto)
        else:
            print("Opção inválida, tente novamente")
            continue

        numero = Numero(valor_decimal)

        print()
        print("=== Resultado ===")
        print(f"Decimal:     {numero.valor_decimal}")
        print(f"Binário:     {ConversorBinario.de_decimal(numero.valor_decimal)}")
        print(f"Octal:       {ConversorOctal.de_decimal(numero.valor_decimal)}")
        print(f"Hexadecimal: {ConversorHexadecimal.de_decimal(numero.valor_decimal)}")


if __name__ == "__main__":
    main()
