#Codelearn.io/jiswoo
#Nhom 15 CS112.L12.KHCL


Mod = 10**9 + 7

def fibonaci(n):

    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]

def multiply(F, M):
    global Mod
    x = (F[0][0] * M[0][0] % Mod +
         F[0][1] * M[1][0] % Mod) % Mod
    y = (F[0][0] * M[0][1] % Mod +
         F[0][1] * M[1][1] % Mod) % Mod
    z = (F[1][0] * M[0][0] % Mod +
         F[1][1] * M[1][0] % Mod) % Mod
    w = (F[1][0] * M[0][1] % Mod+
         F[1][1] * M[1][1] % Mod) % Mod

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):

    if( n == 0 or n == 1):
        return;
    M = [[1, 1],
         [1, 0]];

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)


n, k = map(int,input().split())
fib = fibonaci(2*k + 1)
arr = (n*fib) % Mod
print(arr)
