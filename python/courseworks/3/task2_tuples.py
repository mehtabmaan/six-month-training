def create_mixed_tuple(s, i, f, b):
    return (s, int(i), float(f), b.lower() == 'true')

def get_specific_element(num_tuple, index):
    if index < len(num_tuple):
        return num_tuple[index]
    return "Index out of range"

def get_fourth_from_end(any_tuple):
    if len(any_tuple) >= 4:
        return any_tuple[-4]
    return "Tuple is too short to retrieve the 4th element from the end."

def add_item_to_tuple(existing_tuple, new_item):
    temp_list = list(existing_tuple)
    temp_list.append(new_item)
    return tuple(temp_list)

def convert_tuple_to_dict(data_tuple):
    result_dict = {}
    for index, value in enumerate(data_tuple):
        result_dict[index] = value
    return result_dict

def replace_last_element_in_list(list_of_tuples, replacement_value):
    new_list = []
    for t in list_of_tuples:
        temp_list = list(t)
        if len(temp_list) > 0:
            temp_list[-1] = replacement_value
        new_list.append(tuple(temp_list))
    return new_list

if __name__ == "__main__":
    val_s = input("Enter a string: ")
    val_i = input("Enter an integer: ")
    val_f = input("Enter a float: ")
    val_b = input("Enter a boolean (True/False): ")
    mixed = create_mixed_tuple(val_s, val_i, val_f, val_b)
    print(f"Mixed Tuple: {mixed}")

    nums_input = input("Enter at least 5 numbers separated by space: ")
    num_tuple = tuple(int(x) for x in nums_input.split())
    print(f"Element at index 2: {get_specific_element(num_tuple, 2)}")
    print(f"4th from end: {get_fourth_from_end(num_tuple)}")

    extra_item = input("Enter an item to add to the number tuple: ")
    updated_tuple = add_item_to_tuple(num_tuple, extra_item)
    print(f"Updated Tuple: {updated_tuple}")

    dictionary_version = convert_tuple_to_dict(num_tuple)
    print(f"Dictionary from tuple: {dictionary_version}")

    print("\nProcessing list of tuples replacement...")
    sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    replace_val = int(input("Enter replacement value for the last elements: "))
    transformed_list = replace_last_element_in_list(sample_list, replace_val)
    print(f"Original: {sample_list}")
    print(f"Transformed: {transformed_list}")