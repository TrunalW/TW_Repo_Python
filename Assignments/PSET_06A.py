"""###
Write a python script that reads the first and last name of a person and
concatenates them to form a full name.
Also, write a script such that a space character is added post concatenation by detecting the casing of the strings.
"""

first_name = input("Enter your first name : \n")
last_name = input("Enter your last name : \n")

full_name = first_name+" "+last_name

print(f'Full name with space in between is : {full_name}')
