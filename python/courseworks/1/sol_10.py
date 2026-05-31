def count(str):
    v_cnt=0
    vowels=['A','a','E','e','i','I','o','O','U','u']
    for i in str:
        if i in vowels:
            v_cnt+=1
    c_cnt=len(str)-v_cnt
    return v_cnt,c_cnt

str=input('Input :')
x,y=count(str)
print(f'Vowels:{x} \nConsonents:{y}')




