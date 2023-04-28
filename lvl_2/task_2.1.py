# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!
arr1=[4,6,2,1,9,63,-134,566] 
arr2=[-52, 56, 30, 29, -54, 0, -110]
arr3=[42, 54, 65, 87, 0]  
arr4=[5]       
n=len(arr1)
print(arr1)
def maximum(numbers):
    max_num = numbers[0] 
    for num in numbers:
        if num > max_num: 
            max_num = num 
    return max_num

def minimum(numbers):
    min_num = numbers[0] 
    for num in numbers:
        if num < min_num: 
            min_num = num 
    return min_num
print(maximum(arr1))
print(minimum(arr1))
print(maximum(arr2))
print(minimum(arr2))
print(maximum(arr3))
print(minimum(arr3))
print(maximum(arr4))
print(minimum(arr4))