
def pocklington(n,factors,acc):
	F=1
	for f in factors:
		F*=f
	if F<math.sqrt(n-1):
		print "Need more factors"
		return
	for i in range(acc):
		a=random.randint(2,n-1)
		if pow(a,n-1, n) != 1:
			return False
		prime=True
		for q in factors:
			if gcd(a**((n-1)/q)-1,n)!=1:
				prime=False
				break
		if prime:
			return True
	return False


