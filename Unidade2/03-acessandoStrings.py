# em uma string, podemos acessar um caractere específico através de um índice
# atenção: o índice de uma string começa em 0

# exemplo:
# "Lua"[0] = "L"; "Lua"[1] = "u"; "Lua"[2] = "a"

palavra = "Lua"
primeiro = palavra[0] # acessando o primeiro caractere
ultimo = palavra[len(palavra) - 1] # acessando o último caractere
print(primeiro + ultimo) # "La"