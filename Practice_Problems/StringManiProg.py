####String indexing and slicing practise

str_name = "This is sample text Sample"
str_val = "PythonWorld"
str_param = "Parameter"

var = str_name[0]
print(f"element at zero index : {str_name[0]}")
print(f"element at last  index  that is lenght minus one : {str_name[len(str_name)-1]}")
print(f"element at last  index  that is  using negative index -1 : {str_name[-1]}")

##lenght of string
print(len(str_param))

###Slicing
print(f"first three chars 0 to 3: {str_name[0:3]}")

###if you do not metion starting index, it default takes 0 ie start of the string
print(f"first three chars direct :3 == {str_name[:3]}")

### slicing using step param [0:3:1]
print(f"first three chars using step param  == {str_param[0:4:-2]}")


print(f"first three chars using step param  == {str_param[-1:len(str_param)]}")
### reverse the string

print(f"Reversing the string using negative step index : {str_param[::-1]}")
