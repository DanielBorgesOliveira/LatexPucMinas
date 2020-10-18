#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

'''
Esse script organiza uma lista latex (toc) em ordem alfabética.
Ncessário indicar o do arquivo com a lista na variável filename.
'''

#filename = 'main.list0'
filename = sys.argv[1]

with open(filename) as f:
    content = f.readlines()

with open(filename, 'w') as f:
    for i in sorted(content):
        f.write(i)
