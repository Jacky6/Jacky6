import subprocess

def ifping(ip, timeout='500'):

    res = subprocess.call(["ping", '-n', '1', '-w', timeout, ip], stdout=subprocess.PIPE)
    if res == 0:
        return True
    else:
        print(ip, '不可达')
        return False
