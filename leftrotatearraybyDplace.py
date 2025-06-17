def rotate_to_right(arr, k):
    n = len(arr)
    if n == 0:
        return 
    k = k % n
    if k > n:
        return
    
    temp = arr[-k:]
    for i in range(n - k -1, -1):
        arr[i + k] = arr[i]
    for i in range(k):
        arr[i] = temp[i]
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_to_right(arr, k)
print("After Rotating the element to right") 
print(arr)

def rotate_to_left(arr, k):
    n = len(arr)
    if n == 0:
        return
    k = k % n
    if k > n:
        return
    temp = arr[-k:]
    for i in range(n - k -1, -1):
        arr[i + k] = arr[i]
        for i in range(k):
            arr[i] = temp[i]
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_to_left(arr, k)
print("After Rotating the element to left")
print(arr)            
            