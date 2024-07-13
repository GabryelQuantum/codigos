# verificar se uma substring está contida em uma string

palavra = "He smiled understandingly-much more than understandingly."
substring = "understand"
if substring in palavra:
    print("A substring está contida na string")
else:
    print("A substring não está contida na string")

# qual o código por trás do 'in'?

palavra = "Python"
substring = "tho"
for i in range(0, len(palavra)):
    if palavra[i:i+len(substring)] == substring:
        print("A substring está contida na string")
        break # serve para sair do for de forma antecipada

# | P | y | t | h | o | n |
# |-----------|
#     |-----------|
#         |-----------|