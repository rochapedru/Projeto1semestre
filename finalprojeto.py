def octal_para_decimal(numero_octal):
    decimal = 0
    expoente = 0
    while numero_octal != 0:
        digito = numero_octal % 10
        decimal += digito * (8 ** expoente)
        expoente += 1
        numero_octal //= 10
    return decimal
while True:
    print("Menu:")
    print("1. Binario para Decimal")
    print("2. Hexadecimal para Decimal")
    print("3. Octadecimal para Decimal")
    print("4. Componentes do Grupo")
    print("5.Disciplinas Envolvidas")
    print("6.Versão do aplicaivo")
    print("7.Curso")
    print("8. Exit")
    print("9. Documentacao")
    
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
        # A CONVERSOR ESTA LA EM CIMA NO COMECO DO PROGRAMA AQUI É SO O PRINT
        numero_octal = int(input("Digite um número octal: "))
        decimal = octal_para_decimal(numero_octal)
        print(f"O número decimal equivalente é: {decimal}")
    elif choice =="4":
        print("Componentes do Grupo" )
        print("Joao Pedro Oliveira Rocha, Davi araujo")
        
    
    elif choice == "5":
        print("Disciplinas envolvidas")
        print("Organização e Arquitetura de Computadores e Programação de Computadores")
    elif choice =="6":
        print("Versão do Aplicativo")
        print("A versão do aplicativo é 1.0")
    elif choice =="7":
        print(" Curso de Análise e Desenvolvimento de sistemas ")
        
    elif choice =="9":
        print("A documentacao está no Github")
        print("https://github.com/rochapedru/Projeto1semestre")
    elif choice == '8':
        print("Saindo...")
        break
    else:
        print("Opcao Inválida.")