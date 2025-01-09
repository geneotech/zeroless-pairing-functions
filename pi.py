import matplotlib.pyplot as plt
from os import makedirs,path
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
import math
import os

# FUNCTIONS OF INTEREST
#
# smallpi(k, x, y)
# bigpi(k, x, y)
#
# smallpi_inv(k, n)
# bigpi_inv(k, n)
#

def digits_in_base(b, num):
    if b == 1:
        return [1] * num

    assert(b >= 2)

    if num == 0:
        return [0]
    digits = []
    while num > 0:
        digits.append(num % b)
        num //= b
    return digits[::-1]

def digits_to_int(b, digits):
    if b == 1:
        return len(digits)

    assert(b >= 2)

    num = 0
    power = 1
    for d in reversed(digits):
        num += d * power
        power *= b
    return num

# D_k(n)
def nth_digit_string(b, n):
    if b == 1:
        return [0] * n

    assert(b >= 2)

    if n == 0:
        return []

    # To treat [0] as the 1th string
    n = n - 1

    power = b
    length = 1

    while n - power >= 0:
        n -= power
        power *= b
        length = length + 1

    digits = digits_in_base(b, n)
    digits = [0] * (length - len(digits)) + digits

    return digits

# D_k^{-1}(n)
def digit_string_to_n(b, digits):
    if b == 1:
        return len(digits)

    n = 0
    power = 1

    for i in reversed(digits):
        n += power + i * power
        power *= b

    return n

def sets_equal(a, b):
    return len(a) == len(b) and all(x in a for x in b)

def zeroless(k, n):
    if k == 2:
        return [1] * n

    assert(k > 2)

    s = nth_digit_string(k - 1, n)
    return [digit + 1 for digit in s]

def zeroless_inv(k, digits):
    assert(k >= 2)
    return digits_to_int(k - 1, digits)

def n_zeroless_nines(k, n):
    if k == 2:
        return zeroless(k, n)

    assert(n >= 1)

    i = ((k-1)**(n+1) - 1)/(k - 2) - 1
    return zeroless(k, i)

def smallpi(k, x, y):
    if x == 0:
        return digits_to_int(k, zeroless(k, y))

    d = digits_in_base(k, x)
    d += [0]
    d += zeroless(k, y)

    return digits_to_int(k, d)

def bigpi(k, x, y):
    if x == 0:
        return digits_to_int(k, zeroless(k, y))

    d = zeroless(k, y + 1)
    d += [0]
    d += nth_digit_string(k, x - 1)
    #print(zeroless(k, y), k, y, d, x)

    return digits_to_int(k, d)

def split_list(lst, split_element):
    index = lst.index(split_element)
    return lst[:index], lst[index + 1:]

def split_list_from_right(lst, split_element):
    index = len(lst) - 1 - lst[::-1].index(split_element)
    return lst[:index], lst[index + 1:]

def smallpi_inv(k, n):
    digits = digits_in_base(k, n)

    separator = 0

    if separator not in digits:
        return [0, zeroless_inv(k, digits)]

    left, right = split_list_from_right(digits, separator)

    x = digits_to_int(k, left)
    y = zeroless_inv(k, right)

    return [ x, y ]

def bigpi_inv(k, n):
    digits = digits_in_base(k, n)

    separator = 0

    if n == 0:
        return [0, 0]

    if separator not in digits:
        return [0, zeroless_inv(k, digits)]

    left, right = split_list(digits, separator)

    x = digit_string_to_n(k, right) + 1
    y = zeroless_inv(k, left) - 1

    return [ x, y ]

# The original P_{2}
def P(x, y):
    return (2 * x + 1) * 2**y - 1

def cantor(x, y):
    return y + ((x + y) * (x + y + 1)) // 2 

def szudzik(x, y):
    return x * x + x + y if x >= y else y * y + x

def rosenberg(x, y):
    return max(x, y) ** 2 + max(x, y) + x - y

def number_concatenation(k, x, y):
    return digits_to_int(k, digits_in_base(k, x) + digits_in_base(k, y))

def smallpi_chain_numbers(k, x, y):
    return digits_to_int(k, digits_in_base(k, x) + [0] + digits_in_base(k, y))

def smallpi_limsup(k, x, y):
    e = math.log(k, k - 1)
    c = ((k-2) ** e) / (k-1)

    return c * x * k * k * y ** e

def main():
    #################################################################################
    # LIMITS
    #################################################################################

    if True:
        #################################################################################
        # LIMITS: smallpi GROWTH
        #################################################################################
        if False:
            for n in range(5, 5+1000000):
                k = 10
                pr = smallpi_inv(k, n)
                x = pr[0]
                y = pr[1]

                if x < 1 or y < 1:
                    continue

                r = n / limsup(k, x, y)

                if r > 1:
                    print("Above lim sup: ", r, a, e)

    #################################################################################
    # SET IDENTITIES ASSERTIONS
    #################################################################################

    if True:
        print("Checking set identities...")

        for k in range(2, 11):
            set_fr = set()
            set_iv = set()

            equals = []

            for n in range(0, k**4):
                pr    = bigpi_inv(k, n)
                prinv = smallpi_inv(k, n)

                set_fr.add((pr[0], pr[1]))
                set_iv.add((prinv[0], prinv[1]))

                if sets_equal(set_fr, set_iv) and n > 1:
                    equals = equals + [n]

            the_off_equal = k**2 + k - 2
            assert(the_off_equal in equals)

            for n in range(1, 4):
                repunit = (k**(n+1) - 1) // (k - 1)
                assert(repunit - 1 in equals)
                assert(repunit in equals)
                assert(repunit + k - 2 in equals)

                #print(repunit - 2, the_off_equal)
                if n > 1:
                    assert((not (repunit - 2 in equals)) )

                assert(not (repunit + k in equals))

        print ("Passed set identities.")


    #################################################################################
    # PROPERTIES IDENTITIES ASSERTIONS
    #################################################################################

    if True:
        print("Checking zeroless/digit string identities...")

        # Some zeroless inv and smaller base identity
        for i in range(2, 1000):
            for k in range(2, 20):
                some_zr = zeroless(k+1, i)

                assert(i == digits_to_int(k, some_zr))
                assert(i == zeroless_inv(k+1, digits_in_base(k, i)))
                # Honestly dont know why this holds
                assert(i == digits_to_int(k, zeroless(k+1, i)))

        # Example from OEIS
        assert(digits_to_int(10, zeroless(10, 8773)) == 12927)
        assert(digits_to_int(10, zeroless(10, 1000)) == 1331)

        # ZEROLESS/DIGIT IDENTITIES
        assert(n_zeroless_nines(10, 1) == [9])
        assert(n_zeroless_nines(10, 2) == [9,9])

        for k in range(2, 11):
            for n in range(1, 10):
                assert(n_zeroless_nines(k, n) == [k-1] * n)
                assert(digits_to_int(k, n_zeroless_nines(k, n)) == k ** n - 1)
                assert(digits_to_int(10, zeroless(10, (9**(n+1) - 1)/8 - 1)) == 10**n - 1)

            for n in range(1, 100):
                # Zk and Dk identity
                assert(digits_to_int(k, zeroless(k, n)) == digit_string_to_n(k, nth_digit_string(k-1, n)))
                # Inverse
                digs = digits_in_base(k, n)

                if not (0 in digs):
                    assert(zeroless_inv(k, digs) == digit_string_to_n(k-1, nth_digit_string(k, n)))

                # NTH DIGIT STRING
                assert(nth_digit_string(k, n+1) + [0] == nth_digit_string(k, k*n+k+1))
                assert(nth_digit_string(k, n)   + [0] == nth_digit_string(k, k*n+1))

                assert(zeroless(k, n) + [1] == zeroless(k, (k-1)*n+1))

                # Therefore
                assert(digits_to_int(10, zeroless(k, n)) * 10 == digits_to_int(10, zeroless(k, (k-1)*n+1)) - 1)

        print("Checking number concatenation identities...")

        #################################################################################
        # LIMITS: number chains
        #################################################################################
        for k in range(10, 11):
            for x in range(1, 100):
                for y in range(1, 100):
                    ch  = number_concatenation(k, x, y)
                    assert(ch <= k*x*y + y)
                    assert(ch >= x*y + y)
                    ch = smallpi_chain_numbers(k, x, y)

                    # Tighter bounds
                    assert(ch <= k*k*x*y + y)
                    assert(ch >= k*x*y + y)

                    # Multiplicative bounds

                    assert(ch <= (k*k+1)*x*y)
                    assert(ch >= k*x*y)

        # SANITY GENERALIZATION EQUALITY
        for x in range(0, 20):
            for y in range(0, 20):
                assert(smallpi(2, x, y) == P(x, y))

        # SANITY
        for k in range(2, 11):
            for n in range(1, 100):
                assert(smallpi(k, 0, n) == bigpi(k, 0, n))

                # ZEROLESS
                assert(zeroless_inv(k, zeroless(k, n)) == n)

                # SMALLPI
                assert(n == smallpi(k, smallpi_inv(k, n)[0], smallpi_inv(k, n)[1]))

                # BIGPI
                assert(n == bigpi(k, bigpi_inv(k, n)[0], bigpi_inv(k, n)[1]))


        print("Checking multiplication identities...")

        # MAJOR FUNCTIONAL EQUATIONS
        for k in range(2, 11):
            for x in range(0, 20):
                for y in range(0, 20):
                    p = lambda i, j : smallpi(k, i, j)

                    # MULTIPLICATIVITY DUE TO ZEROLESS ENDING

                    assert(p(x, y) * k == p(x, y*(k-1) + 1) - 1)

                    for c in range(0, 20):
                        assert(p(x, y) * c == p(c*x, y) + (c-1) * p(0, y))


    print ("All asserts have passed.")

if __name__ == "__main__":
    main()

