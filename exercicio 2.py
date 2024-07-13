def funca(a, b, c):
    if a > b:
        if c > a:
            maior = c
        else: maior = a
    else:
        if c > b:
            maior = c
        else: maior = b
    return maior
a = float(input("Digite seu primeiro numero: "))
b = float(input("Digite seu segundo numero: "))
c = float(input("Digite seu terceiro numero: "))
j = funca(a, b, c)
print("Seu maior numero é: " + str(j))