def sum(n):
    num=0
    sum=0
    for i in range (n):
        num += (2*(10**i))
        sum += num
    return sum


n = int(input('Input :'))
print('Output :',sum(n))