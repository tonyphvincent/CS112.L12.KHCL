s = str(input())
q = int (input())
flag = ["NO"]*q

def check (s, a,b,c,d):
    s1 = sorted( s[a-1:b])
    s2 = sorted( s[c-1:d])
    return s1==s2
# print (check(s, a,b,c,d))
for i in range (q):
    a,b,c,d = map (int, input().split())
    if check(s,a,b,c,d) ==True:
        flag[i] = "YES"

for i in flag:
    print (i)
    
# Input:
#abcbacaac
#2
#1 3 4 6
#1 3 5 7
# Output:
# YES
# NO
