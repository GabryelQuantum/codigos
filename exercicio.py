n = -5
while n <= 0:
    n = int(input("Quantos numeros serao digitados?: "))
maior = 0
primeiravez = True
for i in range (0, n):
    j = int(input("Digite qualquer numero: "))
    if primeiravez:
        maior = j
        primeiravez = False
        continue
    maior = max(j, maior)
print(maior)