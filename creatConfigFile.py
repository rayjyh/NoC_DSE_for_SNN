import os
x1 = 1
x2 = 1
x3 = 1
x4 =1 
x5 =1 
x6 =1 
x7 =1

# 1
def get_topo(num):
    if(num <1 or num >8):
        print("Topo error")
    numbers ={
        1: "mesh",
        2:"torus",
        4:"fly",
        3:"cmesh",
        5:"fat tree",
        6:"flattend",
        7:"dragonfly",
        8:"quad tree"
    }
    return numbers.get(num,None)
# 2
def get_routing_fun(num):
    numbers={
        1:"dim_order",
        2:"dor",
        3:"dor_no_express",
        4:"xy_yx",
        5:"xy_yx_no_express",
        6:"dim_order_ni",
        7:"dim_order_pni",
        8:"dim_order_bal",
        9:"romm",
        10:"romm_ni",
        11:"min_adapt",
        12:"valiant",
        13:"valiant_ni",
        14:"chaos",
        15:"adapptive_xy_yx",
        16:"planar_adapt"
        # 4:"min",
        # 5:"ran_min",
        # 6:"nca",
        # 7:"ugal",
        # 8:"dest_tag",
        # 9:"min_adapt"
    }
    return numbers.get(num,None)
# 3
def get_vc_allocator(num):
    numbers ={
        2:"max-size",
        1:"islip",
        3:"pim",
        4:"loa",
        # 5:"wavevfront",
        5:"separable_input_first",
        6:"separable_output_first"
    }
    return numbers.get(num,None)
# 4
def get_arb_type(num):
    numbers ={
        1:"round_robin",
        2:"matrix"
    }
    return numbers.get(num,None)
# 5
def get_priority(num):
    numbers={
        1:"age",
        2:"one",
        3:"sequence"
    }
    return numbers.get(num,None)
# 6
def get_num_vcs(num):
    numbers ={
        1:1,
        2:2,
        3:4,
        4:8,
        5:16,
        6:32
    }
    return numbers.get(num,None)
# 7
def get_vc_buf_size(num):
    numbers ={
        1:1,
        2:2,
        3:4,
        4:8,
        5:16,
        6:32,
        7:64
    }
    return numbers.get(num,None)


# print(getTopo(8))
# print(get_arb_type(1))
# print(get_num_vcs(1))
# print(get_priority(1))
# print(get_routing_fun(1))
# print(get_vc_allocator(1))
# print(get_vc_buf_size(1))



def creatConfigFile(x1,x2,x3,x4,x5,x6,x7):
    str_topo = "topology =" +get_topo(x1)+";"
    # print("-------"+str_topo)
    str_routing = "routing_function = " + get_routing_fun(x2)+";"
    str_vc_allocator = "vc_allocator = " + get_vc_allocator(x3)+";"
    str_arb_type = "arb_type = " + get_arb_type(x4)+";"
    str_priority = "priority =  " + get_priority(x5)+";"
    str_num_vcs = "num_vcs     = " +str( get_num_vcs(x6))+";"
    str_vc_buff_size = "vc_buf_size = " +str(get_vc_buf_size(x7))+";"
    # if(os.path.exists("wsy_booksim_congfig_file")):
    #     # file = open("wsy_booksim_config_file","w")
    #     # file.truncate()
    #     # file.close()
    os.remove("./wsy_work/wsy_booksim_config_file")
    file = open("./wsy_work/wsy_booksim_config_file","a")

    file.write("// Topology\n"+str_topo)
    file.write("\nk=16;")
    file.write("\nn=2;")
    file.write("\n\n\n// Routing\n"+str_routing)
    file.write("\n\n\n// Flow control\n"+str_num_vcs)
    file.write("\n"+str_vc_buff_size)
    file.write("\nwait_for_tail_credit = 1;")
    file.write("\n\n\n// Router architecture\n"+str_vc_allocator)
    file.write("\nsw_allocator = "+get_vc_allocator(x3)+";")
    file.write("\nalloc_iters  = 1;")
    file.write("\n\n\n\ncredit_delay   = 2;\nrouting_delay  = 0;\nvc_alloc_delay = 1;\nsw_alloc_delay = 1;")
    file.write("\n\n\n\ninput_speedup     = 2;\noutput_speedup    = 1;\ninternal_speedup  = 1.0;")
    file.write("\n\n\n")
    file.write("// Traffic\ntraffic = uniform;\npacket_size = 1;")
    file.write("\n\n\n")
    file.write("// Simulation\nsim_type = latency;\ninjection_rate = 0.005;")
    file.write("\n/////////////////////////////////////////////")





