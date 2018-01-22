#C:Python31python.exe  
# -*- coding:utf-8 -*-

def valid():
    return True

'''慣用'''
if valid():
    print 'valid'
if not valid():
    print 'invalid'
    
'''非慣用'''
if valid() == True:
    print 'valid'
if valid() == False:
    print 'false'
    
'''慣用
對sequence (string、lists、tuples)來說，
因為空的sequence是False，不需判斷長度是否為零
'''
users = []
if not users:
    print 'No users available'   
    
'''非慣用'''
if len(users) == 0:
    print 'No users available' 

'''數值型態需明確比值'''
i = 10   
if i % 2  == 0:
    print 'odd number'
 
'''和None比較要使用is和is not，儘管在正常情況下和==沒有啥差別'''   
class Negator(object):
    def __eq__(self, other):
        return not other

thing = Negator()
print thing == None
print thing is None
