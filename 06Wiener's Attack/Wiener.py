import sympy

def fractions(x, y):
    ans = [y // x]
    if y % x == 0: return ans
    else:
        ans.extend(fractions(y % x, x))
        return ans

def continued_fractions(e, n):
    ans = []
    x = fractions(e, n)
    for i in range(1, len(x)):
        k, d = 1, x[i-1]
        for j in x[:i-1][::-1]:
            k, d = d, d * j + k
        ans.append((k, d))
    return ans

def Wiener(e, n):
    for k, d in continued_fractions(e, n):
        phi = (e * d - 1) // k
        # x ** 2 - (n - phi + 1)x + n = 0
        if d == int(sympy.invert(e, phi)):
            return d
            break

e = 17993
n = 90581

d = Wiener(e, n)