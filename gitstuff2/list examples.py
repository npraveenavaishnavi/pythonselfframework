#list in python
values=[1, 2, "amritha", 3, 4]
print(values)
#list is a datatype that allows multiple values and can be different datatypes
print(values[2])  #index number of value is printed

print(values[-1])  #-1 is defined to display the last index of your list

print(values[1:3])  #[a:d] is used to display the sublist of the array

values.insert(3, "varshini")   #.insert is used to insert values between the array
print(values)

values.append("End of the list")   #.append is used to add new value at end
print(values)

values[2]="AMRITHA"  #to update, use value[index number]="updated value"
print(values)

del values[2]   #to delete any value use"del"
print(values)

# TUPLE is same as LIST datatype but it is immutable
values1 = [1, 2, "amritha", 3.4]
print(values1[1])

values1[2]= "AMRITHA"
print(values1)

#dictionary key:value
dic={"a":2 ,4:"bcd" , "c":"HELLO WORLD"}
print(dic["c"])
print(dic[4])


#dictionary
dict = {}
dict["first name "]="praveena"
dict["last name"]="nageswaran"
print(dict)
print(dict["last name"])

