# First 10 numbers of Fibonacci sequence

array = [0, 1]
for i in range(2, 10):
    array.append(array[i - 1] + array[i - 2])
for i in range(0, 10):
    print(array[i])
