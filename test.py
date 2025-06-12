def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True



def get_primes(limit):

    return [num for num in range(2, limit + 1) if is_prime(num)]



# Example usage

limit = 30

primes = get_primes(limit)

print(f"Prime numbers up to {limit}: {primes}")