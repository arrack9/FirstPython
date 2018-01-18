#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''
Created on 2018年1月18日

@author: Pingyao.Chen
'''

class Account:
    '''
    classdocs
    '''
    def __init__(self, name, number, balance):
        '''
        Constructor
        '''
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('balance not enough')
        self.balance -= amount
        
    def _str_(self):
        return 'Account({0}, {1}, {2})'.format(
            self.name, self.number, self.balance)
        