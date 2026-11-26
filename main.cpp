#include <cstdint>
#include <iostream>

bool is_perfect(std::uint64_t number) {
    std::uint64_t remaining = number;
    std::uint64_t divisor_sum = 1;

    for (std::uint64_t prime = 2; prime <= remaining / prime;
         prime += (prime == 2 ? 1 : 2)) {
        if (remaining % prime != 0) {
            continue;
        }

        // Each prime power contributes 1 + p + ... + p^exponent.
        std::uint64_t power = 1;
        std::uint64_t factor_sum = 1;
        do {
            remaining /= prime;
            power *= prime;
            factor_sum += power;
        } while (remaining % prime == 0);
        divisor_sum *= factor_sum;
    }

    if (remaining > 1) {
        divisor_sum *= remaining + 1;
    }
    return divisor_sum == 2 * number;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    if (!(std::cin >> count)) {
        return 0;
    }
    while (count-- > 0) {
        std::uint64_t number;
        std::cin >> number;
        std::cout << is_perfect(number) << '\n';
    }
}
