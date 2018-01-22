#C:Python31python.exe  
# -*- coding:utf-8 -*- 
import bank
import xmath
acct = bank.Account('Pingyao', '111-1111', 77777777)
acct.deposit(900)
acct.withdraw(200)
print (acct.balance)

a = xmath.max(100, 90)
print(a)
b = xmath.min(11, 99)
print(b)
c = xmath.suma(1, 2)
print(c)