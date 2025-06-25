def bubble_sort(arr,n):
    for i in range(n-1, -1, -1):
        for j in range(0,i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("After bubble sort:", end=" ")
        for i in range(n):
            print(arr[i],end=" ")
        print()
if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    print("Before using bubble sort:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    bubble_sort(arr, n)