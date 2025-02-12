#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool* calculate_primes(int n) {
    bool *primes = malloc((n + 1) * sizeof(bool));
    if (!primes) {
        return NULL; // Ошибка выделения памяти
    }

    for (int i = 0; i <= n; i++) {
        primes[i] = true;
    }
    primes[0] = primes[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (primes[p]) {
            for (int i = p * p; i <= n; i += p) {
                primes[i] = false;
            }
        }
    }
    return primes;
}

void free_memory(bool *ptr) {
    free(ptr);
}

