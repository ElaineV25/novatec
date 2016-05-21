from oo.calculadora_oo import Operacao, Calculadora


class Adicao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 + arg2

if __name__ == '__main__':

    calculadora = Calculadora()

    adicao = Adicao()
    calculadora.adicionar_operacao('+', adicao)
    calculadora._sinal = '+'
    calculadora._arg1 = 2
    calculadora._arg2 = 3


    print(calculadora.executar_operacao())