import random

# Definindo a matriz simétrica (x=y)
x = int(input("Ordem do array: "))
matriz = [[0] * x for t in range(x)]

# colocando valores aleatórios ela percorrendo normalmente
for i in range(len(matriz)):
    for j in range(len(matriz)):
        n_aleatorio = random.randint(0, 99)
        matriz[i][j] = str(n_aleatorio).zfill(2) # deixando o numero com um zero a esquerda (01)


# Vendo como ela ficou (não precisa ser assim, mas fica mais bonitinha)
for i in range(len(matriz)):
    print(matriz[i])


#  Centro da matriz (par ou impar)
meio = (len(matriz[j])//2) # a divisão inteira (//) retorna exatamente o centro já que a matriz começa no índice 0
if len(matriz) % 2 != 0:
    print("\nCentro da matriz com ordem impar:")
    print("[",matriz[meio][meio],"]")
else:
    print("\nCentro da matriz com ordem par:")
    print("[",(matriz[meio-1][meio-1]),", ",
            (matriz[meio-1][meio]),"] \n[",
            (matriz[meio][meio-1]),", ",
            (matriz[meio][meio]),"]", sep="")



#   i == posição na linha
#   j == posição na coluna


# contorno da matriz simétrica 
print("\nContorno da matriz:")

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 0:
                print(matriz[i][j], end=", ")
        if i >= 1 and (j == 0 or j == len(matriz)-1) or i == 0 or i == len(matriz)-1:
            if i >= 1 or i == len(matriz)-1:
                print(matriz[i][j], end=", ")
        else: print("00", end=", ")
    print()


# navegando por camadas
print("\nNavegando por camadas:")

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 0:
                print(matriz[i][j], end=", ")
        if i >= 1 and (j == 0 or j == len(matriz)-1) or i == 0 or i == len(matriz)-1:
            if i >= 1 or i == len(matriz)-1:
                print(matriz[i][j], end=", ")
        else: print("00", end=", ")
    print()