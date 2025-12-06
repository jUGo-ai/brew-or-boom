# print("Hello World")

import time

def print_slowly(text, delay=0.1):
    """
    Prints a string character by character with a specified delay.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print() # Add a newline after the entire text is printed

# Usage:
print_slowly("Hello, this is a slow-typing effect in Python!")
print_slowly("You can adjust the delay for different speeds.", delay=0.05)