#loop para checar senha com máximo de 3 tentativas
senha = "12345"
senhaUsuario = input("Diga sua senha: ")
tentativas = 1
while (senha != senhaUsuario) and (tentativas < 3):
    print("errou haha")
    senhaUsuario = input("Diga sua senha: ")
    tentativas+=1
if senha == senhaUsuario:
    print("acertou")
else:
    print("errou haha")

#diz os numeros pares de uma lista de numeros
numeros = (list(range(10)))
print(numeros)
for i in numeros:
    if i % 2 == 0:
        print(i)

#verifica se um elemento específico está na lista
nomes = ["Éder", "danilo", "Alexandre", "Ayrton", "Thiago"]
for i in range(len(nomes)):
    if nomes[i]=="danilo":
        print(f"O danilo está na posição {i+1}")
        break
    elif i == len(nomes)-1:
        print("Não está aqui")

#inverte os elementos de uma lista
lista = [1,2,3,4,5,6,7,8]
print(lista)
ultimo = len(lista)-1
for i in range(len(lista)//2):
    aux = lista[i]
    lista[i] = lista[ultimo-i]
    lista[ultimo-i] = aux
    print(lista)

#verifica os elementos em comum em 2 listas
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7]
intersect = []
for elem1 in lista1:
    for elem2 in lista2:
        if elem2 == elem1:
            intersect.append(elem1)
print(intersect)
