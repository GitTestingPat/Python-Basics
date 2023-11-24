

# This function checks if a number is prime or not.
def is_prime(n):
    # If the number is less than 2, it is not prime.
    if n < 2:
        return False

    # If the number is 2, it is prime.
    if n == 2:
        return True

    # If the number is divisible by 2, it is not prime.
    if n % 2 == 0:
        return False

    # Start checking from 3 to the square root of the number.
    for i in range(3, int(n**0.5) + 1, 2):
        # If the number is divisible by any number in this range, it is not prime.
        if n % i == 0:
            return False

    # If the number is not divisible by any number in the range, it is prime.
    return True

# This function generates a list of prime numbers within a given range.
def generate_primes(start, end):
    # Create an empty list to store the prime numbers.
    primes = []