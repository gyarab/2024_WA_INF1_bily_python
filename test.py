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
    # generátorová funkce - vrací znaky, které jsou alfanumerické
    text = ''.join(c for c in text if c.isalpha())
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return {"vowels": vowel_count, "consonants": consonant_count}

def class_and_break_time(start_class: int, end_class: int) -> tuple:
    if not isinstance(start_class, int) or not isinstance(end_class, int) or start_class < 0 or end_class < 0:
        raise ValueError("Both arguments must be positive integers.")
    
    if start_class > end_class:
        raise ValueError("Start class cannot be after end class.")
    
    if start_class > 12 or end_class > 12:
        raise ValueError("Class hours cannot exceed 12.")
    
    class_duration = (end_class - start_class + 1) * 45
    
    break_times = [0, 5, 10, 20, 10, 10, 5, 5, 10, 10, 5, 5]
    # Adjust indexing for 1-based to 0-based
    break_duration = sum(break_times[start_class:end_class])
    
    return class_duration, break_duration

# domáčák - domácí úkol
import re

def css_color_to_rgb(color):
    if not isinstance(color, str):
        raise ValueError("Input must be a string.")
    
    # Remove whitespace from the color string
    color = color.replace(" ", "")
    
    # Check if the color is in hexadecimal format
    if re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", color):
        if len(color) == 4:
            # Expand shorthand hexadecimal color to full format
            color = "#" + color[1] * 2 + color[2] * 2 + color[3] * 2
        
        # Convert hexadecimal color to RGB
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        return r, g, b
    
    # Check if the color is in RGB format
    if re.match(r"^rgb\(\d{1,3},\d{1,3},\d{1,3}\)$", color):
        # Extract RGB values from the string
        r, g, b = map(int, color[4:-1].split(","))
        
        return r, g, b
    
    # Check if the color is in named format
    named_colors = {
        "aliceblue": (240, 248, 255),
        "antiquewhite": (250, 235, 215),
        "aqua": (0, 255, 255),
        "aquamarine": (127, 255, 212),
        # Add more named colors here
    }
    
    if color.lower() in named_colors:
        return named_colors[color.lower()]
    
    # If the color format is not recognized, raise an error
    raise ValueError("Invalid color format.")
