#C:Python31python.exe  
# -*- coding:utf-8 -*- 
import module_xmath
print '# import module_xmath'
print module_xmath.pi
print module_xmath.xmax(10, 5)
print module_xmath.xsum(1, 2, 3, 4, 5)

print '# import module_xmath as math'
import module_xmath as math # 為 xmath模組取別名為math
print math.e

print '# from module_xmath import min'
from module_xmath import min # 將min複製至目前模組，不建議from modu import*，易造成名稱衝突
print min(10, 5)