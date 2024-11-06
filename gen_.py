# This is a sample Python script.
import ipaddress
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import socket


#生成恶意流量


def generate_decimal_ip():
    # 生成四个随机的十进制数作为IP地址的四个部分
    decimal_parts = [str(random.randint(0, 255)) for _ in range(4)]

    # 将四个部分连接成IP地址
    decimal_ip = '.'.join(decimal_parts)

    return decimal_ip


def generate_random_port():
    # 生成一个随机的端口号（0到65535之间）
    random_port = random.randint(0, 65535)

    return random_port


def read_db_acl():
    with open('Data/TCPFilters10k', 'r') as file:
        lines = file.readlines()
    rule_set = []
    # Iterate through each line in the file
    for line in lines:
        # Split the line into columns using tabs as separators
        columns = line.strip().split('\t')
        tmpset = []
        # Extract values from the columns
        source_ip = columns[0].split('@')[1].split('/')
        dest_ip = columns[1].split('/')
        source_port_range = columns[2].split(':')
        dest_port_range = columns[3].split(':')
        protocol = columns[4].split('/')

        # Append extracted values to the respective lists
        tmpset.append(source_ip)
        tmpset.append(dest_ip)
        tmpset.append(source_port_range)
        tmpset.append(dest_port_range)
        tmpset.append(protocol)
        rule_set.append(tmpset)
    return rule_set


def get_network_address(ip_cidr):
    # 创建 IPv4Network 对象
    network = ipaddress.IPv4Network(ip_cidr, strict=False)

    # 获取网络地址
    network_address = network.network_address

    return str(network_address)


def ip_to_bits_array(ip_address):
    # 使用socket.inet_pton将IP地址转换为字节
    ip_bytes = socket.inet_pton(socket.AF_INET, ip_address)

    # 将每个字节转换为对应的位数组
    bits_array = [bin(byte)[2:].zfill(8) for byte in ip_bytes]

    # 将位数组连接成一个大的数组
    flattened_bits_array = ''.join(bits_array)

    return flattened_bits_array


def checkIp(ip1, ip2, cidr):
    ipBits1 = ip_to_bits_array(ip1)
    ipBits2 = ip_to_bits_array(ip2)
    for i in range(0, cidr):
        if ipBits1[i] != ipBits2[i]:
            return i
    return cidr


def main():
    rule_set = read_db_acl()
    check_num_load = []
    for i in range(0, 1):
        sourceIp = generate_decimal_ip()
        sourcePort = generate_random_port()
        destIp = generate_decimal_ip()
        destPort = generate_random_port()
        maxCount = 0
        maxInfos = []
        maxRule = ''
        for rule in rule_set:
            count = 0
            infos = []
            srcCheckAddr = get_network_address(rule[0][0] + "/" + rule[0][1])
            dstCheckAddr = get_network_address(rule[1][0] + "/" + rule[1][1])
            srcCheckCidr = int(rule[0][1])
            dstCheckCidr = int(rule[1][1])
            srcCheckPorts = [int(rule[2][0]), int(rule[2][1])]
            dstCheckPorts = [int(rule[3][0]), int(rule[3][1])]
            check1 = checkIp(srcCheckAddr, sourceIp, srcCheckCidr)
            infos.append('源IP地址命中了: ' + str(check1) + '位')
            count = count + 1
            if check1 == srcCheckCidr:
                # 源IP地址匹配上了
                count = count + 1
                if dstCheckAddr == '0.0.0.0' and dstCheckCidr == 1:
                    k = 1
                check2 = checkIp(dstCheckAddr, destIp, dstCheckCidr)
                infos.append('目的IP地址命中了: ' + str(check2) + '位')
                if check2 == dstCheckCidr:
                    # 目的IP地址匹配上了
                    count = count + 1
                    if sourcePort >= srcCheckPorts[0] and sourcePort <= srcCheckPorts[1]:
                        # 源端口范围匹配上了
                        count = count + 1
                        infos.append('源端口号命中了')
                        if destPort >= dstCheckPorts[0] and destPort <= dstCheckPorts[1]:
                            infos.append('目的端口号命中了')
            if count > maxCount:
                maxCount = count
                maxInfos = infos
                maxRule = rule
        # print('srcIp: ' + sourceIp + '; dstIp: ' + destIp + '; sourcePort: ' + str(sourcePort) + '; destPort: ' + str(destPort))
        # print(maxCount, maxInfos, maxRule)
        tmp_laod = 0
        tmp_laod += 32
        if maxCount>1:
            tmp_laod += 32
            if maxCount>2:
                tmp_laod+=9*(maxCount-2)
            if maxCount==4:
                tmp_laod+=2
        check_num_load.append(tmp_laod)
        # print(tmp_laod)
    return check_num_load[0]


if __name__ == '__main__':
    for tmp in range(10):
        check_num_load = 0
        time = 100
        for i in range(0,time):
            j=random.randint(0,10)
            if j==0:
                check_num_load += main()
            else:
                check_num_load += 84
        print('{:.2f}'.format((check_num_load/50)/200))
