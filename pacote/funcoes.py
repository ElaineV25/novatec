def f(base, expoente=3, valor_resto=2):
    return (base ** expoente) % valor_resto


# print(f(3, 4))
# print(f(2))
# print(f(3, 4, 6))
# print(f(valor_resto=3, base=7))


def media(*numeros):
    '''
    Calcula a média aritmética dos argumentos da função
    Ou seja, soma os elementos e divide pelo numero total de elementos
    :param numeros: parametros a serem extraidos da média
    :return: Número com média
    '''
    n = len(numeros)
    # md = 0
    # for i in numeros:
    #     md += i
    # return md / n
    print(numeros)
    return sum(numeros) / n


if __name__ == '__main__':
    print(media(1))
    print(media(1, 2))
    print(media(1, 2, 3))
    lista = list(range(10))
    print(media(*lista))
    # print(media())
