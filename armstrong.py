def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    return total == n
print("Input: 153 ->", is_armstrong(153))
print("Input: 9474 ->", is_armstrong(9474))




