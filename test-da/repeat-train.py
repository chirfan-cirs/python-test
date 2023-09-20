print("\nGanjil")
list = [1,2,3,4,5]
print(list[0::2])

print("\nGenap")
list = [1,2,3,4,5]
print(list[1::2])

print("\nInput Ganjil")
inp = int(input("Masukan Nomor : "))
for i in range(1, inp, 2):
    print(i)

print("\nInput Genap")
inp = int(input("Masukan Nomor : "))
for i in range(0, inp, 2):
    print(i)
