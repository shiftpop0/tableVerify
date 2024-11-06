import requests

# 数据来源 https://blackip.ustc.edu.cn
def get_blacklist():  #1W
    url="https://blackip.ustc.edu.cn/list.php?txt"
    response = requests.get(url)
    text = response.text.split('\n')[:-1]
    ip_list = []
    for index,item_ip in enumerate(text):
        if ":" in item_ip:
            continue
        if "/" not in item_ip:
            ip_list.append('@'+item_ip+"/32")
        else:
            ip_list.append('@'+item_ip)
    return ip_list


# 数据来源 https://myip.ms/browse/blacklist/Blacklist_IP_Blacklist_IP_Addresses_Live_Database_Real-time
def read_full_blacklist_database():  #13W
    with open('../Data/full_blacklist_database.txt', 'r') as file:
        lines = file.readlines()
    rule_set=[]
    for line in lines:
        if ":" in line:
            continue
        columns = line.strip().split('\t')
        ip = columns[0]
        rule_set.append('@'+ip+"/32")
    return rule_set

# 数据来源 https://github.com/maravento/blackip
def read_github_blackip():  #124w
    with open('../Data/blackip.txt', 'r') as file:
        lines = file.readlines()
    rule_set=[]
    for line in lines:
        if ":" in line:
            continue
        columns = line.strip().split('\t')
        ip = columns[0]
        rule_set.append('@'+ip+"/32")
    return rule_set

# 数据来源 https://github.com/stamparm/ipsum
def read_github_ipsum(n = 8):
    with open('../Data/levels/{}.txt'.format(n), 'r') as file:
        lines = file.readlines()
    rule_set=[]
    for line in lines:
        rule_set.append('@'+line+"/32")
    return rule_set

if __name__ == '__main__':
    read_github_blackip()