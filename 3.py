

#Задача «Ряд - 1»

#a = int(input())
#b = int(input())
#for i in range(a, b + 1):
#	print(i)



#Задача «Ряд - 2»

#a = int(input('Введите 1 число:'))
#b = int(input('Введите 2 число:'))
#if a < b:
#    for i in range(a, b + 1):
#        print(i, end=' ')
#else:
#    for i in range(a, b - 1, -1):
#        print(i, end=' ')





#Задача № 3 «Сумма N чисел»

#n = int(input('Введите количество чисел:'))
#x = 0
#for i in range(n):
#    n = int(input('Введите число:'))
#    x += n
#print(x)




#Задача 4 «Факториал»

#n = int(input('Введите число:'))
#x = 1
#for i in range(2 , n + 1):
#    x *= i
#print(x)




# Задача 5 «Лесенка»

#n = int(input('Введите число:'))
#x = 0
#if n >= 1:
#    for i in range(1, n + 1):
#        for z in range(1, i + 1):
#            print(z, end='\n', sep='')




#Задача 6 «Список квадратов»

#n = input("Введите целое неотриц. число: ")
#if int(n) >= 0:
#    n = int(n)
#    for i in range(1, n + 1):
#        x = i * i
#        if x <= n:
#            print(x)
#else:
#    print("Введите целое неотриц. число")





#Задача 7 «Степень двойки»

#n = int(input('Введите натуральное число:'))
#i = 0
#x = 1
#while x * 2 <= n:
#    x *= 2
#    i += 1
#print(f"Наибольшая целая степень двойки, не превосходящая {n}, равна 2^{i} = {x}")





#Задача 8 «Утренняя пробежка»

#x = float(input('Введите начальный пробег спортсмена:'))
#y = float(input('Введите количество:'))
#days = 1
#while x < y:
#    x += x * 0.10
#    days += 1
#print(f"На {days}-й день спортсмен достигнет пробега не менее {y} километров.")




#Задача 9 «Длина последовательности»

#count = 0
#while True:
#    numb = int(input('Введите целое неотрицательное число (0 для завершения):'))
#    if numb == 0:
#        break
#    count += 1
#print(f"Количество членов последовательности: {count}")





# Задача 10 «Количество элементов, которые больше предыдущего»

#num = int(input('Введите первое натуральное число (0 для завершения):'))
#count = 0
#while True:
#    numb = int(input('Введите целое неотрицательное число (0 для завершения):'))
#    if numb == 0:
#        break
#    if numb > num:
#        count += 1
#    num = numb
#print(f"Количество элементов, больших предыдущего: {count}")




#Задача 11 «Второй максимум»

#first_max = 0
#second_max = 0
#num = int(input('Введите натуральное число (0 для завершения):'))
#while num != 0:
#    if num > first_max:
#        second_max = first_max
#        first_max = num
#    elif num > second_max and num != first_max:
#        second_max = num
#    num = int(input('Введите натуральное число (0 для завершения):'))
#print(f"Второй по величине элемент в последовательности: {second_max}")




#Задача 12 «Числа Фибоначчи»

#n = int(input("Введите номер n для нахождения числа Фибоначчи φn: "))
#
#if n == 0:
#    result = 0
#elif n == 1:
#    result = 1
#else:
#    fib_n_minus_1 = 1
#    fib_n_minus_2 = 0
#
#    for i in range(2, n + 1):
#        fib_n = fib_n_minus_1 + fib_n_minus_2
#        fib_n_minus_2 = fib_n_minus_1
#        fib_n_minus_1 = fib_n
#
#    result = fib_n
#
#print(f"Число Фибоначчи φ{n} равно {result}")






#Задача 13 «Максимальное число идущих подряд равных элементов»

#num = int(input('Введите первое натуральное число (0 для завершения):'))
#current_streak = 1
#max_streak = 1
#while True:
#    numb = int(input('Введите целое неотрицательное число (0 для завершения):'))
#    if numb == 0:
#        break
#    if numb == num:
#        current_streak += 1
#        if current_streak > max_streak:
#            max_streak = current_streak
#    else:
#        current_streak = 1
#    num = numb
#if max_streak > 1:
#    print(f"Наибольшее число подряд идущих элементов равных друг другу: {max_streak}")
#else:
#    print("В последовательности нет подряд идущих элементов, равных друг другу.")





#Задача 14 «Четные индексы»

#List = ["Samat", "Azamat", "Roma", "Ilya"]
#print(List[::2])



#Задача 15 «Больше предыдущего»

#List = [3, 56, 5, 454, 54]
#for i in range(1, len(List)):
#    if List[i] > List[i - 1]:
#        print(List[i])




#Задача 16 «Наибольший элемент»

#List = [43, 556, 3, 4, 5654]
#max_value = max(List)  # Находим наибольший элемент
#max_index = List.index(max_value)  # Находим индекс первого вхождения наибольшего элемента
#print(f"Наибольший элемент: {max_value}")
#print(f"Индекс наибольшего элемента: {max_index}")




#Задача 17 «Шеренга»

#heights = list(map(int, input().split()))
#petya_height = int(input())
#position = 1
#for height in heights:
#    if petya_height <= height:
#        break
#    position += 1
#print(position)





#Задача 18 «Переставить соседние»

#List = [1, 2, 3, 4, 5, 6]
#List[0] = List[1]
#List[2] = List[3]
#List[4] = List[5]
##print(List)




#Задача 19 «Переставить min и max»

#List = [453, 67, 1, 59, 2, 28, 349]
#min_index = List.index(min(List))
#max_index = List.index(max(List))
#List[min_index], List[max_index] = List[max_index], List[min_index]
#print("Изменённый список:")
#print(List)





#Задача 20 «Удалить элемент»

#numbers = []
#while True:
#    try:
#        num = int(input("Введите число (0 для завершения): "))
#        if num == 0:
#            break
#        numbers.append(num)
#    except ValueError:
#        print("Введите корректное число")
#k = int(input('Введите индекс списка, который хотите удалить:'))
#List = numbers.pop(k)
#print(numbers)




#Задача 21 «Вставить элемент»

#numbers = [int(x) for x in input().split()]
#k, c = map(int, input().split())
#numbers.append(None)
#for i in range(len(numbers) - 1, k, -1):
#    numbers[i] = numbers[i - 1]
#numbers[k] = c
#print("Изменённый список:", numbers)




#Задача 22 «Ферзи»

#queens = [tuple(map(int, input().split())) for _ in range(8)]
#def are_queens_attacking(queens):
#    for i in range(8):
#        for j in range(i + 1, 8):
#            x1, y1 = queens[i]
#            x2, y2 = queens[j]
#            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
#                return "YES"
#    return "NO"
#result = are_queens_attacking(queens)
#print(result)

