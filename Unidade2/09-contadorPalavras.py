# algoritmo para contar o número de palavras em uma string
# para simplificar, uma palavra é definida como uma sequência de caracteres que não contém espaços

frase = "He smiled a kind of sickly smile, and curled up on the floor, and the subsequent proceedings interested him no more."
contador = 1
for caractere in frase:
    if caractere == " ": # caractere é um espaço em branco
        contador += 1
print(contador)