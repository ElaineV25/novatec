def calcular():
    valor1 = float(input('Digite o primeiro valor: '))
    sinal = input('Digite o sinal da operação: ')
    valor2 = float(input('Digite o segundo valor: '))
    if sinal == '-':
        return valor1 - valor2
    elif sinal == '+':
        return valor1 + valor2
    raise ValueError('Operação não suportada')
