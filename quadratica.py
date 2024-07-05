import math
def quadratica(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta < 0:
        return "I"
    if delta >= 0:
        mais = (-b + math.sqrt(delta))/(2 * a)
        menos = (-b - math.sqrt(delta))/(2 * a)
        return mais, menos
a = float(input("Digite seu a: "))
b = float(input("Digite seu b: "))
c = float(input("Digite seu c: "))
if quadratica(a, b, c) == "I":
    print("SEM SOLUÇÃO")
else:
    mais,menos = quadratica(a, b, c)
    print("Primeira raiz: ", round(mais, 2))
    print("Segunda raiz: ", round(menos, 2))