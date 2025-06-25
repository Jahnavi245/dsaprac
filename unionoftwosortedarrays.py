def find_union(arr1, arr2):
    s = set()
    union = []
    
    for num in arr1:
         s.add(num)
    for num in arr2:
        s.add(num)
    for num in s:
        union.append(num)
    return union