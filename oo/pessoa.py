class Pessoa:
    olhos = 2

    def __init__(self, nome, idade=18, preco=0.00):
        self._idade = idade
        self.nome = nome
        self._preco = preco

    def cumprimentar(this, prefixo='Olá'):
        return '{prefixo} meu nome é {nome}'.format(prefixo=prefixo, nome=this.nome)

    def pagar_com_cartao(self):
        return 'Pagando {preco} por {nome}'.format(preco=self.preco, nome=self.nome)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError('Não é possível utilizar valores negativos')
        self._preco = preco


renzo = Pessoa('Renzo', 33)
renzo_clone = renzo
marcos = Pessoa('Marcos', 19)

print(id(renzo))
print(id(marcos))

print(renzo.cumprimentar())
print(marcos.cumprimentar())

print(renzo.nome)
print(renzo._idade)

print(renzo is marcos)
print(renzo is renzo_clone)
print(renzo == marcos)
print(renzo == renzo_clone)
print(renzo.preco)
renzo.preco = 10
print(renzo.preco)
# renzo.preco = -10  Operação proibida no método setter
print(renzo.preco)
print(renzo.pagar_com_cartao())
print(marcos.pagar_com_cartao())

# Acesso a atributos de classe
print(renzo.olhos)
print(marcos.olhos)
print(Pessoa.olhos)
print(renzo.__dict__)
print(marcos.__dict__)
print(Pessoa.__dict__)
Pessoa.olhos=4
# del renzo.olhos
print(renzo.olhos)
print(marcos.olhos)
print(Pessoa.olhos)
print(renzo.__dict__)
print(marcos.__dict__)
print(Pessoa.__dict__)
print(id(renzo.olhos))
print(id(marcos.olhos))
print(id(Pessoa.olhos))
