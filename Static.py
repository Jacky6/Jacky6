import re

# 用于获取现网分区分区的静态路由模板配置,输出格式为列表
def static_route(dc, part):

    if dc.upper() == 'SHE':
        Part = part.upper()
        # print(Part)
        list02 = []
        file = 'E:/20230704/交换机设备配置/SHE2003_{}_DS_01.txt'.format(Part)
        with open(file, 'r') as f:
            list01 = f.readlines()
            for i in list01:
                if re.match('ip route-static vpn-instance .*', i) and re.search('ABC|VRF', i) and 'preference 1' not in i:
                    list02.append(i)
                    break
            for i in list01:
                if re.match('ip route-static vpn-instance .*', i) and re.search('ABC|VRF', i) and 'preference 1' in i:
                    list02.append(i)
                    break

        # print(list02)
        a = list02[0].split(' ')
        a[4] = 'network'
        a[5] = 'netmask'
        a[-1] = a[-1].replace('\n', '')
        fw_route = " ".join(a)
        b = list02[1].split(' ')
        b[4] = 'network'
        b[5] = 'netmask'
        b[-1] = b[-1].replace('\n', '')
        bypass_route = " ".join(b)
        command = []
        command.append(fw_route)
        command.append(bypass_route)
        return command

    elif dc.upper() == 'SHTC':
        Part = part.upper()
        # print(Part)
        list02 = []
        file = 'E:/20230704/交换机设备配置/SHTC07_{}_DS_01.txt'.format(Part)
        with open(file, 'r') as f:
            list01 = f.readlines()
            for i in list01:
                if re.match('ip route-static vpn-instance .*[ABC|VRF] .*', i) and 'preference 1' not in i:
                    list02.append(i)
                    break
            for i in list01:
                if re.match('ip route-static vpn-instance .*[ABC|VRF] .* preference 1', i):
                    list02.append(i)
                    break
        # print(list02[0])
        # print(list02[1])
        a = list02[0].split(' ')
        a[4] = 'network'
        a[5] = 'netmask'
        a[-1] = a[-1].replace('\n', '')
        fw_route = " ".join(a)
        b = list02[1].split(' ')
        b[4] = 'network'
        b[5] = 'netmask'
        b[-1] = b[-1].replace('\n', '')
        bypass_route = " ".join(b)
        command = []
        command.append(fw_route)
        command.append(bypass_route)
        return command






