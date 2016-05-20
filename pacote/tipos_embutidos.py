# Lista

lista = [1, 2, 3, 4, 5]

for valor in lista:
    print(valor)

lista.append(7)
print(lista)
print(list(range(10)))

frutas = 'banana melancia abacate maça'.split()
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
del frutas[1]
frutas.pop()
frutas[0] = 'Banana Nanica'

print(frutas)

# Tuplas

naipes = ('Paus', 'Ouros', 'Copas', 'Espadas')

print(naipes)
# naipes[0]='Foo' Operação proibida pois tupla é imutável

print(naipes[:2])  # posso fazer pq cria nova tupla

primeiro, *ultimos = naipes

print(primeiro, ultimos)

# Conjuntos

