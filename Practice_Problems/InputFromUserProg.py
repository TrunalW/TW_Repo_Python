#Program to take input from enduser
# and the use it in print function

##START
name = input("Enter your name \n")

print("welcome to python world:",name)

""" USing concatenation operator
+ operator to append string
also using f-string way """

print("welcome to python world : "+name)

#using .format
print("Welcome to python world : {} this is done using .format".format(name))

print("Welcome to python world : {} this is done using .format iserting second variable {}".format(name,'sampleText'))

#using FString literal
print(f'name is {name}also another statement is appended {"sample"} this is done using f String literal way')



