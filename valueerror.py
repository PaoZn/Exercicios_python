#Crie um programa que peça ao usuário para inserir um número inteiro. Caso o usuário insira um valor que não seja um número, mostre uma mensagem de erro.

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número digitado:", numero)
except ValueError:
    print("Erro: valor inválido, por favor insira um número inteiro.")
