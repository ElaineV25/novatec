from time import time


def profile(funcao):
    def funcao_wrapper(*args, **kwargs):
        inicio = time()
        resultado = funcao(*args, **kwargs)
        fim = time()
        print(fim - inicio)
        return resultado

    return funcao_wrapper

@profile
def f(n):
    return 'Executei f {}'.format(n)

print(f.__name__)



a = f

print(a(4))
print(a(5))


def g():
    def h():
        return 'executando h'

    return h


print(g()())
