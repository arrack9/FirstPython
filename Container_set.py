#C:Python31python.exe  
# -*- coding:utf-8 -*- 
'''�Ĥ@��O�]�w��Ķ���Ҧb����m
       �ĤG��O�]�w�{���X�ϥ�utf-8���s�X
   set���A'''
admins = {'Justin', 'caterpillar'} #�إ�set
print(admins)
users = {'momor', 'hamini', 'Justin'}
print('Justin' in admins)  # justin�O�_�b�����s?
print(admins & users)	   # �֦P�ɦb�����s�]�O�ϥΪ̸s?
print(admins | users)	   # �֬O�����s�άO�ϥΪ̸s?
print(admins - users)	   # �֬O�����s�����O�ϥΪ̸s?
print(admins ^ users)	   # XOR
print(admins > users)      # E
print(admins < users)