a, k, b, m, n= map(int,input().split())
def binary_search():
    first=0
    last=int(10**18)
    result = 0
    while first <= last:
        mid= (first + last)//2
        if a * (mid-mid//k) + b * (mid-mid//m) >= n:
            last=mid-1
            result=mid
        else:
            first=mid+1
    return result
print(binary_search())
