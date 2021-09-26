#Tuples. Tuple compared to list, you cannot use other function to edit the elemenet within the data list.
#Tuples must be created more than one element, or you need to at least add a coma to make it work
Coordinates = [(2,3), (2,5), (3,7)]
print(Coordinates)
print(Coordinates[0])
print(Coordinates[:])
print(Coordinates[:2])
print(Coordinates[-1:])
print(Coordinates[:-1])
print("\n")

#Unpack turple
My_tuple = "Max", 28, "Boston"
Name, Age, Location = My_tuple
print(Name)
print(Age)
print(Location)

#Partial unpack with * symbol
Tuple_Data = (1,3,5,7,9)
i1, *i2, i3 = Tuple_Data
print(i1)
print(i2)
print(i3)

#Tuple can be more efficient than list, but it's unmmutable
import sys
my_list = [0,1,2, "hello", True]
my_tuple = (0,1,2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")