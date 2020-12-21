import sys
sys.path.append("../04-实现阶段/codes")

from StudentQueryDev import *

print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq([123, '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq([779, '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', 'wfst', '*', '*', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', 'DSP642', '*', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '2.50', '*', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '2020-7-2', '*', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '98121.17', '*', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', 'guizhou', '*', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', '*', '10', '*', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', '*', '*', 'admin3', '*', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', '*', '*', '*', 'admin2', '*']))
print(StudentQueryDev.queryDevReq(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '空闲']))
