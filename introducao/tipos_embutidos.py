# Lista

lista = [1, 2, 3, 4, 5]

for valor in lista:
    print(valor)

lista.append(7)
print(lista)
print(list(range(10)))

print(lista + [8, 9])  # permite concatenação

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

elementos_repetidos = list(range(100)) * 2
print(elementos_repetidos)
print(set(elementos_repetidos))
renzo_chars = set('renzo')
print(renzo_chars)  # Não mantém ordem

print('r' in renzo_chars)
print('a' in renzo_chars)

vogais = set('aeiou')

print(renzo_chars & vogais)  # interseção
print(renzo_chars - vogais)  # Diferença
print(renzo_chars.union(vogais))  # União

# Dicionário

estados = {'RN': 'Rio Grande do Norte', 'SP': 'São Paulo'}

print(estados['RN'])
estados['RJ']= 'Rio de Janeiro'
print(estados)


for chave in estados:  # mesmo resultado de have in estados.keys()
    print(chave)

for valor in estados.values():
    print(valor)

for chave, valor in estados.items(): # Utilizando desempacotamento de tupla
    print(chave, valor, sep=' --- ')



