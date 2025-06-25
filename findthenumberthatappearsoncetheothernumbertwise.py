def getSingleElement(arr):
    # Size of the array:
    n = len(arr)
    # Run a loop for selecting elements:
    for i in range(n):
        num = arr[i]  # selected element
        cnt = 0

        # Find the occurrence using linear search:
        for j in range(n):
            if arr[j] == num:
                cnt += 1
        # If the occurrence is 1, return the number:
        if cnt == 1:
            return num
    # This line will never execute
    # if the array contains a single element.
    return -1
def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)
if __name__ == '__main__':
    main()


#  Better Approach
def  getSingleElement(arr):
    n = len(arr)#size of array
    hashmap = {} #empty map
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
    for num, count in hashmap.items():
        if count == 1:
            return num
    return -1
def main():
    arr = [4,1,2,1,2]
    print("The single element is:", ans)
if __name__ == "__main__":
    main()

# Optimal XOR Code
def getSingleElement(arr):
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr
def main():
    arr = [4,1,2,1,2]
    ans = getSingleElement(arr)
    print("The single element is:",ans)
if __name__ == "__main__":
    main()
    
      