# Crie um dicionário com informações de uma pessoa, como nome e idade, e tente acessar a chave endereco que não existe no dicionário. Trate o erro de chave.

try:
    pessoa = {"nome": "Carlos", "idade": 30}
    print("Endereço:", pessoa["endereco"])
except KeyError:
    print("Erro: chave 'endereco' não encontrada no dicionário.")
