#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''tuple型態  串列可以修改，而tuple不能修改
       串列與tuple裡面的成員可以是任何的物件，數字、字串、其他串列或tuple，
       甚至是辭典、function物件...。它們也可以像字串一樣使用索引、切片來取得其中的成員'''
       
'''下例中，串列中包含數字123, 字串abc, 另一個串列[111,222], 與tuple (333,444)
       串列與tuple的索引與切片使用方式與字串完全相同，請參考Python字串。 '''
a = [123, 'abc', [111,222], (333,444)]
print a[0]
print a[2][0]
print a[3][1]
print a[1]

'''串列或Tuple可以相加，前題是串列必須與串列相加，
   tuple則必須與tuple相加，最後會傳回新的串列或tuple。'''
a = [111, 222] + [333, 444] + [555, 666] + [777, 888]
print a
b = (000, 999) + (888, 777) + (666, 555) + (444, 333)  
print b
a = ['aaa', 'bbb'] + ['Jester', 'Yuan-Feng'] + ['Tiffany', 'Ivan'] + ['MST' + 'HP_Team']
print a
b = ('Japan', 'Korea') + ('China', 'Turkey') + ('Thailand', 'Taiwan') + ('America', 'India')
print b
'''若串列與Tuple相加要將tuple轉成list後再相加
       或是list轉成tuple再相加'''
print a + list(b)
print tuple(a) + b
'''可以將串列或tuple重複數位，類似字串的乘法'''
a = [111, 222]
print a * 3
b = ('555', '999')
print b * 5
a = [123, 'abc', [111, 222], (333, 555)]
print a
a[1] = 'xyz'
print a
'''一次置換串列中多個成員'''
a[0:2] = ['aaa', 'bbb', 'ccc']
print a
'''一次刪除串列中多個成員'''
a[0:1] = []
print a
'''也可使用del刪除'''
del a[0:1]
print a
'''呼叫remove方法依內容來刪除，一次只能刪除一個成員'''
a.remove([111,222])
print a
'''append與pop新增成只適用於串列，不適用於tuple,
        可以呼叫append方法，增加成員到串列'''
a = [123, 456]
a.append(789)
print a
'''呼叫pop取出串列成員，可以指定索引，若不指定則預設為最後一個，並在取出後從串列刪除該成員'''
a = [111,222,333,444,555,666,777,888,999,000]
a.pop()
print a
a.pop(2)
print a
a.append(333)
print a
a.append(111)
print a
'''Others 關於tuple有一個偷懶的方法，就是不加小括號'''
a = 111, 999, 888
print a
'''但如果只有一個項目，不管有沒有加小刮號都要在後面加逗號'''
a = 111,
print a
'''沒有加逗號，會被直譯器誤認為數定111'''
a = 111
print a
'''交換2個變數值，以傳統C語言的寫法可能會是'''
a = 9
b = 5
temp = a
a = b
b = temp
print a
print b
'''交換2個變數值，python的寫法如下'''
a, b = b, a
print a
print b