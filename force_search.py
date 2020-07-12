import time
from aimFunction_test import aimFunction
topo = [1,2]
routing_fun = [1,2,3,4,5,6,9,11,16]
vc_allo = [1,3,4,5,6]
arb_type = [1,2]
priority = [1,2,3]
num_vcs = [1,2,3,4,5,6]
vc_buf_size = [1,2,3,4,5,6,7]
y_b = 99999999999
x_b = [0,0,0,0,0,0,0]
count = 0
begin_time = time.clock()

# def aimFunction(x1,x2,x3,x4,x5,x6,x7):
#     y = x1*x1 + x2*x3-x4*2 +x5+x6-x7**3
#     return y

for x1 in topo:
    for x2 in routing_fun:
        for x3 in vc_allo :
            for x4 in arb_type:
                for x5 in priority:
                    for x6 in num_vcs:
                        for x7 in vc_buf_size:
                            y = aimFunction(x1,x2,x3,x4,x5,x6,x7)
                            print(x1,x2,x3,x4,x5,x6,x7,"---------------------------------",y)
                            if y < y_b:
                                y_b = y
                                x_b = [x1,x2,x3,x4,x5,x6,x7]
                            count+=1
end_time = time.clock()
print( "共有  %s 种情况 "%(count))
print("共耗时为：%s"%(end_time - begin_time))
print("最好的x为：%s"%(x_b))
print("最好的y为：%s"%(y_b))