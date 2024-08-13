
# сортировка вставками
def slow_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        while arr[i - 1] > val and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr

#быстрая сортировка
def qsort(arr):
    #массив такой длинны уже отсортирован
    if len(arr) <= 1:
        return arr
    
    if len(arr) < 10:
        return slow_sort(arr)

    l = 0
    r = len(arr) - 1
    m = (r + l) // 2
    while (l < r):
        val = arr[m]
        while(r > m):
            if arr[r] < val:
                break
            r -= 1
        while(l < m):
            if arr[l] >= val:
                break
            l += 1
        arr[l], arr[r] = arr[r], arr[l]

        #сместить границу по индексу при необходимости
        if (l == m and r != m):
            m = r
        elif (l != m and r == m):
            m = l
    #сортировка частей
    arr_left = qsort(arr[:m])
    arr_right = qsort(arr[m + 1:])

    #объединение
    arr = arr_left + arr[m:m + 1] + arr_right
    return arr
if __name__ == '__main__':
    a = [1, 3, 11, 2, 1, 5, 0, -4, 7, 10, -7, 15, 6]
    a = qsort(a)
    print(a)