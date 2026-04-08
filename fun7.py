def vow(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return (count)
s = input("enter a string: ")
r = vow(s)
print("The number of vowels in the string is:", r)