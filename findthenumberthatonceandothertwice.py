def getSingleElement(arr):
    n = len(arr)
    maxi = max(arr)
    hash = [0] * (maxi + 1)
    for num in arr:
        hash[num] +=1
    for num in arr:
        if hash[num] == 1:
            return num
    return -1
def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)
if __name__ == '__main__':
    main()
    