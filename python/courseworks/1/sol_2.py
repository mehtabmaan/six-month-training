def unique_characters(str):
    unique_chars =[]
    for i in str:
        if i not in unique_chars:
            unique_chars.append(i)
    return unique_chars

str = input('Enter the text :')
print("".join(unique_characters(str)))
