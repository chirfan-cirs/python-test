list = ["1 Sleep", "2 Eat", "3 Playing"]
no = [0, 10]
print(list)

print("\nShow all list")
for i in list:
    print(f"List number {i}")

print("\nAdd list")
list.append("4 Bath")
pop = list.pop(1)
for i in list:
    print(f"List number {i}")
print(pop)

print("\nNew List")
list = ["1 Sleep", "2 Eat", "3 Playing"]
new_list = list[:]
for i in new_list:
    print(f" List number {i}")

del list[:]
print("\nDel list")
for i in new_list:
    print(f"New List number {i}")

print("\nList compre : Ganjil")
list = ["1 Sleep", "2 Eat", "3 Playing"]
new_list = list[0::2]
for i in new_list:
    print(f"New List number {i}")

print("\nList compre : Genap")
list = ["1 Sleep", "2 Eat", "3 Playing", "4 Bath"]
new_list = list[1::2]
for i in new_list:
    print(f"New List number {i}")

print("\nList compre : Direct Ganjil")
list = ["1 Sleep", "2 Eat", "3 Playing"]
print(list[0::2])

print("\nList compre : Direct Genap")
list = ["1 Sleep", "2 Eat", "3 Playing", "4 Bath"]
print(list[1::2])

print("\nInput Ganjil using compre")
inp = int(input("Masukan Nomor : "))
for i in range(1, inp, 2):
    print(i)

print("\nInput Genap using compre")
inp = int(input("Masukan Nomor : "))
for i in range(0, inp, 2):
    print(i)
