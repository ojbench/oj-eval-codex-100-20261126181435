"""Compare the executable with an independent proper-divisor sieve."""

import pathlib
import subprocess
import sys


executable = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "./code").resolve()


def check(numbers, expected):
    data = f"{len(numbers)}\n" + " ".join(map(str, numbers)) + "\n"
    result = subprocess.run(
        [str(executable)], input=data, text=True, capture_output=True, check=True
    )
    assert list(map(int, result.stdout.split())) == expected, (numbers, result.stdout)


limit = 10000
sums = [0] * (limit + 1)
for divisor in range(1, limit // 2 + 1):
    for multiple in range(2 * divisor, limit + 1, divisor):
        sums[multiple] += divisor
for start in range(1, limit + 1, 10):
    numbers = list(range(start, min(start + 10, limit + 1)))
    check(numbers, [int(sums[n] == n) for n in numbers])

check([4, 14, 4, 5, 6], [0, 0, 0, 0, 1])
check([6, 28, 496, 8128, 33550336, 8589869056, 137438691328], [1] * 7)
check([1, 10**12, 999983**2, 2**39, 3**25, 999999999989], [0] * 6)
check([999999999989] * 10, [0] * 10)
print("Passed exhaustive checks through 10000, sample, and large boundary cases.")
