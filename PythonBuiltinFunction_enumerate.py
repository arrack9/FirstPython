#C:Python31python.exe  
# -*- coding:utf-8 -*-
'''在python中如果需要用到index的話，可使用內建函式enumerate'''

'''normal write'''
names = ['Alice', 'Bob', 'Cindy']
index = 0
while index < len(names):
    print '%d %s' % (index, names[index])
    index += 1
    
''' python enumerate'''
favorites = ['Chocalate', 'Coffee', 'Whisky', 'Red Wine', 'Cheese']
item = 0
for item, element in enumerate(favorites):
    print '%d %s' % (item, element)