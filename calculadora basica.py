
num1 = float(input("insira o primeiro numero: "))
num2 = float(input("insira o segundo numero: "))
operacao = (input("insira o sinal: "))

if operacao == '+':
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

elif operacao == '-':
    resultado = num1 - num2 
    print("o resultado da subtração é:", resultado)

elif operacao == '/':
    resultado = num1 / num2
    print("o rsultado da divisao é:", resultado)

elif operacao == '*':
    resultado = num1 * num2
    print("o resultado da multiplicação é:", resultado)

else:
    print("Operação inválida")