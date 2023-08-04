num = 5
x = 0

for i in range(num):
    for j in range(i+1):
        x = i + 1
        print("* ", end="")
    print("\n")
