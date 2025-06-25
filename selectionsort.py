def selection_sort(arr, n):
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        #swap
        arr[mini], arr[i] = arr[i], arr[mini]
    print("After selection sort:", end=" ")
    for i in range(n):
        print(arr[i],end=" ")
    print()
if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    print("Before selection sort:", end=" ")
    for i in range(n):
        print(arr[i],end=" ")
    print()
    selection_sort(arr,n)


        