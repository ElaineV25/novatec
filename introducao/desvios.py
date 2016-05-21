while True:
    x = input('Digite um numero: ')
    x = int(x)

    if x == 42:
        print('Resposta do sentido da vida')
        break
    elif 42 < x and x < 50:
        print('Está um pouco acima do sentido da vida')
    elif 32 < x < 42:
        print('Está um pouco abaixo do sentido da vida')
    else:
        print('Está longe do sentido da vida')

print('Vc encontrou o sentido da vida, parabéns')
