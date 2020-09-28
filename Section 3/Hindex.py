def hindex(n):
    n.sort()        
    for i in range(len(n)):
        temp = len(n) - i
        if temp <= n[i]:
            return temp
    return 0

m =input()
n = [int(x) for x in input().split()]
print(hindex(n))
