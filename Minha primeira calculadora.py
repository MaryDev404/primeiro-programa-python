while True:
    print("\n -- Calculadora Básica ---")
    print("Escolha um a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
     print("")
     num1 = float(input("Digite o primeiro número: "))
     num2 = float(input("Digite o segundo número: "))
     soma = num1 + num2
     resultado = soma
     print("O resultado da soma dos números é: ",resultado)
    elif opcao == 2:
       print("")
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       subtracao = num1 - num2
       resultado = subtracao
       print("O resultado da subtração dos números é: ",resultado)
    elif opcao == 3:
       print("")
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       multiplicacao = num1 * num2
       resultado = multiplicacao
       print("O resultado da multilicação dos números é: ",resultado)
    elif opcao == 4:
       print("")
       num1 = float(input("Digite o primeiro número: "))
       num2 = float(input("Digite o segundo número: "))
       divisao = num1 / num2
       resultado = divisao
       print("O resultado da divisão dos números é: ",resultado)
    elif opcao == 5:
       print("")
       print("Programa encerrado! Obrigado por usar!")
       break