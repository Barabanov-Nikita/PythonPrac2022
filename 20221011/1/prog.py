import fractions


def issolution(inp):
    s, w, *coefs = inp
    s, w = fractions.Fraction(s), fractions.Fraction(w)
    a_pow = int(coefs[0])
    a_coefs = [fractions.Fraction(a) for a in coefs[1:2 + a_pow]]
    b_pow = int(coefs[a_pow + 2])
    b_coefs = [fractions.Fraction(b) for b in coefs[3 + a_pow:]]

    a, b = sum(a_coefs[i]*s**i for i in range(a_pow, -1, -1)), sum(b_coefs[i]*s**i for i in range(b_pow, -1, -1))
    return a / b == w if b != 0 else False


print(issolution(eval(input())))
