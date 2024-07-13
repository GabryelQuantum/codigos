def funcao(a, b, c):
    if a == b == c:
        return 1
    else:
        return -1 
a = int(input("Digite seu primeiro numero: "))
b = int(input("Digite seu segundo numero: "))
c = int(input("Digite seu terceiro numero: "))
g = funcao(a, b, c)
print(g)