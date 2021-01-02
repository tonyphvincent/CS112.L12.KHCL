s =str(input())
q = int (input())
Hash = [0]


for char in s:
    Hash.append(Hash[len(Hash) -1] + 31 ** (ord(char) - ord('a')))

ans = []
for i in range (q):
    a,b,c,d = map (int,input().split())
    if  Hash[b] - Hash[a-1] == Hash[d] -Hash[c-1]:
        ans.append("YES")
    else:
        ans.append("NO")

print ("\n".join(ans))

# Input:
# abcbacaac
# 2
# 1 3 4 6
# 1 3 5 7
# Output:
# YES
# NO
