def sq (n):
    lst=[x**2 for x in range(n)]
    return lst

num = int (input("Enter a number: "))
print(sq(num))
