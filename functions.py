from __future__ import division
import  numpy as np
import random
from random import choice
import math
# ==========================================
def change_file(old_file,new_file,count):
    result = []
    # 将旧文件中数据读进result中
    with open(old_file) as f:
        for line in f:
            result.append(list(map(int,line.split(' '))))
    #将时间拉长count倍
    for num in result:
        num[0] = num[0]*count
    new_file = open(new_file,"w")
    # 将result存入新的文件中
    for x in result:
        new_file.write(str(x[0])+" "+str(x[1])+"\n")
    new_file.close()
# ==========================================
def get_time():
    file  = open("log","r")
    log = file.readlines()[-60:]
    # for i in range(len(log)):
    #     print(log[i])
    # print(log[1])
    # print(log[2])
    print(log[4])
    # packet_latency_avery = np.mean(list(map(float,re.findall('.+\S\s(\d+\D?\d*).', log[2]))))
    packet_latency_max = np.mean(list(map(float,re.findall('.+\S\s(\d+\D?\d*).', log[4]))))
    return packet_latency_max
# ==========================================
def data_write(file_path, data1,data2,data3):
    outwb = openpyxl.Workbook()
    outws = outwb.create_sheet("sheet",0)
    for  i in range(len(data1)):
        outws.cell(row = 1,column = i+1).value  = data1[i]
    for i in range(len(data2)):
       outws.cell(row = 2,column = i+1).value  = data2[i]
    for i in range(len(data3)):
       outws.cell(row = 3,column = i+1).value  = data3[i]
    outwb.save(file_path)
# ==========================================
def disturb(len,T):
    return np.random.uniform(low=-0.055,high=0.055)*T
# ==========================================
def aimFunction(x):
    y=x**3-60*x**2-4*x+6
    return y
# ==========================================
def choice(x,X,T):
    lenth = len(X)
    index = X.index(x)
    new_index = math.ceil(index + np.random.uniform(low=-0.055,high=0.055)*T)%lenth
    # print("")
    return X[new_index]


# ==========================================

if __name__=="__main__":
    len = 7
    T=1000 #initiate temperature
    Tmin=10 #minimum value of terperature
    x=np.random.uniform(low=0,high=100)#initiate x
    k=50 #times of internal circulation 
    y=0#initiate result
    t=0#time
    while T>=Tmin:
        for i in range(k):
            #calculate y
            y=aimFunction(x)
            #generate a new x in the neighboorhood of x by transform function
            xNew=x+np.random.uniform(low=-0.055,high=0.055)*T
            if (0<=xNew and xNew<=100):
                yNew=aimFunction(xNew)
                if yNew-y<0:
                    x=xNew
                else:
                    #metropolis principle
                    p=math.exp(-(yNew-y)/T)
                    r=np.random.uniform(low=0,high=1)
                    if r<p:
                        x=xNew
        t+=1
        print(t)
        T=1000/(1+t)
        
    print (x,aimFunction(x))
    
    lenth1 = len(x1_range)
    T = 1000
    Tmin = 500
    index1 = random.randint(1,len(x1_range))
    x1 = x1_range[index1]
    k = 50
    y = 0
    t = 0
    while T>=Tmin:
        for i in range(k):
            y1 = aimFunction(x1)
            index1_new = math.ceil(index1 + np.random.uniform(low=-0.055,high=0.055)*T)%lenth1
            print(index1_new)
            x1New = x1_range[index1_new]
            print(x1New)
        t = t+1
        print("++++++"+str(t))
        T = 1000/(1+t)
    # x = 3
    # X = [1,2,3,4,5,6,7]
    # T = 500
    # print(x,choice(x,X,T))