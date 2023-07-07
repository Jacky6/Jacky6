
from python_module import network


def gataway(ip1_str):
    ip1_str01 = network.network_netmask(ip1_str)
    ip1 = ip1_str01.split(' ')[0]
    netmask1 = ip1_str01.split(' ')[1]
    prefix1 = network.netmask_prefix(netmask1)
    hostnum = 2 ** (32 - prefix1)
    # print(hostnum)
    ip1_list = ip1.split('.')
    netmask1_list = netmask1.split('.')

    network1_list = []
    network1_list_str = []
    network_vip_list_str =[]
    network_01ip_list_str = []
    network_02ip_list_str = []

    for i in range(0, 4):
        ips = list(bin(int(ip1_list[i])).replace('0b', ''))
        net = list(bin(int(netmask1_list[i])).replace('0b', ''))
        if len(ips) == 8 and len(net) == 8:
            # print(ips)
            # print(net)
            # print(ips[4])
            # print(net[4])
            # print(bool(int(ips[4])) and bool(int(net[4])))
            list01 = ['0b']
            for y in range(0, 8):
                a = str(int((bool(int(ips[y])) and bool(int(net[y])))))
                list01.append(a)
            # print(list01)
            a_srt = ''.join(list01)
            network1_list.append((int(a_srt, 2)))

        elif len(ip1_list) != 8 or len(ips) != 8:
            for i in range(0, 8 - len(ips)):
                ips.insert(0, '0')
            for i in range(0, 8 - len(net)):
                net.insert(0, '0')
            # print(ips)
            # print(net)
            # print(ips[4])
            # print(net[4])
            # print(bool(int(ips[4])) and bool(int(net[4])))

            list01 = ['0b']
            for y in range(0, 8):
                a = str(int((bool(int(ips[y])) and bool(int(net[y])))))
                list01.append(a)
            # print(list01)
            a_srt = ''.join(list01)
            network1_list.append((int(a_srt, 2)))
    # print(network1_list)
    for a in network1_list:
        network1_list_str.append(str(a))



    # print(network1_list_str)
    for i in network1_list_str:
        network_vip_list_str.append(i)
        network_01ip_list_str.append(i)
        network_02ip_list_str.append(i)

    ip_network = '.'.join(network1_list_str)
    network_vip_list_str[3] = str(int(network1_list_str[3]) + hostnum - 2)
    # print(network_vip_list_str)
    network_01ip_list_str[3] = str(int(network_vip_list_str[3]) - 1)
    # print(network_01ip_list_str)
    network_02ip_list_str[3] = str(int(network_01ip_list_str[3]) - 1)
    # print(network_02ip_list_str)
    # print(network1_list_str)
    ip_vip = '.'.join(network_vip_list_str)
    ip_01ds = '.'.join(network_01ip_list_str)
    ip_02ds = '.'.join(network_02ip_list_str)
    # print(ip_network)
    # print(ip_host)

    #
    # print(network_vip_list_str)
    # print(network_01ip_list_str)
    # print(network_02ip_list_str)
    # print(ip_vip)
    # print(ip_01ds)
    # print(ip_02ds)
    # ip_gateway = [ip_vip, ip_01ds, ip_02ds]
    return ip_vip, ip_01ds, ip_02ds