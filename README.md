# zeroless-pairing-functions
Newly discovered pairing functions proportional to *product* of x and y, rather a square of the larger one. ZPFs for short.

This is a mirror of the article at:

# The Zeroless [Pairing Function](https://en.wikipedia.org/wiki/Pairing_function)

There exists a fascinatingly trivial pairing **bijection** $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ that should perhaps be common knowledge. Consider:

$$
\Large
\begin{align}
\pi(\color{green}{39050},\color{darkred}{1000}) & = \color{green}{\underbrace{39050}_{x}}\mspace{8mu}{{0}}\color{darkred}{\mspace{8mu}\underbrace{1331}_{Z(y)}}.
\end{align}
$$

1) We take the $\color{green}{\text{digits of} \ x}$.
2) We add the digit $0$ as the separator.
3) We append the $\color{darkred}{y\text{-th}}$ [**zeroless number**](https://oeis.org/A052382), thereby enumerating **all strings of digits $1-9$**.

That is all. Why is this a bijection?

1) Pairs $x = 0, y > 0$ enumerate all numbers without the digit $0$.
    - $x$ and the separator become leading zeros and hence naturally disappear.
2) Pairs $x \geq 0, y = 0$ enumerate all numbers that have at least one digit $0$ **and end** with a $0$.
    - $Z(\color{darkred}{0}) = \varnothing$, yet the separator zero remains. This is the set of all multiplies of $10$.
3) Pairs $x > 0, y > 0$ enumerate all numbers that have at least one digit $0$ **and don't end** with a $0$.

Any natural number falls into exactly one of the three disjoint categories. From there it is clear it inverts into a unique pair.

Most will have noticed the choice of base $10$ to be completely arbitrary.
Surprisingly, there exists a closed form for the case of binary numbers, and that is the century-old [**Pepis-Kalmar-Robinson pairing function:**](https://en.wikipedia.org/wiki/Pairing_function#Other_pairing_functions)

$$
P_{2}(x, y) = 2^{y}(2x + 1) - 1
$$

Though disliked for its growth rate, $P_{2}$ admits to a **generalization into higher number bases**, whereby it discards the exponent and performs on par with contemporary pairing functions.

To illustrate, $P_{2}(25, 4)$ may be rewritten as:

$$
\Large
\begin{align}
P_{2}(\color{green}{11001_{(2)}},\color{darkred}{4}) & = (\color{green}{\underbrace{11001}_{x_{(2)}}}\mspace{8mu}{{0}}\color{darkred}{\mspace{8mu}\underbrace{1111}_{Z_{2}(y)}} )_{(2)} = 815.
\end{align}
$$

Where $\color{darkred}{Z_k(y)}$ stands for **the y-th base-k zeroless number.** In binary number system, the only zeroless numbers are, of course, the consecutive strings of ones: $1, 11, 111, \dots$.

This definition invites us to lift $P_2$ to any base $k$:

$$
\Large
\pi_{k}(\color{green}{x},\color{darkred}{y}) = ( \color{green}{x_{(k)}} \mathbin\Vert \mspace{-20mu}\overbrace{0}^{\text{separator}}\mspace{-20mu} \mathbin\Vert \color{darkred}{Z_{k}(y)} )_{(k)}
$$

$$
\text{Or more succintly,}
$$

$$
\pi_k(x, y) = xk \mathbin\Vert_{k} Z_{k}(y)
$$

$$
\text{for all} \ k \geq 2.
$$

Where $p \mathbin\Vert_{k} q$ stands for the [concatenation of $p$ and $q$](https://mathworld.wolfram.com/Concatenation.html) in base $k$.

We get an *infinite* family of pairing bijections $\pi_k: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$, and it is obvious that the special case $\pi_2 = P_2$.

$\pi_3$ and above are no longer exponential. To recall the first example,

$$
\begin{align}
\pi_{2}(\color{green}{39050},\color{darkred}{1000}) & > 2^{\color{darkred}{1000}} \\
\pi_{3}(\color{green}{39050},\color{darkred}{1000}) & = 2305883039 \\
\pi_{4}(\color{green}{39050},\color{darkred}{1000}) & = 639799021 \\
\pi_{5}(\color{green}{39050},\color{darkred}{1000}) & = 610158559 \\
\pi_{10}(\color{green}{39050},\color{darkred}{1000}) & = \color{green}{39050}{0}\color{darkred}{1331} \\
\end{align}
$$

# Compactness

Paul Tarau was [**the first to discover in 2013**](https://arxiv.org/abs/1301.0129) that $P_{2}$ can be generalized to any number base. However, Tarau's approach is based on [$p$-adic valuations](https://en.wikipedia.org/wiki/P-adic_valuation), which preserves **exponential** growth in one of the arguments. 

The worst-case behavior of $\pi_k$ can be shown to be roughly:

$$
(k^{2} + 1)xy^{\log_{k-1}{(k)}}
$$

Thus, our $\pi_k(x, y)$ *does* as well grow asymmetrically, but this is due to a small **constant exponent** in $y^{\log_{k-1}(k)}$. This exponent very rapidly approaches $1$ from above:

$$
\lim_{k \to \infty} {\log_{k-1}(k)} = \lim_{k \to \infty} {\frac{\ln(k)}{\ln(k-1)}} = 1^+
$$

Which for the familiar $\pi_{10}$ gives around:

$$
101xy^{1.04\dots}
$$

$\pi_k$ uncannily approaches multiplication as $k$ goes to infinity - even though it remains trivially invertible.

Consequently, $\pi_{10}$ performs better than [Cantor](https://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function), [Szudzik](https://web.archive.org/web/20111125104326/http://szudzik.com/ElegantPairing.pdf) and [Rosenberg-Strong](https://arxiv.org/abs/1706.04129) whenever $x$ and $y$ are on different orders of magnitude.

Compared against the commonly used $R(x, y) = \max(x, y)^{2} + \max(x, y) + x - y$:

$$
\begin{align}
R(10, 1000000) & = \color{darkred}{1000000000010} \\
\pi(10, 1000000) & = \color{green}{1001783661} \\
R(10^{35}, 10^{10}) & \simeq \color{darkred}{10^{70}} \\
\pi(10^{35}, 10^{10}) & \simeq \color{green}{10^{47}} \\
\\
\text{However:} \\
R(10^{35}, 10^{35}) & \simeq  \color{green}{10^{70}} \\
\pi(10^{35}, 10^{35}) & \simeq \color{darkred}{10^{73}}
\end{align}
$$

*(whenever speaking of base $10$, I shall omit the subscript $_{10}$ for brevity)*

$\pi$ shows its strength especially when encoding sequences:

$$
\begin{align}
R(R(R(R(10, 20), 30), 40), 50) & = \color{darkred}{813628265118213965230} \\
\pi(\pi(\pi(\pi(10, 20), 30), 40), 50) & = \color{green}{10022033044055}
\end{align}
$$

Trivially, $\pi_k$ is monotonic in either argument. That is to say,

$$
\text{for all} \ X > x \ \text{and} \  Y > y\text{:} \\
\pi_k(X, y) > \pi_k(x, y) \\
\pi_k(x, Y) > \pi_k(x, y) \\
\pi_k(X, Y) > \pi_k(x, y)
$$

# Complexity

$\pi_{k}$ merely translates between numeral systems, and so performs no more than $O(\log_{k}(x) + \log_{k-1}(y))$ operations of elementary integer arithmetic.

The inverse **does not involve a square root** as is the case with widely used quadratic pairing functions. Simply split the argument by the rightmost zero and convert the representations back. 

Finding $Z_k(y)$ can be done in $O(\log_{k-1}(y))$, as demonstrated later on.

# Plots

If we invert the subsequent natural numbers by taking $\pi_{3}^{-1}(n)$, this is how the output pairs $(x, y)$ distribute on the plane:

||
|:----:|
|![The inverses of pi in ternary number system][1]<br>The space-filling curve of $\pi_{3}^{-1}$.|


For comparison, this is the exponential $P_2^{-1}$, or equivalently, $\pi_{2}^{-1}(n)$:

||
|:----:|
|![The inverses of pi in ternary number system][2]<br>The space-filling curve of $\pi_{2}^{-1}$.<br>Exponential growth in one of the arguments becomes evident.|

A striking property of $\pi_3$ and higher is that they look like **skewed hyperbolas**, even though they are trivial to compute in both directions. This is unexpected because any thus far known hyperbolic PFs encode information about integer factorization - a brilliant example [was given by Arnold Rosenberg in 2003:](https://www.researchgate.net/publication/220181086_Efficient_Pairing_Functions_-_and_Why_You_Should_Care)

||
|:----:|
|![Rosenberg's hyperbolic pairing function][3]<br>Rosenberg's hyperbolic pairing function. **$\delta(n)$ denotes the number of divisors of $n$**.|

Matthew Szudzik introduced the idea of [*base-$n$ proportional* pairing functions in 2018.](https://arxiv.org/abs/1809.06876v3) Though sounding similar to $\pi_k$, Szudzik's family of PFs fill the 2D plane through a "single" rectangle that ever-expands from the origin in alternating directions, rather than through hyperbolic shells.

# A fresh look on divisibility

From the definition of $\pi_k$, it follows immediately that:

$$
\pi_k(x, 0) = kx
$$

And since $kx = xk$, then perhaps interestingly, if $x \geq 2$:

$$
\pi_k(\color{green}{x}, 0) = \pi_{\color{green}{x}}(k, 0)
$$

It should be clear by now that:

$$
y = 0 \iff k \mid \pi_k(x, y) 
$$

This is because $k$ divides some $n$ if and only if that $n$ ends with a $0$ in base $k$. But $\pi_k(x, y)$ will *never* end with a zero in base $k$ for $y > 0$ by definition: $\pi_k(x,y)$ ends with a *zeroless* number $Z_k(y)$.

Hence, if some $\pi_k(x, y) = n$, then $y$ can be conceived of as the "remainder" after "dividing" some $n$ by some base $k$.

Here I am plotting such remainders for all $n$ from $1$ through $100$:

||
|:----:|
|![The y coordinates after inverting n in successive bases.][4]<br>Inverting the first $100$ numbers in successive bases. For every frame $n$ from $1$ to $100$, we plot $y = \pi_{x}^{-1}(n)[2]$. That is to say, we invert $n$ using $\pi^{-1}$ in successive number bases (base given by $x$), and set the plotted $y$ coordinate to the second element of the inverted pair. $y = 0 \iff x | n$. We pause for a while at every prime $n$.|

The hyperbolic shape emerges due to a simple probabilistic property: as we represent $n$ in higher bases, it has less and less digits. If each digit is a random variable between $0$ and $k-1$, then as $k$ increases, digits have progressively less chance to be $0$ - thus as $k$ grows, $n_{(k)}$ is more likely to be *zeroless*, with the asymptotic limit at $k = n+1$. Trivially, $n$ is always the $n$-th zeroless number in bases $n+1$ and above.

# Identities

By definition:

- $\pi_k(x, 0) = kx$
- $\pi_k(x, 0) = \pi_x(k, 0), x \geq 2$
- $\pi_k(0, y) = Z_k(y)$

Summary of what I have derived so far:

1) For any $c \geq 0$:
    - $\pi_k(cx, y) = c \cdot \pi_k(x, y) - (c-1)Z_k(y)$, or rearranged:
    - $c \cdot \pi_k(x, y) = \pi_k(cx, y) + (c-1)Z_k(y)$
2) $k\cdot\pi_k(x, y) = \pi_k(x, (k-1)y + 1) - 1$
3) $\pi_k(kx, y) + (k-1)Z_k(y) = \pi_k(x, (k-1)y + 1) - 1$
    - This just combines 1) and 2).
4) For any $n \geq 0$:
    - $\pi_k(x, \frac{(k-1)^{n+1} - 1}{k - 2} - 1) + 1 = k^n(kx + 1)$

The rest of this chapter is a not-too-rigorous explanation of how I arrived at these identities.

## Homogeneity in $x$

$\pi$ has quasi-homogeneity in $x$: it is not hard to imagine what happens when you replace some $\pi(x, y)$ with $\pi(cx, y), \text{for any} \ c \geq 0$.

Consider, for $c = 7, \color{green}{x = 39050}, \color{darkred}{y = 1000}$:

$$
\begin{align}
\color{green}{x} & = \color{green}{39050} \\
\color{purple}{cx} & = \color{purple}{273343} \\
\pi(\color{green}{x},\color{darkred}{y}) & = \color{green}{39050}0\color{darkred}{1331} \\
\pi(\color{purple}{cx},\color{darkred}{y}) & = \color{purple}{273343}0\color{darkred}{1331} \\
\end{align}
$$

On the other hand:

$$
\begin{align}
\pi(\color{green}{x},\color{darkred}{y}) & = \color{green}{39050}0\color{darkred}{1331} \\
\pi(0,\color{darkred}{y}) & = \color{darkred}{1331} \\
(\pi(\color{green}{x},\color{darkred}{y}) - \pi(0,\color{darkred}{y})) & = \color{green}{39050}00000 \\
c \cdot (\pi(\color{green}{x},\color{darkred}{y}) - \pi(0,\color{darkred}{y})) & = \color{purple}{273343}00000 \\
\pi(0,\color{darkred}{y}) + c \cdot  (\pi(\color{green}{x},\color{darkred}{y}) - \pi(0,\color{darkred}{y})) & = \color{purple}{273343}0\color{darkred}{1331} \\
\\
\text{This is why}: \\
\pi(0,\color{darkred}{y}) + c \cdot  (\pi(\color{green}{x},\color{darkred}{y}) - \pi(0,\color{darkred}{y})) & = \pi(\color{purple}{cx},\color{darkred}{y}) \\
\end{align}
$$

Knowing also that $\pi_k(0, y) = Z_k(y)$, We get the recurrence relation:

$$\Large
\pi_k(cx, y) = c \cdot \pi_k(x, y) - (c-1)Z_k(y)
$$

$$
\text{For all} \ x,y,c \geq 0.
$$

Rearranging terms, we get the equivalent product formula:

$$
c \cdot \pi_k(x, y) = \pi_k(cx, y) + (c-1)Z_k(y)
$$

### Based on the trailing $Z_k(y)$

[OEIS gives](https://oeis.org/A052382) a simple recurrence relation for $Z(n)$:

$$
10 \cdot Z(n) + c = Z(9n + c), \\
1 \leq c \leq 9.
$$

In general:

$$
k \cdot Z(n) + c = Z_{k}((k-1)n + c), \\
1 \leq c \leq k-1.
$$

We now have a way of calculating $k \cdot \pi_k(x, y)$. Why? 

Since $\pi_k(x, \color{purple}{y})$ ends with $Z_k(\color{purple}{y})$, replacing $\pi_k(x, \color{purple}{y})$ with $\pi_k(x, \color{purple}{(k-1)y + 1})$ changes the suffix from $Z_k(y)$ to $k \cdot Z_k(y) + 1$. This means $\pi_k(x, y)$ will end up with an additional $1$ at the end. Subtract $1$ and we've just got an additional $0$ instead.

Hence:

$$\Large
k \cdot \pi_k(x, y) = \pi_k(x, (k-1)y + 1) - 1
$$

Knowing this, and the arbitrary product formula $c \cdot \pi_k(x, y)$ we derived in the previous section, we may for the first time correlate the two coordinates:

$$
\pi_k(kx, y) + (k-1)Z_k(y) = \pi_k(x, (k-1)y + 1) - 1
$$

The meaning of which is... likely tautological.

#### Endings with arbitrary number of nines

OEIS gives a formula for the n-th zeroless number of the form $9, 99, 999, \dots$:

For any $n \geq 1$: 

$$
Z(\frac{9^{n+1} - 1}{8} - 1) = 10^n - 1
$$

In general, for any base $k > 2$:

$$
Z_k(\frac{(k-1)^{n+1} - 1}{k - 2} - 1) = k^n - 1
$$

It is then possible to pick such $y$ that $\pi_k(x, y)$ ends with $n$ digits $k - 1$. Adding $1$ would result in all zeros again. Suppose for $k = 10, n = 3$ and some $x,y$ such that $Z(y) = 999$:

$$
\begin{align}
\pi_k(x, 0)     & = 84330 \\
k^n\pi_k(x, 0) & = 84330000 \\
k^n\pi_k(x, 0) + k^n & = 84331000 \\
\pi_k(x, \color{darkred}{y})     & = 84330\color{darkred}{999} \\
\pi_k(x, \color{darkred}{y}) + 1 & = 84331000
\end{align}
$$

Seeing this, we may establish, for any $n \geq 1$:

$$\Large
\pi_k(x, \frac{(k-1)^{n+1} - 1}{k - 2} - 1) + 1 = k^n\pi_k(x, 0) + k^n
$$

It is easy to see $k^n$ divides the LHS, although it is likely insignificant.

# Asymptotic growth

Working with base $10$ for simplicity, $\pi_{10}$ is exactly:

$$
\pi(x, y) = 10x \mathbin\Vert Z(y)
$$

There are two things we'd like to approximate:

1) The [number concatenation](https://mathworld.wolfram.com/Concatenation.html) $p \mathbin\Vert q$.
2) The $n$-th zeroless number $Z(n)$.

## Concatenation

There is an exact closed form:

$$
p \mathbin\Vert q = p \cdot 10^{\lfloor \log_{10}(q) \rfloor + 1} + q, \\
q \geq 1.
$$

We may easily come up with an algebraic bound on this operation. Certainly,

$$
\lfloor \log_{10}(q) \rfloor \leq \log_{10}(q)
$$

Then,

$$
\begin{align}
p \mathbin\Vert q & \color{darkred}{=} p \cdot 10^{\lfloor \log_{10}(q) \rfloor + 1} + q \\
p \mathbin\Vert q & \color{green}{\leq} p \cdot 10^{\log_{10}(q) + 1} + q \\
p \mathbin\Vert q & \leq p \cdot 10^{\log_{10}(q)} \cdot  10 + q \\
p \mathbin\Vert q & \leq pq \cdot  10 + q \\
p \mathbin\Vert q & \leq 10pq + q
\end{align}
$$

In that case, we have the inequality for $\pi$:

$$
\begin{align}
\pi(x, y) & \leq 100 x \cdot Z(y) + Z(y) \\
\end{align}
$$

But for any $x \geq 1$, it is certainly the case that:

$$
100 x \cdot Z(y) + Z(y) \leq  101 x \cdot Z(y)
$$

Although a bit of an overestimate, the right-hand side is way easier to work with.

In general:

$$
\begin{align}
p \mathbin\Vert_{k} q & \leq kpq + q\\
\pi_k(x, y) & \leq (k^2 + 1) x \cdot Z(y)
\end{align}
$$

## Zeroless numbers

[OEIS gives](https://oeis.org/A052382) a limit on the growth of $Z(n)$:

$$
\limsup_{n \to \infty} \frac{Z(n)}{n^{\log_9(10)}} = \frac{8^{\log_9(10)}}{9} \simeq 0.982
$$

This means $n^{\log_9(10)}$ is already a great estimate for the worst-case of $Z(n)$.

OEIS additionally gives the following limit for any base $k \geq 3$:

$$
\limsup_{n \to \infty} \frac{Z_k(n)}{C_k n^{\log_{k-1}(k)}} = 1^+ \\
$$

$$
\text{with the constant:}
$$

$$
C_k = \frac{(k - 2)^{\log_{k-1}(k)}}{k - 1}
$$

$C_k$ rapidly approaches $1$ such that it's negliglible, with $\sim 0.982$ at $k = 10$.

$$
\lim_{k \to \infty} C_k = 1^-
$$

This is because the exponent $\log_{k-1}(k)$ would "add" only $1$ to $k-1$, so it adds *even less* to the numerator which is $k - 2$, and thus keeps the numerator always just a little below the denominator $k - 1$.

Thus, as we choose a higher base $k$ for $Z_k(n)$, estimating the worst-case with $n^{\log_{k-1}(k)}$ gets ever more accurate.

## Combining the bounds

Now consider some given $x \geq 1$. Recall this inequality for $\pi_k$:

$$
\begin{align}
\pi_k(x, y) & \leq (k^{2} + 1)x \cdot Z_k(y)
\end{align}
$$

We may divide both sides by $(k^{2} + 1)x$:

$$
\frac{\pi_k(x, y)}{(k^{2} + 1)x} \leq Z_k(y)
$$

And finally, by $C_k y^{\log_{k-1}(k)}$ (define the constant $K = C_k (k^{2} + 1)$ for brevity):

$$
\frac{\pi_k(x, y)}{Kxy^{\log_{k-1}(k)}} \leq \frac{Z_k(y)}{C_k y^{\log_{k-1}(k)}}
$$

Moments before, we had seen that the limit supremum of the right hand side is $1^+$.

Certainly, for any $f(n) \leq g(n)$, one can say the same about their upper limits, even though the converse needs not hold:

$$
\limsup_{n \to \infty} f(n) \leq \limsup_{n \to \infty} g(n)
$$

In that case, we proceed to substitute both sides of the inequality with their respective limits:

$$
\begin{align}
\limsup_{y \to \infty} \frac{\pi_k(x, y)}{K xy^{\log_{k-1}(k)}} & \leq 1.
\end{align}
$$

Finally, we estimate that $K = C_k (k^{2} + 1) \simeq k^2$: 
- the $k^2$ in $(k^2 + 1)$ dominates, 
- and $C_k$ rapidly approaches $1$.

Therefore, with a certain dose of hand-waving, we can say that, for any given $x \geq 1$ and big enough $k$, in the worst case:

$$\Large
\pi_k(x, y) \sim k^{2} xy^{\log_{k-1}(k)}
$$

$$
\text{as} \ y \to \infty
$$

# Calculating $Z_k(y)$

## Strings of digits

Let us first ask: how do we uniquely assign a *number* to an *arbitrary string of digits*, e.g. "$00394$"?

[Just listing all natural numbers won't do.](https://en.wikipedia.org/wiki/Bijective_numeration) The number $2$ can stand for the string "$2$" just as it could for "$00002$".

It turns out it is sufficient to take [**the n-th number starting with $1$**](https://oeis.org/A131835) and trim the leading $1$. 

For example:

$$\require{cancel}
\begin{align}
D(0)   & = \cancel{1} = \varnothing \\
D(1)   & = \cancel{1}\color{green}{0} \\
D(2)   & = \cancel{1}\color{green}{1} \\
       & \dots \\
D(10)  & = \cancel{1}\color{green}{9} \\
D(11)  & = \cancel{1}\color{green}{00} \\
D(12)  & = \cancel{1}\color{green}{01} \\
D(13)  & = \cancel{1}\color{green}{02} \\
       & \dots \\
D(110) & = \cancel{1}\color{green}{99} \\
D(111) & = \cancel{1}\color{green}{000} \\
D(112) & = \cancel{1}\color{green}{001} \\
\end{align}
$$

&nbsp; &nbsp; &nbsp; &nbsp; To calculate $D(1200)$, we subtract subsequent powers of $10$ from $1200$ for as long as we can before going below $0$:

$$
1200 - 1 - 10 - 100 - 1000 = 89
$$

&nbsp; &nbsp; &nbsp; &nbsp; The number of digits is equivalent to the number of subtractions. We pad the surplus with zeros. Hence,

$$
D(1200) = \cancel{1}\color{green}{0089}
$$

This idea can be generalized to any base $k$. Simply subtract powers of $k$ instead of powers of $10$, and once we may subtract no more, write down the remainder in base $k$.

Calculating again for base $k=9$: 

$$
1200 - 1 - 9 - 81 - 729 = 380_{(10)} = 462_{(9)}
$$

Hence:

$$
D_9(1200) = \cancel{1}\color{green}{0462}
$$

In this way, $D_9$ enumerates all strings of digits from the set $\{0,1,...,8\}$.

The inverse $D^{-1}_k$, a *ranking* function for strings, is just as easy to compute on any input string of digits:
- Let $d_i$ be the $i$-th digit from the right.
- The result is $(d_0+1)k^{0}+(d_1+1)k^{1}+...+(d_n+1)k^{n}$.
- This is effectively reading a number $n$ in base $k$ but as if each digit was shifted by $1$.

## Going from $D_k$ to $Z_k$

A useful fact about *numbers without zero* is that they are actually nothing more than *arbitrary strings of digits*. Since we don't need to consider leading zeros, you may conceive of any *string* of digits $1-9$ you like, e.g. "$1112194$" - and you'll always find a single and unique zeroless number that corresponds to it - $1112194$.

Thus, to obtain the $n$-th zeroless number, notice it's enough to get the $n$-th string of digits from the set $\{0, 1, ..., 8\}$ - which happens to be $D_{9}(n)$ - **and then** increase all obtained digits by one.

Knowing this, $Z_k(n)$ can be expressed as:

$$
Z_k(n) = D_{k}^{-1}(D_{k-1}(n))
$$

E.g. $Z_{10}(1200) = D_{10}^{-1}(D_9(1200)) = D_{10}^{-1}(\cancel{1}\color{green}{0462}) = 1573.$

Since all digits of the string $D_9(n)$ are less than $9$, there will be no carry when $D_{10}^{-1}$ adds consecutive powers of $10$. $D_{10}^{-1}$ ends up merely incrementing each digit of the string, lifting them to the range $\{1, 2, ..., 9\}$, thus obtaining a zeroless number.

We now see calculating $Z_k(y)$ takes at worst $O(\log_{k-1}(y))$ steps of integer arithmetic.

The inverse, i.e. calculating the $n$ from a given $Z_k(n)$ is equally trivial:

$$
Z_{k}^{-1}(n) = D_{k-1}^{-1}(D_{k}(n))
$$

We might take a shortcut and, $d_i$ being $i$-th digit of $n$ in base $k$, just compute:

$$
Z_{k}^{-1}(n) = d_0(k-1)^{0}+d_1(k-1)^{1}+...+d_n(k-1)^{n}
$$

Thus effectively "writing down $n_{(k)}$ and reading it as it was a number in base $k-1$" - even though we allow digits equal to $k$, this operation remains well defined.

# $\pi$'s conjugate

$\pi$ has a symmetrical big brother:

$$
\Large
\begin{align}
\Pi(\color{green}{39050},\color{darkred}{1000}) & = \color{darkred}{\underbrace{1332}_{Z(y+1)}}\mspace{8mu}{{0}}\color{green}{\mspace{8mu}\underbrace{27938}_{D(x)}}.
\end{align}
$$

$\Pi$ is the obvious complement to $\pi$ wherein the *zeroless* number encodes the leading string. For $\Pi$ to remain a bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$, we now need the trailing sequence to have arbitrary strings of digits $0,1,...,9$, not just $1,2,...,9$.

Additionally, because of the $y+1$ term, we need to define a special case for $x=0$ to cover all zeroless numbers:

$$
\Pi(0,\color{darkred}{y}) = \pi(0,\color{darkred}{y}) = \color{darkred}{Z_k(y)}.
$$

## Identities with $\Pi$

There is a simple recurrence relation for $D_k(n)$:

$$
k \cdot D_k(x) = D_k(kx+1)
$$

Hence:

$$
k \cdot \Pi_{k}(x, y) = \Pi_{k}(kx + 1, y),
$$

$$
\text{for all} \  x, y \geq 0.
$$

It is hard to establish other identities due to intractability of $Z_k$ and $D_k$.

# Set identities

You might have noticed $\Pi$ reverses the placement of $x$ and $y$ within the output number.

Having $y$ consistently correspond to zeroless numbers reveals a certain set identity between $\pi$ and $\Pi$, suggesting $\Pi$ is somehow fundamentally *the* conjugate of $\pi$ and it wouldn't make sense in the other order.

Take any set of points ($S$ as in "small pi"):

$$
S_k^{n} = \{ \pi_{k}^{-1}(0), \pi_{k}^{-1}(1), \dots, \pi_{k}^{-1}(n) \}.
$$

That is to say, we invert subsequent natural numbers with some $\pi_{k}^{-1}$, progressively filling the $\mathbb{N} \times \mathbb{N}$ space up to some number $n$.

Analogously, take also the set ($B$ as in "big pi"): 

$$
B_k^{n} = \{ \Pi_{k}^{-1}(0), \Pi_{k}^{-1}(1), \dots, \Pi_{k}^{-1}(n) \}
$$

It appears that for any given $k \geq 2$, the sets become equivalent at certain values of $n$. Specifically:

$$
S_k^{n} = B_k^{n} \\ \text{if and only if:} \\ n \in \{k^2 + k - 2\} \cup \left\{ \frac{k^{m+1} - 1}{k - 1} - 1 + c \ \middle| \ 0 \leq c \leq k - 1, m \geq 0 \right\}
$$

To put it simply, the sets seem to meet at every [repunit in base $k$](https://en.wikipedia.org/wiki/Repunit), as well as at the curious value $n = k^2 + k - 2$. The former sounds logical given the fact that the bijection $\Pi \circ \pi^{-1}$ is more or less a rearranging of digits.

Let us plot this:

||
|:----:|
|![The set equivalences for consecutive repunits of 3.][5]<br>The set equivalences of $\pi_{3}^{-1}$ and $\Pi_{3}^{-1}$ for consecutive repunits of $3$.|

I first plot the black dots representing the inverses of $\pi_3$, and then plot the inverses of $\Pi_3$ in green, showing how it successively fills the same area.

# *Re-pairing* functions

On a final note, having so many pairing functions at our disposal, we may come up with infinitely many permutations of the natural numbers, e.g. any of the form $\pi_{a} \circ \pi_{b}^{-1}$.

Another example is $\Pi_{k} \circ \pi_{k}^{-1}$. Here is a plot of the case $k = 3$, or as I like to call it, the "grand piano plot":

||
|:----:|
|![The grand piano plot.][6]<br>The *grand piano plot* of $\Pi_k(\pi_{k}^{-1}(n))$, for the first $1000$ natural numbers. It is, of course, a bijection $\mathbb{N} \to \mathbb{N}$.|

One can see how the function rearranges numbers only within sets of exponentially increasing sizes.

  [1]: https://i.sstatic.net/rUZodLmk.gif
  [2]: https://i.sstatic.net/fTfcan6t.gif
  [3]: https://i.sstatic.net/2CXfSnM6.png
  [4]: https://i.sstatic.net/AJh1WfR8.gif
  [5]: https://i.sstatic.net/BH8StNXz.gif
  [6]: https://i.sstatic.net/653yVfQB.png
