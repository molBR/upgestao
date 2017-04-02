from fuzzywuzzy import fuzz
from fuzzywuzzy import process

listaBD = ['beijinho','brigadeiro','coxinha','pao de queijo','empada','brigadeironha']

def PassaFuzzy(listaBD,selecionado):
	listaRetorna = []
	for x in range(0,len(listaBD)):
		print fuzz.partial_ratio(listaBD[x],selecionado)
		if fuzz.partial_ratio(listaBD[x], selecionado)>=80:
			print "a"
			listaRetorna.append(listaBD[x])
	return listaRetorna
	

print PassaFuzzy(listaBD,"brigadeila")