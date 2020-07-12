import  os
import re
import numpy as np
from creatConfigFile import creatConfigFile
from creat_cmesh_config import creat_cmesh_config

def aimFunction(x1,x2,x3,x4,x5,x6,x7):
    # print("wsy: config_file has been created!")
    # print("start run booksim :")
    if x1 == 3:
        # print("cmesh")
        creat_cmesh_config(x1,x2,x3,x4,x5,x6,x7) 
        output = os.system("./booksim ./wsy_work/wsy_booksim_cmesh_config > log")
    elif x1==1 or x1 == 2:
        creatConfigFile(x1,x2,x3,x4,x5,x6,x7)
        output = os.system("./booksim ./wsy_work/wsy_booksim_config_file  > log")
    # output  = os.system("./booksim  ./wsy_work/wsy_booksim_config_file > log")
    # print("booksim finish!")
    # print("caculate latency:")    
    file = open("log",'r')
    log = file.readlines()
    line=[9999999999999]
    if len(log)>60 and "Overall Traffic Statistics" in log[-60]:
        # print(log[-59])
        # print(log[-58])
        # print(log[-57])
        if "e+" in log[-58] :
            print("e")
        elif  "-" in log[-58]:
            print("-")
        else:
            line = re.findall('.+\S\s(\d+\D?\d*).', log[-58])
            line = list(map(float,line))
    # else:
    #     print
        # print("aimfunction:当前配置booksim不可行\n")
    y = np.mean(line)
    # print("topo,routing_function,vc_allocator,arb_type,priority,y  = ",x1,x2,x3,x4,x5,x6,x7,y)
    return y

