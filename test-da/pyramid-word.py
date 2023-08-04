my_str = input("Insert word : ")
x = 0

print("PYRAMID WORD")
for i in my_str:
    x = x + 1
    print(str.upper(my_str[0:x]))

for j in my_str:
    x = x - 1
    print(str.upper(my_str[0:x]))
