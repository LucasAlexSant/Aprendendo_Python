while True:
    numero = int(input("Informe um núemero: "))

    if numero == 100:
        break
    print(numero)

for numero in range(100):
     if numero == 10:
        break
     
     print(numero)
        
for numero in range(100):
     if numero % 2 == 0:
        continue
     
     print(numero)