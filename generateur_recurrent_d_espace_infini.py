def generateur_recurrent_d_espace(alphabet_de_dimension,  coordonné, dimension):
	for i in alphabet_de_dimension:
		if len(coordonné) < dimension-1:
			for y in generateur_recurrent_d_espace(alphabet_de_dimension, coordonné + str(i), dimension):
				yield y
		elif len(coordonné) == dimension-1 :
			yield coordonné + str(i)

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i = i + 1
		for x in generateur_recurrent_d_espace([x for x in range(1, i)],  "", i+1):
			yield x