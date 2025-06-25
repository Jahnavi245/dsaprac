def missingNumber(a, N):
    hash = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i 
    return -1
def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)
if __name__ == '__main__':
    main() 
    