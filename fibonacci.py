n = int(input("Digite quantos numeros quer em sua sequencia: "))
def F(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)
for i in range(0, n):
    g = F(i)
    print(g)