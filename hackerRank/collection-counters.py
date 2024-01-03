from collections import Counter
x = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
N = int(input(""))

values = Counter(x).values()
print(values)