# Crie uma lista com três elementos e tente acessar o quinto elemento dela. Trate o erro de índice.

try:
    lista = ["maçã", "banana", "laranja"]
    print(lista[4])
except IndexError:
    print("Erro: índice fora do intervalo da lista.")
