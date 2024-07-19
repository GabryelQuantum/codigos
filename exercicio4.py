def fatorial(x):
    if x < 0:
        return "Sem fatorial!"
    else:
        for i in range(1, x):
            x = x*i
        return x
x = int(input("Digite seu x: "))
g = fatorial(x)
print(g)
