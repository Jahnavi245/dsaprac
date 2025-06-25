def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    print("After insertion sort:", arr)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before insertion sort:", arr)
    insertion_sort(arr)
