def isPalindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if rev == original:
        return "Palindrome"
    else:
        return "Not a palindrome"
N = 4554
print("Input:", N)
print("Output:", isPalindrome(N))