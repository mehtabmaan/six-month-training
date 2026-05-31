def odd_index(num_lst):
    odd_n=[num_lst[i] for i in range(len(num_lst)) if i%2!=0]
    return odd_n

num_lst=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f'Iutput :{num_lst}')
print(f'Output :{odd_index(num_lst)}')