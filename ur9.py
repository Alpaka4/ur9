###Задача 1
###Дан список чисел. Превратите его в список квадратов этих чисел.
##import random
##lst=[]
##n=10
##for i in range(n):
##    lst.append(random.randint(1,10))
##print(lst)
##for i in range(n):
##    lst[i]=lst[i]*lst[i]
##print(lst)
###Задача 2
##import random
##lst=[]
##n=10
##p=0
##for i in range(n):
##    lst.append(random.randint(-10,10))
##print(lst)
##for i in range(n):
##    if lst[i]>0:
##        p+=1
##print(p)
###Задача 3
##import random
##lst=[]
##n=12
##P=1
##for i in range(n):
##    lst.append(random.randint(1,10))
##print(lst)
##for i in range(n):
##        P*=lst[i]
##print(P)
###Задача 4
##import random
##lst=[]
##n=9
##S=0
##for i in range(n):
##    lst.append(random.randint(-20,30))
##print(lst)
##for i in range(n):
##    if lst[i]>0:
##        S+=lst[i]
##print(S)
###Задача 4
##import random
##lst=[]
##n=11
##for i in range(n):
##    lst.append(random.randint(-50,50))
##print(lst)
##for i in range(n):
##    if lst[i]%3!=0:
##        print(lst[i])
###Array7◦
###. Дан массив размера N. Вывести его элементы в обратном порядке.
##import random
##print("Введите кол-во элементов списка")
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##lst.reverse()
##print(lst)
###Array8. Дан целочисленный массив размера N. Вывести все содержащиеся в
###данном массиве нечетные числа в порядке возрастания их индексов, а
###также их количество K.
##import random
##print("Введите кол-во элементов списка")
##lst=[]
##n=int(input())
##K=0
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(n):
##    if lst[i]%2!=0:
##        print(lst[i])
##        K+=1
##print("K=",K)
###Array9. Дан целочисленный массив размера N. Вывести все содержащиеся в
###данном массиве четные числа в порядке убывания их индексов, а также
###их количество K.
##import random
##print("Введите кол-во элементов списка")
##lst=[]
##n=int(input())
##K=0
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##lst.reverse()
##for i in range(n):
##    if lst[i]%2==0:
##        print(lst[i])
##        K+=1
##print("K=",K)
###Array10. Дан целочисленный массив размера N. Вывести вначале все содержащиеся в данном массиве четные числа в порядке возрастания их индексов,
###а затем — все нечетные числа в порядке убывания их индексов.
##import random
##print("Введите кол-во элементов списка")
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(n):
##    if lst[i]%2==0:
##        print(lst[i], end=" ")
##print()
##lst.reverse()
##for i in range(n):
##    if lst[i]%2!=0:
##        print(lst[i], end=" ")
###Array11. Дан массив A размера N и целое число K (1 ≤ K ≤ N). Вывести элементы массива с порядковыми номерами, кратными K: AK, A2·K, A3·K, . . . .
###Условный оператор не использовать.
##print("введите число которое будет меньше размера списка")
##import random
##lst=[]
##n=int(input())
##k=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(k,n,k):
##    print(lst[i])
###Array12. Дан массив A размера N (N — четное число). Вывести его элементы
###с четными номерами в порядке возрастания номеров: A2, A4, A6, . . ., AN .
###Условный оператор не использовать.
##import random
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(2,n,2):
##    print(lst[i])
###Array13. Дан массив A размера N (N — нечетное число). Вывести его элементы
###с нечетными номерами в порядке убывания номеров: AN , AN−2, AN−4, . . .,
###A1. Условный оператор не использовать.
##import random
##print("Введите нечётный размер списка")
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##lst.reverse()
##for i in range(1,n,2):
##    print(lst[i])
###Array14. Дан массив A размера N. Вывести вначале его элементы с четными
###номерами (в порядке возрастания номеров), а затем — элементы с нечетными номерами (также в порядке возрастания номеров):
###A2, A4, A6, . . ., A1, A3, A5, . . . .
###Условный оператор не использовать.
##import random
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(2,n,2 end=" "):
##    print(lst[i])
##print()
##for i in range(1,n,2 end=" "):
##    print(lst[i])
##Array15. Дан массив A размера N. Вывести вначале его элементы с нечетными
##46 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.5
##номерами в порядке возрастания номеров, а затем — элементы с четными
##номерами в порядке убывания номеров:
##A1, A3, A5, . . ., A6, A4, A2.
##Условный оператор не использовать
import random
lst=[]
n=int(input())
for i in range(n):
    lst.append(random.randint(1,100))
print(lst)
for i in range(1,n,2):
    print(lst[i])
print()
lst.reverse()
for i in range(2,n,2):
    print(lst[i])



