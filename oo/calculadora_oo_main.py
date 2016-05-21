from oo.calculadora_oo import Operacao, Calculadora


class Subtracao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 - arg2


class Multiplicao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 * arg2


class CalculadoraPolonesaReversa(Calculadora):
    def obter_entradas(self):
        self._sinal = input('Digite o sinal da operação: ')
        self._arg1 = float(input('Digite o primeiro valor: '))
        self._arg2 = float(input('Digite o segundo valor: '))


if __name__ == '__main__':
    calculadora = CalculadoraPolonesaReversa()
    sub = Subtracao()
    mul = Multiplicao()
    calculadora.adicionar_operacao('-', sub)
    calculadora.adicionar_operacao('*', mul)
    print(calculadora.obter_entradas_e_calcular())
