# Tente abrir um arquivo que não existe. Trate o erro de arquivo não encontrado

try:
    with open("arquivo_inexistente.txt", "r") as file:
        conteudo = file.read()
except FileNotFoundError:
    print("Erro: o arquivo solicitado não foi encontrado.")
