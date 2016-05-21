# Tudo pode ser transformado em booleano em python

## Regra geral: tudo que lembrar 0 avalia para falso

## Caso óbvio

print(bool(True))
print(bool(False))


### Para  Números

def print_booleano(obj):
    print(obj, bool(obj), sep=' --> ')


print('Inteiros')
print_booleano(0)
print_booleano(-1)
print_booleano(1)

print('Float')
print_booleano(0.0)
print_booleano(-1.1)
print_booleano(1.2)

### Sequencias

print('String')
print_booleano('')
print_booleano('Renzo')

print('Tupla')
print_booleano(tuple())
print_booleano((2,))

print('Dicionario')
print_booleano({})
print_booleano({'a': 1})

# Objetos

print('Objetos')
print_booleano(None)

import pacote2

print_booleano(pacote2)

lista = []

if lista:
    print(lista)


def avaliou():
    print('Hadouken')
    return 4


def f(param=None):
    param = param if param is not None else avaliou()
    return param


print(f())
print(f('Renzo'))
