import random

def lucas(factors,acc):
    n=1
    for f in factors:
        n*=f
    n+=1
    print n
    for i in range(acc):
        a = random.randint(2,n-1)
        if a**(n-1) % n != 1:
            return False
        prime = True
        for q in factors:
            if a**((n-1)/q) % n == 1:
                prime = False
                break
        if prime:
            print a
            return True
    return False


if __name__ == "__main__":
    print lucas([2,2,2,1667],1)

