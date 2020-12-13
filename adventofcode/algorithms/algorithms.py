import functools as ft


def chinese_remainder_theorem(a, n):
    # Solves a system of equations on the form
    #    x = a_i mod n_i.
    # given that n_i are pairwise co-prime.
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    x = 0
    # 1. Compute N = n_1 * n_2 * ... * n_N.
    N = ft.reduce(lambda x, y: x * y, n)
    for a_i, n_i in zip(a, n):
        # 2. For each i, compute y_i = N / n_i.
        y_i = N // n_i
        # 3. For each i, compute z_i = y_i^-1 mod n_i.
        z_i = modular_inverse(y_i, n_i)
        # 4.a. Add a_i * y_i * z_i to x.
        x += a_i * y_i * z_i
    # 4.b. x mod N is the unique solution modulo N.
    return x % N


def modular_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
