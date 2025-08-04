def print_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def main():
    number = 28
    divisors = print_divisors(number)
    print(f"Divisors of {number} are: ", end="")
    for d in divisors:
        print(d, end=" ")  # print all in one line

if __name__ == "__main__":
    main()
    
    
    