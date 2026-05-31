def sort_dict_by_value(d):
    items = list(d.items())
    asc = dict(sorted(items, key=lambda x: x[1]))
    desc = dict(sorted(items, key=lambda x: x[1], reverse=True))
    return asc, desc

def get_keys(d):
    return [k for k in d.keys()]

def get_values(d):
    return [v for v in d.values()]

def get_items(d):
    return [(k, v) for k, v in d.items()]

def merge_two_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def calculate_stats(d):
    total_sum = 0
    total_prod = 1
    if not d:
        return 0, 0
    for v in d.values():
        total_sum += v
        total_prod *= v
    return total_sum, total_prod

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def remove_duplicate_values(d):
    result = {}
    seen_values = set()
    for k, v in d.items():
        if v not in seen_values:
            result[k] = v
            seen_values.add(v)
    return result

if __name__ == "__main__":
    entries1 = input("Enter first dictionary (key:value pairs separated by spaces, e.g., a:10 b:20): ")
    dict1 = {}
    if entries1.strip():
        for pair in entries1.split():
            k, v = pair.split(':')
            dict1[k] = float(v)

    if dict1:
        asc_v, desc_v = sort_dict_by_value(dict1)
        print(f"Sorted by Value (Asc): {asc_v}")
        print(f"Sorted by Value (Desc): {desc_v}")

    print(f"Keys: {get_keys(dict1)}")
    print(f"Values: {get_values(dict1)}")
    print(f"Pairs: {get_items(dict1)}")

    entries2 = input("Enter second dictionary to merge (e.g., c:30 b:40): ")
    dict2 = {}
    if entries2.strip():
        for pair in entries2.split():
            k, v = pair.split(':')
            dict2[k] = float(v)

    merged = merge_two_dicts(dict1, dict2)
    print(f"Merged Dictionary: {merged}")

    s, p = calculate_stats(dict1)
    print(f"Sum of values: {s}")
    print(f"Product of values: {p}")

    print(f"Sorted by Key: {sort_dict_by_key(dict1)}")

    print(f"Dictionary after removing duplicate values: {remove_duplicate_values(dict1)}")