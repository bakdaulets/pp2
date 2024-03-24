import time 
from math import sqrt
numbers = int(input())
delay_ms = int(input())
def calculate_square(number, delay_ms):
    time.sleep(delay_ms / 1000.0) 
    result = sqrt(number)
    return f"Square root of {number} after {delay_ms} milliseconds is {result}"
a = calculate_square(numbers, delay_ms)
print(a)