numeroUser = int(input("ingrese un numero: "))

contador = 1

while numeroUser > 9:
    numeroUser = numeroUser // 10
    contador += 1
    

print(contador)