def median(num1,num2,num3):
     lst=[num1,num2,num3]
     lst.sort()
     mid=int((len(lst)-1-0)/2)
     return lst[mid]

num1=int(input('Input first number :'))
num2=int(input('Input second number :'))
num3=int(input('Input third number :'))
print(f'Output :{median(num1,num2,num3)}')
