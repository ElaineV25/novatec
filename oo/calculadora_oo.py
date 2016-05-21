class Operacao:
    def calcular(self, arg1, arg2):
        raise NotImplementedError('Deve executar calculo com dois parametros')


class Calculadora:
    def __init__(self):
        self._operacoes = {}
        self._sinal = None
        self._arg1 = None
        self._arg2 = None
        self.adicionar_operacao('+', Adicao())

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao

    def executar_operacao(self):
        operacao_escolhida = self._operacoes[self._sinal]
        return operacao_escolhida.calcular(self._arg1, self._arg2)

    def obter_entradas_e_calcular(self):
        self._arg1 = float(input('Digite o primeiro valor: '))
        self._sinal = input('Digite o sinal da operação: ')
        self._arg2 = float(input('Digite o segundo valor: '))
        return self.executar_operacao()


class Adicao(Operacao):
    def calcular(self, arg1, arg2):
        return arg1 + arg2


if __name__ == '__main__':
    calculadora = Calculadora()

    print(calculadora.obter_entradas_e_calcular())
