from __future__ import division
import numpy as np
import math
# from  aimFunction import aimFunction
import random
from random import choice
from aimFunction_test import aimFunction
from creatConfigFile import creatConfigFile
import os
import matplotlib.pyplot as plt
import re
import openpyxl
import time

# ==========================================
begin_time = time.clock()
# ==========================================
x1_b = x1 =  choice([1,2,3])
x2_b = x2 =  choice([1,2,3,4,5,6,9,11,16])
x3_b = x3 =  choice([1,3,4,5,6])
x4_b = x4 = choice([1,2])
x5_b = x5 =choice([1,2,3])
x6_b = x6 = choice([1,2,3,4,5,6])
x7_b = x7 =choice([1,2,3,4,5,6,7])

y = y_b = aimFunction(x1,x2,x3,x4,x5,x6,x7)
yNew = 0

rubbish = [[2,2,3,4,5,6,7]]

# 首先初始化一个可行的架构
while y_b > 100000:
    x1_b = x1 =  choice([1,2])
    x2_b = x2 =  choice([1,2,3,4,5,6,9,11,16])
    x3_b = x3 =  choice([1,3,4,5,6])
    x4_b = x4 = choice([1,2])
    x5_b = x5 =choice([1,2,3])
    x6_b = x6 = choice([1,2,3,4,5,6])
    x7_b = x7 =choice([1,2,3,4,5,6,7])
    print("The newly generated parameters are：%s"%([x1,x2,x3,x4,x5,x6,x7]))
    if [x1,x2,x3,x4,x5,x6,x7] in rubbish:
        # print("%s in rubbish"%([x1,x2,x3,x4,x5,x6,x7]))
        continue
    y = y_b = aimFunction(x1,x2,x3,x4,x5,x6,x7)
    if y > 999999999:
        rubbish.append([x1,x2,x3,x4,x5,x6,x7])
        continue
print("best:",x1,x2_b,x3_b,x4_b,x5_b,x6_b,x7_b,y_b)

print(rubbish)

T= 1000
Tmin = 300
k = 30
t =0
num = 0
while T >Tmin:
    # print("T:",T,"==================================")
    for i in range(k):
        # print("i:",i)
        num+=1
        print("num = ",num)
        if(y>100000):
            continue
        # print(x1,x2,x3,x4,x5,x6,x7,y)
        # y = aimFunction(x1,x2,x3,x4,x5,x6,x7)
        x1New = choice([1,2])
        x2New = choice([1,2,3,4,5,6,9,11,16])
        x3New = choice([1,3,4,5,6])
        x4New =  choice([1,2])
        x5New =  choice([1,2,3])
        x6New =  choice([1,2,3,4,5,6])
        x7New =  choice([1,2,3,4,5,6,7])
        print("The newly generated parameters are：%s"%([x1New,x2New,x3New,x4New,x5New,x6New,x7New]))
        if [x1New,x2New,x3New,x4New,x5New,x6New,x7New] in rubbish:
            # print("%s in rubbish"%([x1New,x2New,x3New,x4New,x5New,x6New,x7New]))
            continue
        yNew = aimFunction(x1New,x2New,x3New,x4New,x5New,x6New,x7New)
        # if yNew > 99999999:
        #     rubbish.append([x1,x2,x3,x4,x5,x6,x7])
        #     continue
        if (yNew > 100000):
            rubbish.append([x1New,x2New,x3New,x4New,x5New,x6New,x7New])
            # print("%s in rubbish"%([x1New,x2New,x3New,x4New,x5New,x6New,x7New]))
            continue
        if(yNew < y):
            # print("x and y changed!")
            x1 = x1New
            x2 = x2New
            x3 = x3New
            x4 = x4New
            x5  = x5New
            x6 = x6New
            x7 = x7New
            y = yNew
            if(yNew < y_b):
                print("best changed!")
                x1_b = x1New
                x2_b = x2New
                x3_b = x3New
                x4_b = x4New
                x5_b = x5New
                x6_b = x6New
                x7_b = x7New
                y_b = yNew
                print("best:",x1_b,x2_b,x3_b,x4_b,x5_b,x6_b,x7_b,y_b)
        else:
            p=math.exp(-(yNew-y)/T)
            r=np.random.uniform(low=0,high=1)
            if r<p:
                # print("x  and y changed!")
                x1 = x1New
                x2 = x2New
                x3 = x3New
                x4 = x4New
                x5  = x5New
                x6 = x6New
                x7 = x7New
                y = yNew
            # else:
            #     rubbish.append([x1,x2,x3,x4,x5,x6,x7])
            #     continue
    t= t+1
    T = 1000/(1+t)
print("best: ",x1_b,x2_b,x3_b,x4_b,x5_b,x6_b,x7_b,y_b)
best_config = [x1_b,x2_b,x3_b,x4_b,x5_b,x6_b,x7_b]
end_time = time.clock()
print("The total time is：%s"%(end_time - begin_time))

