# Tente concatenar uma string com um número em uma operação de soma. Use o try-except para tratar a exceção.

try:
    resultado = "O número é: " + 5
    print(resultado)
except TypeError:
    print("Erro: não é possível concatenar string com um número.")
