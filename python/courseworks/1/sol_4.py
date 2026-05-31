def num_len(num):
    count=0
    if num==0:
        count=1
    
    i=num
    while(i>0):
        i=i//10
        count+=1
    return count

num=int(input("Input :"))
print(f'Output :{num_len(num)}')
