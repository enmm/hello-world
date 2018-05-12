#!/usr/bin/python
#! -*- coding: UTF-8 -*-
year = int( raw_input( '年：'))
month = int( raw_input('月：'))
day = int( raw_input('天：'))
days = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month < 12:
    sum = days[month - 1]
else:
    print '输入的月份有误'
sum += day
if year%400 == 0 or year%4 == 0 and year%100 != 0 and month > 2:
    sum+= 1
print '这是第%d天！'% sum

