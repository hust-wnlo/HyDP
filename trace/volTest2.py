




file = open("Result.csv", "a+")

import numpy as np
import math

ID_list = [ID for ID in range(0, 1000)]



time_interval = 3600   # 时间步长
RW_type = 'K'
all_time = 31 * 24 * 3600  # s



for ID_value in ID_list:
    ID = ID_value
    path = "vol/ID_%s.csv" % str(ID)

    fp = open(path, "r")
    all_size = 0
    for eachline in fp: # 先统计一波总的size

        line = eachline[:-1].split(",")
        RW = line[1][0]         # R or W
        size = int(line[3])     # bytes
        # time = int(line[4])     # us  1000000us = 1s

        if RW != RW_type:
            all_size += size
    fp.close()



    fp = open(path, "r")
    s_size = 0
    s_min, s_max = float('inf'), -1 * float('inf')

    s_end = 1577808000 + time_interval
    # m_end = 1577808000 + 60

    for eachline in fp:

        line = eachline[:-1].split(",")
        RW = line[1][0]         # R or W
        time = int(line[4]) / 1000000     # us  1000000us = 1s

        if RW != RW_type:
            if time > s_end:    # 重新计算新的周期
                if s_size < s_min:
                    s_min = s_size
                if s_size > s_max:
                    s_max = s_size

                while time > s_end:
                    s_min = 0 # 进入意味着已经出现了空周期
                    s_end += time_interval
                s_size = size
            else:
                s_size += size


    fp.close()

    ss = str(ID) + ',' + str(round(all_size / 1024, 2))  # KB
    ss += "," + str(round(s_min, 3)) + "," + str(round(s_max, 3))  # bytes

    print(ss)

    file.write(ss + "\n")
    file.flush()

file.close()

















































