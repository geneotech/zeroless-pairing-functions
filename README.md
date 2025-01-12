# Zeroless Pairing Functions (ZPFs)

Newly discovered pairing functions proportional to *product* of $x$ and $y$, rather than square of the larger argument. *ZPFs* for short.

These pairing functions work best:

- When $x$ and $y$ are on different orders of magnitude,
- and *especially* when **encoding tuples/sequences of arbitrary length.**

This is just a reference implementation. If this catches interest, I will later optimize encoding/decoding speed or maybe even provide C equivalents.
The explanation of math can be found in this **[math.stackexchange article]()**.

# Benchmarks

Here is a comparison against the famous Rosenberg pairing function $R(x, y) = \max(x, y)^{2} + \max(x, y) + x - y$.

Example sequence:

```
    R_tuple([10, 20, 30, 40, 50]) = 813628265118213965230
pi_tuple_10([10, 20, 30, 40, 50]) = 10022033044055
pi_tuple_3 ([10, 20, 30, 40, 50]) = 320310228347
```

Some pairs:

```
R    (10,1000000) = 1000000000010
pi_10(10,1000000) = 1001783661

R    (10**35,10**10) = 10000000000000000000000000000000000199999999999999999999999990000000000
pi_10(10**35,10**10) = 100000000000000000000000000000000000027726678111
```

$\pi_k$ loses whenever the arguments get close:

```
R    (10**35,10**35) = 10000000000000000000000000000000000100000000000000000000000000000000000
pi_10(10**35,10**35) = 10000000000000000000000000000000000004384821434397613896522554972726635481
```

# Usage

Run `python pi.py` to launch benchmarks, verify the equalities, and exit.

Functions to use in your code (sorry this is not packaged yet):

```python
pi_      (k, x, y)
BIGPI_   (k, x, y)
pi_tuple_(k, [args...])
```

Inverses:

```python
pi_inv   (k, n)
BIGPI_inv(k, n)
```

Shortcuts:

```python
pi_3 (x, y)
pi_10(x, y)
pi_tuple_3([args...])
pi_tuple_10([args...])
```

Note that the `k` in $\pi_k$ is not a "compression" factor. `k` should be empirically chosen depending on the maximum magnitude of $x$ and $y$ you plan to use it with. The decimal base $k = 10$ is a fine choice for reasonable values.

$\pi_k$ is *not* monotonic in `k`. For example:

```
pi_(2,  39050, 1000)  > 2 ** 1000 
pi_(3,  39050, 1000)  = 2305883039
pi_(4,  39050, 1000)  = 639799021
pi_(5,  39050, 1000)  = 610158559
pi_(10, 39050, 1000)  = 3905001331
```

The best $k$ to use rises somewhat logarithmically in the magnitude of the largest possible argument.

# Sequences of arbitrary length

To naively encode/decode tuples by chaining calls to `pi_small` like we did, we need to know how many elements there are up front.
Easy way to do this exists, but I will add this later on.
