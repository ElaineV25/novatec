from time import time

from oo.pessoa import Pessoa


class Aluno(Pessoa):
    def estudar(self):
        return '{} está estudando'.format(self.nome)

    def cumprimentar(this, prefixo='E aí galera!'):
        return super().cumprimentar(prefixo)

    def exercer_atividade_de_aula(self):
        return self.estudar()


class Instrutor(Pessoa):
    def ensinar(self):
        return '{} está ensinando'.format(self.nome)

    def cumprimentar(this, prefixo='Olá'):
        inicio = time()
        resultado = super().cumprimentar(prefixo)
        fim = time()
        print('Demorou {} milisegundos'.format(fim - inicio))
        return resultado

    def exercer_atividade_de_aula(self):
        return self.ensinar()


if __name__ == '__main__':
    rogerio = Aluno('Rogerio')

    print(rogerio.estudar())

    renzo = Instrutor('Renzo')
    print(renzo.ensinar())

    turma = [renzo, rogerio]

    for pessoa in turma:
        print(pessoa.cumprimentar())
        print(pessoa.exercer_atividade_de_aula())
