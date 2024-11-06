#!/usr/bin/env python2
import socket
import struct

def read_db_acl():
    with open('./TCPFilters10k', 'r') as file:
        lines = file.readlines()
    rule_set=[]
    # Iterate through each line in the file
    for line in lines:
        # Split the line into columns using tabs as separators
        columns = line.strip().split('\t')
        tmpset=[]
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





if __name__ == '__main__':
    print(read_db_acl())