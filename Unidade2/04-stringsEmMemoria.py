# strings são armazenadas como uma sequência de caracteres em memória
# | L | u | c | a | s | T | o | z | o |

Nome = "Maracujá"
for caractere in Nome:
    endereco = hex(id(caractere)) # obtém o endereço de memória do caractere
    print(caractere + " - " + endereco)