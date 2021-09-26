#If Statements
Taller_than_the_other_gender = True
More_muscular = False
Grow_beard = True
if Taller_than_the_other_gender or More_muscular or Grow_beard:
    print("You have possibility to be a male.")
elif Taller_than_the_other_gender and not More_muscular and not Grow_beard:
    print("You might be a girly man.")
else:
    print("You are not a male.")
print("\n")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(5,7,4))
print("\n")