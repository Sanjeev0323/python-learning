def order(i,q,p=0):
 t=q*p
 print(f"order summary: {q} * {i}")
 print(f"total price is: {t}")
 print("positional argument is:")
 return t
print("keyword argument is:")
order(q=3,p=10,i="food")
print("default argument is:")
order(4,"burger")





#Write a function student_record(name, *marks, **details) that:
#Student name
#All marks (from *args)
#Additional details (from **kwargs)
 #Tasks
#Call the function with:
#student_record("Arun", 85, 90, 78, city="Chennai", age=20)
#Add more marks and extra details
#Modify the function to calculate and print average marks
#