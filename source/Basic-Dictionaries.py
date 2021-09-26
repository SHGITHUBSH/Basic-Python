#Dictionaries
Month_Conversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
print(Month_Conversion[input("Enter Month Initial: ")])

for key in Month_Conversion.keys():
    print(key)
for value in Month_Conversion.values():
    print(value)
for key, value in Month_Conversion.items():
    print(key, value)

# Add dictionary data into storage
Month_Conversion["正月"] = "一月"
print(Month_Conversion)
print("\n")

#Colleciton mudule's counter feature
from collections import Counter
a = "aaaaaabbbbcc"
My_Counter = Counter(a)
print(My_Counter)
print(My_Counter.keys())
print(My_Counter.values())
print(My_Counter.most_common(1))
print(My_Counter.most_common(2))
print(My_Counter.most_common(1)[0])
print(My_Counter.most_common(1)[0][0])
print(list(My_Counter.elements()))