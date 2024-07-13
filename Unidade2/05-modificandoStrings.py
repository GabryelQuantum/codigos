# strings são imutáveis, ou seja, não podemos modificar o valor de um caractere em uma string
# para modificar uma string, precisamos criar uma nova string

# exemplo:
# remover todos os espaços de uma string

original = "Eu amo programar"
modificado = ""
for caractere in original:
    if caractere != " ":
        modificado += caractere # concatenação de strings
print(modificado) # Euamoprogramar