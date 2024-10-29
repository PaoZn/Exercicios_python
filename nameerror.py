# Tente acessar uma variável que não foi definida anteriormente no código. Trate a exceção para avisar que a variável não existe

try:
    print(minha_variavel)
except NameError:
    print("Erro: variável 'minha_variavel' não foi definida.")
