# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import sys

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
    nome_com_indice = 'Renzo Nuccitelli {}'.format(indice)
    arquivo.write(nome_com_indice)
    arquivo.write('\n')
