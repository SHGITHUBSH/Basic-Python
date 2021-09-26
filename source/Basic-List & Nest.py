#List, not mutable
Friends = ["Mary","Peter","Jack", "John"]
print(Friends[0])
print(Friends[1])
print(Friends[2])
print(Friends[3])
#Negative sign will make the string point the value from the very last one
print(Friends[-1])
print(Friends[-2])
print(Friends[-3])
print(Friends[:])
#Select range of list (or what we called data set), select 0 to 3, will only include 0 to 2 somehow
print(Friends[0:3])
#Update the value in the bracket
Friends[1]="Babara"
print(Friends[1])
print("\n")
#List Function (extend)
lucky_numbers = [4,6,7,8,9]
friends = ["Josh", "Martin", "Luther", "Vann", "Vann"]
#sort in alphat order and ascending  order for the elements
print(friends.sort())
#extend
friends.extend(lucky_numbers)
print(friends.index("Martin"))
print(friends)
#append (add more element in the end of data set
friends.append("Craig")
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Martin")
print(friends)
#pop erase the very last element in the list
friends.pop()
print(friends)
#clear cleans everything out
friends.clear()
print(friends)
#count same value
print(friends.count("Vann"))
#Revese order of the elements in data set
Sky = ["Cloud", "Sun", "Stars"]
print (Sky)
Sky.reverse()
print(Sky)
#Copy of the data set
Sky2 = Sky.copy()
print(Sky2)
print("\n")

#2D List & Nest Loop
Number_Grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(Number_Grid)
print(Number_Grid[0][2])
print(Number_Grid[2][0])
print("\n")

Number_Grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for row in Number_Grid:
    for col in row:
        print(col)
print("\n")

List = [1,2]*5
print(List)

my_list = [1,2,3,4,5]
x = [x*x for x in my_list]
print(x)