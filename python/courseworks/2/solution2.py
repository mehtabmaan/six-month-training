def merge(arr, left, mid, right):
    
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_part):
        if left_part[i] < 0:
            arr[k] = left_part[i]
            k += 1
        i += 1

    while j < len(right_part):
        if right_part[j] < 0:
            arr[k] = right_part[j]
            k += 1
        j += 1

    i = j = 0

    while i < len(left_part):
        if left_part[i] >= 0:
            arr[k] = left_part[i]
            k += 1
        i += 1

    while j < len(right_part):
        if right_part[j] >= 0:
            arr[k] = right_part[j]
            k += 1
        j += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def rearrange_negatives(arr):
    merge_sort(arr, 0, len(arr) - 1)
    return arr

arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange_negatives(arr1))

arr2 = [-12, 11, 13, -5, 6, -7, 5, -3, 8]
print(rearrange_negatives(arr2))