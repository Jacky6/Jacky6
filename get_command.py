
from python_module import network   # 获取静态路由的路由格式
from python_module import Static    # 获取目标分区的的路由模板
import pandas as pd                 # 用于读取目标分区的汇总路由
import re                           # 用于删除preference的回退脚本
ip_prefix01 = pd.read_excel(io='C:/Users/Jacky/Desktop/项目2023/服务域改造南北向切换/第三批次/服务域改造第三批次南北向操作手册V1.0.xlsx', sheet_name='本部路由梳理IPv4')



# 获取目标分区的静态路由,输出格式为列表
def get_command(dc, part):

    Part = part.upper()
    command_list = []
    if Part == 'OM':
        i = 0
        y = 19
    elif Part == 'FN':
        i = 8
        y = 14
    elif Part == 'FNE':
        i = 9
        y = 4
    elif Part == 'OP11':
        i = 1
        y = 2

    ip_prefix_list = []
    for index in range(0, y):
        ip_prefix_list.append(ip_prefix01.values[index][i])
    ip_prefix = '\n'.join(ip_prefix_list)

    for p in ip_prefix_list:
        ip = network.network_netmask(p)
        # print(ip)
        a = Static.static_route(dc, Part)
        for command in a:
            command = command.replace('network netmask', ip)
            command_list.append(command)
    return command_list

    # for commands in command_list:
    #     print(commands)

# 获取目标分区的静态路由的回退脚本,输出格式为列表
def get_command_back(dc, part):

    Part = part.upper()
    command_list = []
    if Part == 'OM':
        i = 0
        y = 19
    elif Part == 'FN':
        i = 8
        y = 14
    elif Part == 'FNE':
        i = 9
        y = 4
    elif Part == 'OP11':
        i = 1
        y = 2

    ip_prefix_list = []
    for index in range(0, y):
        ip_prefix_list.append(ip_prefix01.values[index][i])
    ip_prefix = '\n'.join(ip_prefix_list)

    for p in ip_prefix_list:
        ip = network.network_netmask(p)
        a = Static.static_route(dc, Part)
        for command in a:
            command = command.replace('network netmask', ip)
            command = re.sub('ip route', 'undo ip route', command)
            command = re.sub("preference .*", '', command)
            command_list.append(command)
    return command_list


def a():
    return "a"





























