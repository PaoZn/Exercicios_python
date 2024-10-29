# Tente usar um método inexistente em uma string, como append. Trate o erro de atributo.

try:
    texto = "Olá, mundo!"
    texto.append("!")  # append não é um método válido para strings
except AttributeError:
    print("Erro: método inexistente para o tipo de dado.")
