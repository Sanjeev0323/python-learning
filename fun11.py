def pali(s):
    return s == s[::-1]
s = input("enter a string: ")
r = pali(s)
print("pali",r)
