# substrings são partes menores de uma string
# por exemplo, a string "Python" possui algumas substrings, como "Py", "on", "tho"...

# para acessar uma substring, utilizamos a notação de slice
# slice: [começo:fim]
# começo: índice do primeiro caractere da substring
# fim: índice do último caractere da substring + 1, pois é exclusivo

palavra = "Python"
substring = palavra[0:2] # "Py"
print(substring)