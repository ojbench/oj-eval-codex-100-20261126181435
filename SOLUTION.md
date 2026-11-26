# Perfect numbers

Factor each input n by trial division, removing all copies of each factor.
For a prime power p^a, the sum of its divisors is 1 + p + ... + p^a.
Multiplying these sums gives sigma(n), since each divisor uniquely chooses
an exponent for every prime factor. Any remainder greater than one after
trial division is prime and contributes remainder + 1.

The sum of proper divisors is sigma(n) - n, so output whether sigma(n) = 2n.
For n = 1 the product is 1, correctly producing false.

Time is O(sqrt(n)) per input and auxiliary space is O(1). All arithmetic
uses uint64_t. For n <= 10^12, sigma(n) <= n(1 + ln(n)) < 2.9 * 10^13,
so the divisor sums and their partial products fit comfortably.

Build with `cmake . && make`. Run local checks with
`python3 tests/test_solution.py ./code`.
