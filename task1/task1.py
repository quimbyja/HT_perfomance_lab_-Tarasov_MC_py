n = int(input("Число элементов в массиве: "))
m = int(input("Длина интервала среза: "))
arr = list(range(1, n + 1))
current = 0
arr_str = ''
for i in arr:
    arr_str += str(i)
print("Круговой массив: ", arr_str)
print("Путь: ", end='')
while True:
    print(arr[current], end='')
    current = (current + m - 1) % n
    if current == 0:
        break
