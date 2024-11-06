import random


def caculate_standard_deviation(list):
    sum = 0
    for item in list:
        sum += item
    average = sum/len(list)
    sum = 0
    for item in list:
        sum += (item - average)**2
    return average, (sum/len(list))**0.5

def main():
    low = 64
    high = 128
    exp = [[],[]] # 0: avg, 1: std
    for i in range(11):
        list = []
        for j in range(100):
            cap = random.randint(low, high)
            utilization = 104/cap
            # print(utilization)
            list.append(utilization)
        avg, std = caculate_standard_deviation(list)
        exp[0].append(avg)
        exp[1].append(std)
    for item in exp:
        for item2 in item:
            print(item2, end=', ')
        print()

if __name__ == '__main__':
    main()