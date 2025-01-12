import math

# FUNCTIONS OF INTEREST:
#
# pi_      (k, x, y)
# BIGPI_   (k, x, y)
# pi_tuple_(k, [args...])
#
# INVERSES:
#
# pi_inv   (k, n)
# BIGPI_inv(k, n)
#
# SHORTCUTS:
#
# pi_3 (x, y)
# pi_10(x, y)
# pi_tuple_3([args...])
# pi_tuple_10([args...])

##########################################################
# 1) FUNCTIONS OF INTEREST
##########################################################

def pi_(k, x, y):
    if x == 0:
        return digits_to_int(k, zeroless(k, y))

    d = digits_in_base(k, x)
    d += [0]
    d += zeroless(k, y)

    return digits_to_int(k, d)

def pi_tuple_(k, args):
    if not args:
        return 0
    result = args[0]
    for arg in args[1:]:
        result = pi_(k, result, arg)
    return result

def BIGPI_(k, x, y):
    if x == 0:
        return digits_to_int(k, zeroless(k, y))

    d = zeroless(k, y + 1)
    d += [0]
    d += nth_digit_string(k, x - 1)
    #print(zeroless(k, y), k, y, d, x)

    return digits_to_int(k, d)

##########################################################
# 1.1) THE INVERSES
##########################################################

def pi_inv(k, n):
    digits = digits_in_base(k, n)

    separator = 0

    if separator not in digits:
        return [0, zeroless_inv(k, digits)]

    left, right = split_list_from_right(digits, separator)

    x = digits_to_int(k, left)
    y = zeroless_inv(k, right)

    return [ x, y ]

def BIGPI_inv(k, n):
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

##########################################################
# 2) SHORTCUTS
##########################################################

def pi_3(x, y):
    return pi_(3, x, y)

def pi_10(x, y):
    return pi_(10, x, y)

def pi_tuple_3(args):
    return pi_tuple_(3, args)

def pi_tuple_10(args):
    return pi_tuple_(10, args)

##########################################################
# 3) INTERMEDIATE FUNCTIONS (DIGIT STRINGS/ZEROLESS)
##########################################################

# Z_k(n)
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

def split_list(lst, split_element):
    index = lst.index(split_element)
    return lst[:index], lst[index + 1:]

def split_list_from_right(lst, split_element):
    index = len(lst) - 1 - lst[::-1].index(split_element)
    return lst[:index], lst[index + 1:]

# The original P_{2}

def Z(k, n):
    return digits_to_int(k, zeroless(k, n))

def number_concatenation(k, x, y):
    return digits_to_int(k, digits_in_base(k, x) + digits_in_base(k, y))

def pi_chain_numbers_(k, x, y):
    return digits_to_int(k, digits_in_base(k, x) + [0] + digits_in_base(k, y))

def pi_limsup_(k, x, y):
    e = math.log(k, k - 1)
    #c = ((k-2) ** e) / (k-1)
    k2 = k * k

    return k2 * x * (y ** e)

##########################################################
# 4) OTHER PAIRING FUNCTIONS
##########################################################

def P_2(x, y):
    return (2 * x + 1) * 2**y - 1

def R_tuple(args):
    if not args:
        return 0
    result = args[0]
    for arg in args[1:]:
        result = R(result, arg)
    return result

def R(x, y):
    # Rosenberg pairing function
    return max(x, y) ** 2 + max(x, y) + x - y

##########################################################
# 5) BENCHMARKS/COMPARISONS
##########################################################

def test_limit_superior(k):
    print("Testing for pi being above limit supremum...")

    for n in range(5, 5+1000000):
        k = 10
        pr = pi_inv(k, n)
        x = pr[0]
        y = pr[1]

        if x < 2 or y < 2:
            # To only look at better estimates.
            continue

        r = n / pi_limsup_(k, x, y)

        if r > 1:
            # This would normally happen with y = 1.
            print("ABOVE LIMIT SUPREMUM: ", r, x, y, n)

    print("Test complete.")

def run_comparisons(base_k):
    print ("")
    print ("##########################################")
    print ("####### COMPARISONS WITH OTHER PFS #######")
    print ("##########################################")

    k = base_k
    x, y = 10, 1000000
    print(f"\nFor base {k}.")
    print(f"\nRosenberg vs. pi for (x={x}, y={y}):")
    print(f"  R (x,y) = {R(x, y)}")
    print(f"  pi(x,y) = {pi_(k, x, y)}")

    x, y = 10**35, 10**10
    print(f"\nRosenberg vs. pi for (x=10^35, y=10^10):")
    print(f"  R (x,y) = {R(x, y)}")
    print(f"  pi(x,y) = {pi_(k, x, y)}")

    x, y = 10**35, 10**35
    print(f"\nRosenberg vs. pi for (x=10^35, y=10^35):")
    print(f"  R (x,y) = {R(x, y)}")
    print(f"  pi(x,y) = {pi_(k, x, y)}")

    seq = [10, 20, 30, 40, 50]
    print(f"\nR_tuple({seq}): {R_tuple(seq)}")
    print(f"pi_tuple_{k}({seq}): {pi_tuple_(k, seq)}")

def print_readme_claims():
    print(R    (10,1000000))
    print(pi_10(10,1000000))

    print(R    (10**35,10**10))
    print(pi_10(10**35,10**10))

    print(R    (10**35,10**35))
    print(pi_10(10**35,10**35))

    print(R_tuple    ([10, 20, 30, 40, 50]))
    print(pi_tuple_10([10, 20, 30, 40, 50]))
    print(pi_tuple_3 ([10, 20, 30, 40, 50]))

##########################################################
# 6) ASSERTS - VERIFYING IDENTITIES
##########################################################

def verify_identities():
    print ("")
    print ("##########################################")
    print ("########### VERIFY IDENTITIES ############")
    print ("##########################################")
    print ("")

    verify_set_identities()
    verify_zeroless_identities()
    verify_number_concatenation_inequalities()
    verify_major_functional_equations()
    verify_sanity_identities()

    print ("All identities are correct.")

def verify_set_identities():
    print("Checking set identities...")

    for k in range(2, 11):
        set_fr = set()
        set_iv = set()

        equals = []

        for n in range(0, k**4):
            pr    = BIGPI_inv(k, n)
            prinv = pi_inv(k, n)

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

def verify_zeroless_identities():
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

def verify_number_concatenation_inequalities():
    print("Checking number concatenation inequalities...")

    for k in range(10, 11):
        for x in range(1, 100):
            for y in range(1, 100):
                ch  = number_concatenation(k, x, y)
                assert(ch <= k*x*y + y)
                assert(ch >= x*y + y)
                ch = pi_chain_numbers_(k, x, y)

                # Tighter bounds
                assert(ch <= k*k*x*y + y)
                assert(ch >= k*x*y + y)

                # Multiplicative bounds

                assert(ch <= (k*k+1)*x*y)
                assert(ch >= k*x*y)

def verify_sanity_identities():
    print("Checking sanity generalization identity...")

    for x in range(0, 20):
        for y in range(0, 20):
            assert(pi_(2, x, y) == P_2(x, y))

    print("Checking sanity inverses identity...")

    for k in range(2, 11):
        for n in range(1, 100):
            assert(pi_(k, 0, n) == BIGPI_(k, 0, n))

            # ZEROLESS
            assert(zeroless_inv(k, zeroless(k, n)) == n)

            # SMALLPI
            assert(n == pi_(k, pi_inv(k, n)[0], pi_inv(k, n)[1]))

            # BIGPI
            assert(n == BIGPI_(k, BIGPI_inv(k, n)[0], BIGPI_inv(k, n)[1]))


def verify_major_functional_equations():
    print("Checking major functional equations...")

    # ORIGINAL P_2 FORM
    for x in range(0, 20):
        for y in range(0, 20):
            p = lambda i, j : P_2(i, j)
            z = lambda n : Z(2, n)

            # Original properties
            # Closed form
            assert(p(x, y) == (z(y) + 1) * (2 * x + 1) - 1)

            # Increments
            assert(p(x + 1, y) == p(x, y) + 2*(z(y) + 1))
            assert(p(x, y + 1) == 2 * p(x, y) + 1)

            for c in range(0, 20):
                # Homogeneity
                assert(p(x, y) * c == p(c*x, y) + (c-1) * z(y))

                # Additivity in x
                assert(p(x + c, y) == p(x, y) + p(c, y) - z(y))

                # Additivity in y
                assert(p(x, y + c) == (z(c) + 1) * (p(x, y) + 1) - 1)


    # GENERAL FORM
    for k in range(2, 11):
        for x in range(0, 20):
            for y in range(0, 20):
                p = lambda i, j : pi_(k, i, j)
                z = lambda n : Z(k, n)

                # GENERAL INCREMENT
                assert(p(x, y) * k == p(x, y*(k-1) + 1) - 1)

                # GENERAL CLOSED FORM (ALL NINES)
                if k > 2:
                    frac = ((k-1) ** (y + 1) - 1) // (k - 2)
                    assert(k**y * (k*x + 1) - 1 == p(x, frac - 1))
                else:
                    assert(k**y * (k*x + 1) - 1 == p(x, y))

                # GENERAL CLOSED FORM (ALL ONES)
                if k > 2:
                    frac = ((k-1) ** y - 1) // (k - 2)

                    assert(k**y * (k*x + 1) + ((k ** y) - 1)//(k-1) - k**y == p(x, frac))
                else:
                    assert(k**y * (k*x + 1) + ((k ** y) - 1)//(k-1) - k**y == p(x, y))
                    assert(k**y * (k*x + 1) - 1 == p(x, y))

                for j in range(1, k):
                    assert(p(x, (k-1)*y + j) - j == p(x, y) * k )

                for c in range(0, 20):
                    # HOMOGENEITY/PRODUCT FORMULA
                    assert(p(x, y) * c == p(c*x, y) + (c-1) * z(y))
                    assert(p(c*x, y) == p(x, y) * c - (c-1) * z(y))

                    # ADDITIVITY IN X
                    assert(p(x + c, y) == p(x, y) + p(c, y) - z(y))

##########################################################
# 7) MAIN
##########################################################

def main():
    run_comparisons(10)
    run_comparisons(3)
    verify_identities()
    test_limit_superior(10)

if __name__ == "__main__":
    main()

