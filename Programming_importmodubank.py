#C:Python31python.exe  
# -*- coding:utf-8 -*-
import module_bank
acct = module_bank.account('Pingyao', '999-9999', 10000000)
module_bank.deposit(acct, 500)
module_bank.withdraw(acct, 200)
module_bank.invest(acct, 300)
print module_bank.to_str(acct)
