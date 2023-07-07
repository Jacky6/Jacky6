# 将掩码转化为前缀的格式,输出格式为字符串
def netmask_prefix(netmask):
    netmask_list = netmask.split('.')
    a1 = bin(int(netmask_list[0]))
    a2 = bin(int(netmask_list[1]))
    a3 = bin(int(netmask_list[2]))
    a4 = bin(int(netmask_list[3]))
    prefix = str(a1).count('1') + str(a2).count('1') + str(a3).count('1') + str(a4).count('1')
    return prefix

# 将前缀转化为掩码的格式,输出格式为字符串
def prefix_netmask(prefix):
    prefix = int(prefix)
    if prefix <= 8:
        a1 = 256 - 2**(8 - prefix)
        # print(a1)
        netmask = '{0}.0.0.0'.format(str(a1))
        return netmask
    elif 8 < prefix <= 16:
        a1 = 255
        a2 = 256 - 2**(16 - prefix)
        netmask = '{0}.{1}.0.0'.format(str(a1), str(a2))
        return netmask
    elif 16 < prefix <= 24:
        a1 = 255
        a2 = 255
        a3 = 256 - 2**(24 - prefix)
        netmask = '{0}.{1}.{2}.0'.format(str(a1), str(a2), str(a3))
        return netmask
    elif 24 < prefix <= 32:
        a1 = 255
        a2 = 255
        a3 = 255
        a4 = 256 - 2**(32 - prefix)
        netmask = '{0}.{1}.{2}.{3}'.format(str(a1), str(a2), str(a3), str(a4))
        return netmask
    else:
        return "前缀长度格式不正确"

# 将路由转化为’前缀+掩码‘的格式,输出格式为字符串
def network_netmask(network):
    if '/' in network:
        route = network.split('/')[0]
        netmask = prefix_netmask(int(network.split('/')[1]))
        return '{} {}'.format(route, netmask)
    elif ' ' in network and '.' in network.split(' ')[1]:
        route = network.split(' ')[0]
        netmask = network.split(' ')[1]
        return '{} {}'.format(route, netmask)
    elif ' ' in network and '.' not in  network.split(' ')[1]:
        route = network.split(' ')[0]
        netmask = prefix_netmask(int(network.split(' ')[1]))
        return '{} {}'.format(route, netmask)
    else:
        print('格式不正确')

# 将路由转化为’前缀+掩码长度‘的格式,输出格式为字符串
def network_prefix(network):
    if '/' in network:
        route = network.split('/')[0]
        prefix = network.split('/')[1]
        return '{} {}'.format(route, prefix)
    elif ' ' in network and '.' in network.split(' ')[1]:
        route = network.split(' ')[0]
        prefix = netmask_prefix(network.split(' ')[1])
        return '{} {}'.format(route, prefix)
    elif ' ' in network and '.' not in  network.split(' ')[1]:
        route = network.split(' ')[0]
        prefix = network.split(' ')[1]
        return '{} {}'.format(route, prefix)
    else:
        print('格式不正确')



