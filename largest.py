# broute force approch
from typing import List

def sortArr(arr: List[int]) -> int:
    arr.sort()  # numbers ni smallest nundi biggest varaku arrange chestundi
    return arr[-1]  # last lo biggest number untundi

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))

def findLargestElement(arr, n):
    max = arr[0]  # first element ni biggest ani assume chestham
    for i in range(0, n):  # anni numbers check chestham
        if (max < arr[i]):  # okavela ee number max kanna peddha undhi ante
            max = arr[i]    # max ni update chestham
    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    
    max1 = findLargestElement(arr1, len(arr1))
    print("The largest element in the array is:", max1)

    max2 = findLargestElement(arr2, len(arr2))
    print("The largest element in the array is:", max2)
