# Crie um programa que peça ao usuário dois números e tente dividi-los. Caso o divisor seja zero, trate a exceção com uma mensagem informando que divisão por zero não é permitida.

try:
    numerador = float(input("Digite o numerador: "))
    divisor = float(input("Digite o divisor: "))
    resultado = numerador / divisor
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
