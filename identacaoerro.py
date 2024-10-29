#  Deixe a indentação incorreta em um bloco de código e rode o programa. Para fins práticos, simule uma exceção de indentação manualmente em vez de executá-lo, já que IndentationError ocorre no momento da escrita.

try:
    if True:
    print("Indentação incorreta")  # Esta linha está incorretamente indentada
except IndentationError:
    print("Erro: indentação incorreta no código.")
