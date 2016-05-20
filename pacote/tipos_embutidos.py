lista = [1, 2, 3, 4, 5]


for valor in lista:
    print(valor)

lista.append(7)
print(lista)
print(list(range(10)))


frutas='banana melancia abacate maça'.split(' ')
print(frutas)

# Slicing - Fatiamento

print(frutas[0])
print(frutas[-1])
print(frutas[0:2])
print(frutas[0:len(frutas)])
print(len(frutas))
print(frutas[:2])
print(frutas[1:])
print(frutas[:])
print(frutas[::2])

print(list(reversed(frutas)))
print(list(reversed(frutas[::-1])))
