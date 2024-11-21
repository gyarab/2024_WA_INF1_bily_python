from typing import List


def fibonacci(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
    
def celsius_to_fahrenheit(celsius: float) -> float:
        if not isinstance(celsius, (int, float)):
            raise ValueError("Input must be a number.")
        return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError("Input must be a number.")
        return (fahrenheit - 32) * 5/9

def is_prime(n: int) -> bool:
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a natural number.")
    if i == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(a: int, b: int) -> List[int]:
        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise ValueError("Both inputs must be non-negative integers.")
        if b < a:
            a, b = b, a
        primes = []
        for num in range(a, b + 1):
            if is_prime(num):
                primes.append(num)
        return primes