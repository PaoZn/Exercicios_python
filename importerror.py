# Tente importar um módulo que não existe e trate a exceção para avisar sobre a ausência do módulo.

try:
    import modulo_inexistente
except ImportError:
    print("Erro: o módulo solicitado não foi encontrado.")
