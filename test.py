import math
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
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1
        
def rotate_array(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int):
        raise ValueError("Both arguments must be a list and an integer.")
    if n < 0:
        n = len(arr) - abs(n) % len(arr)
    elif n > 0:
        n = n % len(arr)
    rotated_arr = []
    for i in range(len(arr)):
        rotated_arr.append(arr[(i - n) % len(arr)])
    return rotated_arr

def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if len(text) % 3 == 0:
        return [text[i:i+3] for i in range(0, len(text), 3)]
    else:
        last_chunk = text[-(len(text) % 3):] if len(text) > 3 else text
        return [text[i:i+3] for i in range(0, len(text) - (len(text) % 3), 3)] + [last_chunk]


def vowels_and_consonants(text):
            if not isinstance(text, str):
                raise ValueError("Input must be a string.")
            
            vowels = "aeiouáéíóúůý"
            consonants = "bcčdďfghjklmnpqrřsštťvwxzž"
            
            text = text.lower()
            text = ''.join(c for c in text if c.isalpha())
            
            vowel_count = 0
            consonant_count = 0
            
            for char in text:
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1
            
            return {"vowels": vowel_count, "consonants": consonant_count}