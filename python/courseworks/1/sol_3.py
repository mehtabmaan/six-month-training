def divisibility_check(lst):
    new_lst=[]
    for i in lst:
        if i%5==0:
            if i>500:
                break
            if i>150:
                continue
            new_lst.append(i)
    return new_lst

lst=[14,85,625,75]
print(divisibility_check(lst))

        