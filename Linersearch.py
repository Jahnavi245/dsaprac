def search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i 
    return -1
def main():
    arr = [1,2,3,4,5]
    num = 4
    n = len(arr)
    val = search(arr, n, num)
    print(val)
main()
