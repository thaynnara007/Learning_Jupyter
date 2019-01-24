# -*- coding: utf-8 -*-
"""
Alguns conceitos de estatística, part I

+ amostra aleatória simples: um numero n determinado é retirado da população.
É retirando esses elementos de forma aleatoria.
  - com reposição, apos o elemento ser selecionando, ele é colocado de novo na população
  tendo as mesmas chances de ser selecionando de novo para a amostra
  - sem reposição: o elemento é retirado da população, se for selecionando, sem ser reposto de novo
  a população

+ amostra estratificada: a população é dividida em estratos(grupos, por exemplo, educação, raça, etcs)
logo, é retirado uma quantidade igual de elementos de todos os estratos

+ amostragem sistemática: é escolhido um numero n aleatorio, então, a cada n elementos da população, um elemento 
é selecionado.

+ amostragem por unidade monetaria: é escolhido uma feature, e um valor aleatorio dentro da amostragem, é somado
os valores da feature, toda vez que o valor chegar a ser igual ou maior que o valor aleatorio escolhido, a linha
é escolhido.
"""

import pandas as pandas
import numpy as numpy

base = pandas.read_csv('data/iris.csv')
base.head()
base.shape

# amostragem aleatória simples

numpy.random.seed(666) # a amostra vai gerar sempre o mesmo valor
amostra = numpy.random.choice([0,1], size=150, replace=True, p=[0.5,0.5])
len(amostra[amostra == 1])
len(amostra[amostra == 0])