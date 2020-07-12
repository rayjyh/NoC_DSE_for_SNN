import os
from creatConfigFile import get_topo
from creatConfigFile import get_routing_fun
from creatConfigFile import get_vc_allocator
from creatConfigFile import get_arb_type
from creatConfigFile import get_num_vcs
from creatConfigFile import get_vc_buf_size
from creatConfigFile import get_priority

def creat_cmesh_config(x1,x2,x3,x4,x5,x6,x7):
    str_topo = "topology =" +get_topo(x1)+";\n"
    str_routing = "routing_function = " + get_routing_fun(x2)+";\n"
    str_vc_allocator = "vc_allocator = " + get_vc_allocator(x3)+";\n"
    str_arb_type = "arb_type = " + get_arb_type(x4)+";\n"
    str_priority = "priority =  " + get_priority(x5)+";\n"
    str_num_vcs = "num_vcs     = " +str( get_num_vcs(x6))+";\n"
    str_vc_buff_size = "vc_buf_size = " +str(get_vc_buf_size(x7))+";\n"

    os.remove("./wsy_work/wsy_booksim_cmesh_config")
    file = open("./wsy_work/wsy_booksim_cmesh_config","a")

    file.write(str_topo)
    file.write("k = 8;\n")
    file.write("n = 2;\n")
    file.write("c = 4;\n")
    file.write("xr = 2;\n")
    file.write("yr = 2;\n")

    file.write(str_routing)
    file.write(str_vc_allocator)
    file.write(str_arb_type)
    file.write(str_arb_type)
    file.write(str_priority)
    file.write(str_num_vcs)
    file.write(str_vc_buff_size)


# creat_cmesh_config(3,3,1,1,1,3,3)