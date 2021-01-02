n = int(input())

max_num = n // 3

remainder = n % 3

if(remainder == 0):
    print(max_num * 7)
elif(remainder == 1):
    print((max_num - 1) * 7 + 4)
elif(remainder == 2):
    print(max_num * 7 + 1)
