import random

n = int(input()) # должно быть меньше m, в данном случае - 10
m = 10 # нет указания о максимальной длине массива, для читаемости беру 0 < m > 10
array = []
len_array = 0
end_array = [[] for _ in range(n)]
array_element = 0

def fill_len_array():
    len_array = int(random.random() * m)
    if len_array in array or len_array == 0:
        fill_len_array()
    else:
        array.append(len_array)
        return

def fil_end_array(len_arr_i):
    for i in range(len_arr_i):
        arr = random.random()
        arr_tmp.append(arr)
    return arr_tmp

for i in range(n):
    if len_array in array:
        len_array = int(random.random() * 5)
    fill_len_array()

for i in array:
    arr_tmp = []
    if array_element % 2 == 0:
        end_array[array_element] = sorted(fil_end_array(i), reverse = True)
    else:
        end_array[array_element] = sorted(fil_end_array(i))
    if array_element < n:
        array_element = array_element + 1
    
print(end_array)
    
    
    
