def rev_num(num):
    rev_num=0
    for i in range(len(str(num))):
        remainder=num%10
        rev_num= (rev_num*10) + remainder
        num=int(num/10)
    return rev_num

n=int(input("Input :"))
print(f'Output :{rev_num(n)}')
