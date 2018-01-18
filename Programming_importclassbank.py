#C:Python31python.exe  
# -*- coding:utf-8 -*-
import bank
acct = bank.Account('Pingyao', '999-9999', 10000000)
acct.deposit(500)
acct.withdraw(200)
print acct