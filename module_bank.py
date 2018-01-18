#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''
Created on 2018�~1��18��

@author: Pingyao.Chen
'''
def account(name, number, balance):
    return {'name': name, 'number': number, 'balance': balance} # dict

def deposit(acct, amount):
    if amount <= 0:
        raise ValueError('amount must be positive')
    acct['balance'] += amount  # list

def withdraw(acct, amount):
    if amount > acct['balance']:
        raise RuntimeError('balance not enough')
    acct['balance'] -= amount
    
def invest(acct, amount):
    if amount > acct['balance']:
        raise ValueError('Liabilities')
    acct['balance'] -= amount
    
 
def to_str(acct):
    return 'Account:' + str(acct)   