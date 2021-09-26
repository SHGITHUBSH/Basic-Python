

My_string = "how, are, you, doing?"
print(My_string)
My_List = My_string.split(",")
print(My_List)
new_list = "".join(My_List)
print(new_list)


#Remember how to write this timer part because it's good for using it to check if you write program in a clean and
#fast way that saves memory data

from timeit import default_timer as timer
start = timer()

A_List = ["a"]*6
B_List = "".join(A_List)
print(B_List)

stop = timer()
print(stop-start)


start = timer()

my_string = ""
for i in A_List:
    my_string += i
print(my_string)

stop = timer()
print(stop-start)

#.format method & f-string

var = 3.1515151515
var2 = 2.15155
Sentence = "I finished {:.3f} and {:.4f}".format(var,var2)
print (Sentence)
Sentence2 = f"I finished {var} and {var2}"
print(Sentence2)
Sentence3 = f"I finished {var*2} and {var2*3}"
print(Sentence3)





