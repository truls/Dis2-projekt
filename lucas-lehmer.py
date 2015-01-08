

#// Determine if Mp = 2p − 1 is prime
#Lucas–Lehmer(p)
#    var s = 4
#    var M = 2p − 1
#    repeat p − 2 times:
#        s = ((s × s) − 2) mod M
#    if s = 0 return PRIME else return COMPOSITE


def lucas_lehmer(p):
    if p == 0 or p == 1:
        return True
    
    s = 4
    M = pow(2, p) - 1
    for i in range(p - 2):
        s = ((s*s) - 2) % M
    return s == 0


if __name__ == "__main__":
    print(lucas_lehmer(14))

