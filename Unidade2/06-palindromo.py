# algoritmo para verificar se uma string é um palíndromo
# conhecimento: acessar strings com índice, concatenar strings

palavra = "arara"
palavraInvertida = ""
i = len(palavra) - 1
while i >= 0:
    palavraInvertida += palavra[i] # construir a string do fim para o início
    i -= 1 # mesma coisa que i = i - 1

if palavra == palavraInvertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")