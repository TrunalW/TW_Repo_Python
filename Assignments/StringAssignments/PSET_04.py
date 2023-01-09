###In the string hakuna matata print the substring tata using slicing. Try with both positive and negative indices

str_sample = "hakuna matata"

###using positive indexes
print(f"given sample string : {str_sample}")
print(f"using positive index")
start_index = len(str_sample)-4
stop_index = len(str_sample)

print(f"start index : {start_index} stop index : {stop_index}")

print(f"substring : {str_sample[start_index:stop_index]}")


####using negative index
print(f"using negative index")
start_index = -4


print(f"start index : {start_index} \n stop index : no stop index default we can not give len or last index ie -1 because in this stop index is excluded")

print(f"substring : {str_sample[start_index:]}")
