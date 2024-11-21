def fibonacci(n: int) -> int:
    if n < 0:
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

print(celsius_to_fahrenheit(-10))
print(fahrenheit_to_celsius(-104))