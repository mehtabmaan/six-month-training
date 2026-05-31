def length_lst(lst):
    count=0
    for i in lst:
        count+=1
    return count

def multiply_eles(lst,len):
    ans=1
    for i in range(len):
        ans*=lst[i]
    return ans

def Maximum_num(lst,len):
    max=float('-inf')
    for i in range (len):
        if lst[i]>max:
            max=lst[i]
    return max

def smallest_num(lst,len):
    min=float('inf')
    for i in range (len):
        if lst[i]<min:
            min=lst[i]
    return min

def Remove_duplicates(lst,len):
    temp=[]
    result=[]
    for i in lst:
        if i not in temp:
            temp.append(i)
            result.append(i)
    return result

def check_empty(lst,len):
    if len==0:
        return f"List is empty."
    return f"List is not empty."

def largest_odd(lst,len):
    odd_lst=[x for x in lst if x%2!=0]
    len=length_lst(odd_lst)
    if len:
        return Maximum_num(odd_lst,len)
    return f'No odd numbers found'

def remove_indexes(lst,len):
    remove=[5,4,0]
    for i in remove:
        if i<length_lst(lst) and length_lst(lst)!=0:
            del lst[i]
    return  lst

lst=[11,6,9]
len=length_lst(lst)



