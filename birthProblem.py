def probability(n,m):
	numerator = 1
	for i in range(m):
		numerator *= n-i
	denominator = n**m
	return 1-numerator/denominator

d=20
for i in range(11):
	print("Collision probability for ",11+i," people with ",d," projects is: ",probability(d,11+i))









