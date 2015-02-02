#!/usr/bin/env python3.4
# -*- encoding: utf-8 -*-
# contador de consoantes

def conta(palavra):
	return len([x for x in range(len(palavra)) if palavra[x] not in 'aeiou'])

# usando lambda
consoante = lambda palavra: len([x for x in range(len(palavra)) if palavra[x] not in 'aeiou'])

palavra = raw_input('Coloque a palavra que vc quer saber: ')
print 'A palavra ',palavra,' tem %s consoantes'% (conta(palavra))
