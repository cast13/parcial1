n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

if n>0:
    print("SI")

else:
    print("NO")
