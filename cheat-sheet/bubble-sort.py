def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


data = [-2, -9, 1, 0, 4]
print(bubbleSort(data))
