def test():Add commentMore actions
    pass
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage
if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Is 7 prime?", is_prime(7))