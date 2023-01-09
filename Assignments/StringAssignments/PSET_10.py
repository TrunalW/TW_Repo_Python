""" Write and test a script that accepts user input using the input()
function and displays the result of trying to .find()
a particular letter in that input.
"""
txt = input("Enter sample text : \n")
subtxt = input("Enter the which you want to find in above sample : \n")
output = txt.find(subtxt)
print(f"if output is -1 then letter is not present.output: {output}")
