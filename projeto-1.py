while True:
    print("Menu:")
    print("1. Binario para Decimal")
    print("2. Hexadecimal para Decimal")
    print("3. Octadecimal para Decimal")
    print("4. Exit")
    choice = input("Escolha uma opção: ")
    if choice == '1':
        binario = input("Insira binário inteiro ou quebrado: ")
        decimal = 0
        binary_str = str(binario)
        if "." in binary_str:
            
            integer_part, fractional_part = binary_str.split(".")
            for i in range(len(integer_part)):
                digito = int(integer_part[-(i+1)])
                decimal += digito * 2**i
            for i in range(len(fractional_part)):
                digito = int(fractional_part[i])
                decimal += digito * 2**(-(i+1))
        else:
            for i in range(len(binary_str)):
                digito = int(binary_str[-(i+1)])
                decimal += digito * 2**i
        print("O decimal é: ", decimal)

    elif choice == '2':
        hex_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        hexadecimal = input("iNSIRA Hex inteiro ou quebrado: ")
        decimal = 0
        if '.' in hexadecimal:
            integer_part, fractional_part = hexadecimal.split('.')
            potencia = len(integer_part) - 1
            for digito in integer_part:
                decimal += hex_table[digito] * (16 ** potencia)
                potencia -= 1

            potencia = -1
            for digito in fractional_part:
                decimal += hex_table[digito] * (16 ** potencia)
                potencia -= 1
        else:
            potencia = len(hexadecimal) - 1
            for digito in hexadecimal:
                decimal += hex_table[digito] * (16 ** potencia)
                potencia -= 1
        print("O Hexadecimal:", hexadecimal, "é: ", decimal)


    elif choice == '3':
        octal = input("Octal quebrado ou inteiro, insira ")
        decimal = 0
        integer_part, fractional_part = octal.split('.')
        potencia = len(integer_part) - 1
        for digito in integer_part:
            decimal += int(digito) * (8 ** potencia) 
            potencia -= 1
            
        potencia = 1
        for digito in fractional_part:
            decimal += int(digito) * (8 ** -potencia)
            potencia += 1
                
        print("O octal", octal, "em decimal é", decimal)
    elif choice == '4':
        print("Saindo...")
        break
    else:
        print("Opcao Inválida.")


