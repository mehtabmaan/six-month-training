def length_lst(lst):
    count = 0
    for i in lst:
        count += 1
    return count

def multiply_eles(lst, list_len):
    if list_len == 0:
        return 0
    ans = 1
    for i in range(list_len):
        ans *= lst[i]
    return ans

def maximum_num(lst, list_len):
    if list_len == 0:
        return None
    max_val = float('-inf')
    for i in range(list_len):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

def smallest_num(lst, list_len):
    if list_len == 0:
        return None
    min_val = float('inf')
    for i in range(list_len):
        if lst[i] < min_val:
            min_val = lst[i]
    return min_val

def remove_duplicates(lst):
    seen = set()
    result = []
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result

def check_empty(list_len):
    if list_len == 0:
        return "List is empty."
    return "List is not empty."

def largest_odd(lst):
    odd_lst = [x for x in lst if x % 2 != 0]
    size = length_lst(odd_lst)
    if size > 0:
        return maximum_num(odd_lst, size)
    return "No odd numbers found"

def remove_specific_indexes(lst):
    copy_lst = list(lst)
    remove_indices = [5, 4, 0]
    for i in remove_indices:
        if i < length_lst(copy_lst):
            del copy_lst[i]
    return copy_lst

def sort_tuple_list(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])

def count_lowercase_letters(word_list):
    total = 0
    for word in word_list:
        for char in word:
            if 'a' <= char <= 'z':
                total += 1
    return total

def extract_exactly_k_consecutive(lst, k):
    result = []
    n = length_lst(lst)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and lst[i] == lst[i+1]:
            count += 1
            i += 1
        if count == k:
            result.append(lst[i])
        i += 1
    return result

if __name__ == "__main__":
    user_input = input("Enter a list of integers separated by spaces: ")
    int_list = [int(x) for x in user_input.split()]
    n = length_lst(int_list)

    print(f"Product of items: {multiply_eles(int_list, n)}")
    print(f"Largest number: {maximum_num(int_list, n)}")
    print(f"Smallest number: {smallest_num(int_list, n)}")
    print(f"Duplicates removed: {remove_duplicates(int_list)}")
    print(check_empty(n))
    print(f"Largest odd number: {largest_odd(int_list)}")
    print(f"List after removing indexes 0, 4, 5: {remove_specific_indexes(int_list)}")

    tuple_input = input("Enter tuples like (1,3) (2,1) separated by spaces: ")
    raw_tuples = tuple_input.replace('(', '').replace(')', '').split()
    tuple_list = []
    for i in range(0, length_lst(raw_tuples), 2):
        tuple_list.append((int(raw_tuples[i]), int(raw_tuples[i+1])))
    print(f"Sorted tuples: {sort_tuple_list(tuple_list)}")

    words_input = input("Enter words separated by spaces: ")
    word_list = words_input.split()
    print(f"Total lowercase letters: {count_lowercase_letters(word_list)}")

    k_val = int(input("Enter value for k (consecutive count): "))
    print(f"Elements appearing exactly {k_val} times consecutively: {extract_exactly_k_consecutive(int_list, k_val)}")