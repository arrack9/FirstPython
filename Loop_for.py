#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''Python 中的 for 可用來迭代循序結構的物件。例如想將某 list 的元素都做二次方運算，收集在另一個 list 中的話，可以如下'''
from test.test_datetime import Oddballs
numbers = [10, 20 ,30]
squares = []
for number in numbers:
    squares.append(number ** 2)
print squares
numlist = []
for num in numbers:
    numlist.append(num ** 3)
print numlist
numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9] 
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print odd_numbers 
'''不需在將list做完4次方運算存放在宣告的numlist內即可印出'''
print [num ** 4 for num in numbers]
print [number for number in numbers if number % 2 != 0]  

'''for 包含式（comprehension）也可以形式巢狀結構，
        例如有個元素都為 list 的 list，想將其中的 list 元素串起來，也就是將之平坦化，可以如下：'''
lts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [ele for lt in lts for ele in lt]
abs = [(21, 23, 45), (11, 24, 18), (98, 23, 12)]
print [aaa for aa in abs for aaa in aa]

'''當你使用 [] 包圍住 for 包含式（comprehension） 時，會建立 list 實例，
       如果使用 {} 的話，可以建立 set 實例，重複的元素會自動去除。例如：'''
print {name for name in ['Justin', 'caterpillar', 'caterpillar', 'openhome']}

'''也可以建立 dict 實例。
       例如：下例中的 zip 函式，就如名稱意義，會將兩個 list 像拉鏈一樣，兩兩相扣在一起為 tuple，
       這些 tuple 元素組成一個新的 list，對於 tuple 元素組成的這個 list，
       每個 tuple 中的一對元素再指定給 name 與 passwd，最後這對 name 與 passwd 組成 dict 的一對鍵值。'''
names = ['Tiffany', 'John', 'Bob', 'Mary', 'Karen']
passwds = [123, 789, 256, 777, 143]
print{name : passwd for name, passwd in zip(names, passwds)}
transport = ['bus', 'miniVan', 'taxi', 'tutu', 'bicycle', 'motorcycle', 'airplane']
carnumber = [166, 891, 233, 559, 201, 888, 999]
print{trans : number for trans, number in zip(transport, carnumber)}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
color = ['blue', 'red', 'green', 'purple', 'yellow', 'pink', 'orange']
print{week : col for week, col in zip(days, color)}
numbers = []
for number in range(20):
    numbers.append(str(number))
print ", ".join(numbers)