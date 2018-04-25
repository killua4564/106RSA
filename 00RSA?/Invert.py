def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def invert(a, m):
    g, x, y = egcd(a, m)
    if g != 1: print('modular inverse does not exist')
    else: return x % m

e = 17993
phi = 89964

d = invert(e, phi)