def romanToInt(s):

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    while i < len(s):

        # If this is the last character
        if i == len(s) - 1:
            total = total + values[s[i]]
            i = i + 1

        else:
            current = values[s[i]]
            next_value = values[s[i + 1]]

            if current < next_value:
                total = total + (next_value - current)
                i = i + 2   
            else:
                total = total + current
                i = i + 1

    return total


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))