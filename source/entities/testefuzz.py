#encoding: utf-8
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def PassaFuzzy(listaBD,selecionado):
	listaRetorna = []

	for x in range(0,len(listaBD)):
		if fuzz.partial_ratio(listaBD[x][1], selecionado)>=80:
			listaRetorna.append(listaBD[x])
	return listaRetorna
	

def PassaHistFuzzy(listaBD,selecionado):
	listaRetorna = []
	for x in range(len(listaBD)):
		if fuzz.partial_ratio(listaBD[x][2],selecionado)>=80:
			listaRetorna.append(listaBD[x])
	return listaRetorna