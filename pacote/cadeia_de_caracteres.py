# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import sys
from io import UnsupportedOperation

print(sys.getdefaultencoding())  # enconding utilizado pelo interpretador Python
print(sys.getfilesystemencoding())  # encoding do sistema de arquivos

indice = 0

try:
    with open('string.txt', mode='r', encoding='utf8') as arquivo:
        for linha in arquivo:
            print(linha.strip())
            indice += 1
except FileNotFoundError as error:
    logging.error(error.strerror)

with open('string.txt', mode='a', encoding='utf8') as arquivo:
    nome_com_indice = '{indice} Renzo Nuccitelli '.format(indice=indice)
    arquivo.write(nome_com_indice)
    arquivo.write('\n')

arquivo = open('binario.bin', mode='rb')
try:
    cadeia_de_bytes = arquivo.read()
    cadeia_total = bytearray()
    for b in cadeia_de_bytes:
        print(b)
        cadeia_total.append(b)

    print(cadeia_total)
    print(cadeia_total.decode('cp1252'))
    print(type(cadeia_total))
except UnsupportedOperation:
    logging.warning('Arquivo Binário não encontrado')
finally:
    arquivo.close()

arquivo = open('binario.bin', mode='ab')

arquivo.write('café'.encode('cp1252'))
arquivo.close()
