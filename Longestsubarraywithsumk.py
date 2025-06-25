from typing import List
def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a)
    length = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s+= a[k]
                if s == k:
                    length = max(length, j - i + 1)
        return length
    if __name__ == "__main__":
        a = [-1,1,1]
        k = 1
        length = getLongestSubarray(a, k)
        print(f"The length of the longest subarray is: {length}")
        
# Better approach 
from typing import List
def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a)
    length = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == k:
                length = max(length,j - i + 1)
                return length
if __name__ == '__main__':
    a = [-1,1,1]
    k = 1
    len = getLongestSubarray(a,  k)
    print("The length of the longest subarray is:", len)
            
            