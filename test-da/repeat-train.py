list = ["Xaxa", "asdf", "wfea"]
new_list = list[:]
del list[:]

print("\nDelete list")
for i in list:
    print(i)

print("\nNew List")
for j in new_list:
    print(j)

print("\nList")
for i in list:
    print(i)

list = ["Xaxa", "asdf", "wfea"]
print(list[:])
