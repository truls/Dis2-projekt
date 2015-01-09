def com_theorem(n,fac1,fac2,acc):
	F1=1
	F2=1
	for f in fac1:
		F1*=f
	for f in fac2:
		F2*=f
	R1=(n-1)/F1
	R2=(n+1)/F2
	if (gcd(R1,F1)!=1) or (gcd(R2,F2)!=1):
		return False
	#pocklington
	for i in range(acc):
		a=random.randint(2,n-1)
		print a
		if pow(a,n-1, n) != 1:
			return False
		prime=True
		for q in factors:
			if gcd(a**((n-1)/q)-1,n)!=1:
				prime=False
				break
			print gcd(a**((n-1)/q)-1,n)
		if prime:
			break

	#indsaet ting fra opgave 2
	return n<max(F1**2*F2/2,F1*F2**2/2)
