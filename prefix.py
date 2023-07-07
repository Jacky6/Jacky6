import re

# 用于获取现网分区分区的前缀列表模板配置,输出格式为列表
def ospf_prefix(dc, part):

    if dc.upper() == 'SHE':
        Part = part.upper()
        file = 'E:/20230704/交换机设备配置/SHE2003_{}_DS_01.txt'.format(Part)
        with open(file, 'r') as f:
            cfg = f.read()
            cfg_list = cfg.split('\n#\n')
            for i in cfg_list:
                if re.match('ospf', i) and re.search('router-id|vpn-instance|VRF', i):
                    ospf_command_list = i.split('\n')
                    # print(ospf_command_list)
                    for ospf_command in ospf_command_list:
                        if re.search('import-route ', ospf_command):
                            # print(ospf_command)
                            command_list_ospf = ospf_command.split(' ')
                            route_policy_index = command_list_ospf.index('route-policy')
                            route_policy_name_index = route_policy_index + 1
                            route_policy_name = command_list_ospf[route_policy_name_index]
                            break
            print('本部{}分区OSPF协议调用的路由策略的名字为{}'.format(Part, route_policy_name))
            # return route_policy_name
            for x in cfg_list:
                if re.match('route-policy', x) and re.search(route_policy_name, x):
                    # print(x)
                    route_policy_command_list = x.split('\n')
                    for route_policy_command in route_policy_command_list:
                        if re.search('if-match', route_policy_command):
                            command_list_prefix = route_policy_command.split(' ')
                            ip_prefix_index = command_list_prefix.index('ip-prefix')
                            ip_prefix_name_index = ip_prefix_index + 1
                            ip_prefix_name = command_list_prefix[ip_prefix_name_index]
            print('本部{}分区OSPF协议调用的前缀列表的名字为{}'.format(Part, ip_prefix_name))


                    # if re.match('#', i):
                    #     break



        # print(list02)
    #     a = list02[0].split(' ')
    #     a[4] = 'network'
    #     a[5] = 'netmask'
    #     a[-1] = a[-1].replace('\n', '')
    #     fw_route = " ".join(a)
    #     b = list02[1].split(' ')
    #     b[4] = 'network'
    #     b[5] = 'netmask'
    #     b[-1] = b[-1].replace('\n', '')
    #     bypass_route = " ".join(b)
    #     command = []
    #     command.append(fw_route)
    #     command.append(bypass_route)
    #     return command
    #
    # elif dc.upper() == 'SHTC':
    #     Part = part.upper()
    #     # print(Part)
    #     list02 = []
    #     file = 'E:/20230704/交换机设备配置/SHTC07_{}_DS_01.txt'.format(Part)
    #     with open(file, 'r') as f:
    #         list01 = f.readlines()
    #         for i in list01:
    #             if re.match('ip route-static vpn-instance .*[ABC|VRF] .*', i) and 'preference 1' not in i:
    #                 list02.append(i)
    #                 break
    #         for i in list01:
    #             if re.match('ip route-static vpn-instance .*[ABC|VRF] .* preference 1', i):
    #                 list02.append(i)
    #                 break
    #     # print(list02[0])
    #     # print(list02[1])
    #     a = list02[0].split(' ')
    #     a[4] = 'network'
    #     a[5] = 'netmask'
    #     a[-1] = a[-1].replace('\n', '')
    #     fw_route = " ".join(a)
    #     b = list02[1].split(' ')
    #     b[4] = 'network'
    #     b[5] = 'netmask'
    #     b[-1] = b[-1].replace('\n', '')
    #     bypass_route = " ".join(b)
    #     command = []
    #     command.append(fw_route)
    #     command.append(bypass_route)
    #     return command


def bgp_prefix(dc, part):

    if dc.upper() == 'SHE':
        Part = part.upper()
        file = 'E:/20230704/交换机设备配置/SHE2003_{}_DS_01.txt'.format(Part)
        with open(file, 'r') as f:
            cfg = f.read()
            cfg_list = cfg.split('\n#\n')
            # print(cfg_list)
            for i in cfg_list:
                if re.match('bgp', i):
                    bgp_command_list = i.split('#')
                    # print(bgp_command_list)
                    for bgp_command_family in bgp_command_list:
                        if re.search('route-policy ', bgp_command_family):
                            # print(bgp_command_family)
                            command_list_bgp_01 = bgp_command_family.split('\n')
                            command_list_bgp = bgp_command_family.split(' ')
                            # print(command_list_bgp)
                            for family_name in command_list_bgp_01:
                                if '-family' in family_name:
                                    # print(family_name)
                                    bgp_family_name = family_name
                                else:
                                    continue
                            # print(bgp_family_name)
                            route_policy_index = command_list_bgp.index('route-policy')
                            route_policy_name_index = route_policy_index + 1
                            route_policy_name = command_list_bgp[route_policy_name_index]
                            print('本部{}分区BGP协议的{} 地址族调用的路由策略的名字为 {}'.format(Part, bgp_family_name, route_policy_name))

    if dc.upper() == 'SHTC':
        Part = part.upper()
        file = 'E:/20230704/交换机设备配置/SHTC07_{}_DS_01.txt'.format(Part)
        with open(file, 'r') as f:
            cfg = f.read()
            cfg_list = cfg.split('\n#\n')
            # print(cfg_list)
            for i in cfg_list:
                if re.match('bgp', i):
                    bgp_command_list = i.split('#')
                    # print(bgp_command_list)
                    for bgp_command_family in bgp_command_list:
                        if re.search('route-policy ', bgp_command_family):
                            # print(bgp_command_family)
                            command_list_bgp_01 = bgp_command_family.split('\n')
                            command_list_bgp = bgp_command_family.split(' ')
                            # print(command_list_bgp)
                            for family_name in command_list_bgp_01:
                                if '-family' in family_name:
                                    # print(family_name)
                                    bgp_family_name = family_name
                                else:
                                    continue
                            # print(bgp_family_name)
                            route_policy_index = command_list_bgp.index('route-policy')
                            route_policy_name_index = route_policy_index + 1
                            route_policy_name = command_list_bgp[route_policy_name_index]
                            print('同城{}分区BGP协议的{} 地址族调用的路由策略的名字为 {}'.format(Part, bgp_family_name, route_policy_name))
