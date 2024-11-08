#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time


def myNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/12',
                  autoSetMacs=True
                  )

    info('[1;36m*** Adding controller[0m\n')

    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6633)

    info('[1;36m*** Add switches[0m\n')

    Lhasa = net.addSwitch('s1', cls=OVSKernelSwitch, dpid='0000000000000001')
    Lanzhou = net.addSwitch('s2', cls=OVSKernelSwitch, dpid='0000000000000002')
    Kashi = net.addSwitch('s3', cls=OVSKernelSwitch, dpid='0000000000000003')
    Shiquanhe = net.addSwitch('s4', cls=OVSKernelSwitch, dpid='0000000000000004')
    Jinan = net.addSwitch('s5', cls=OVSKernelSwitch, dpid='0000000000000005')
    Qingdao = net.addSwitch('s6', cls=OVSKernelSwitch, dpid='0000000000000006')
    Taiyuan = net.addSwitch('s7', cls=OVSKernelSwitch, dpid='0000000000000007')
    Shilazhuang = net.addSwitch('s8', cls=OVSKernelSwitch, dpid='0000000000000008')
    Shanghai = net.addSwitch('s9', cls=OVSKernelSwitch, dpid='0000000000000009')
    Suzhou = net.addSwitch('s10', cls=OVSKernelSwitch, dpid='0000000000000010')
    InternationalLink1 = net.addSwitch('s11', cls=OVSKernelSwitch, dpid='0000000000000011')
    InternationalLink2 = net.addSwitch('s12', cls=OVSKernelSwitch, dpid='0000000000000012')
    Nanning = net.addSwitch('s13', cls=OVSKernelSwitch, dpid='0000000000000013')
    Changsha = net.addSwitch('s14', cls=OVSKernelSwitch, dpid='0000000000000014')
    Guiyang = net.addSwitch('s15', cls=OVSKernelSwitch, dpid='0000000000000015')
    Chongqing = net.addSwitch('s16', cls=OVSKernelSwitch, dpid='0000000000000016')
    Chengdu = net.addSwitch('s17', cls=OVSKernelSwitch, dpid='0000000000000017')
    Kunming = net.addSwitch('s18', cls=OVSKernelSwitch, dpid='0000000000000018')
    Xian = net.addSwitch('s19', cls=OVSKernelSwitch, dpid='0000000000000019')
    Zhengzhou = net.addSwitch('s20', cls=OVSKernelSwitch, dpid='0000000000000020')
    InternationalLink4 = net.addSwitch('s21', cls=OVSKernelSwitch, dpid='0000000000000021')
    InternationalLink3 = net.addSwitch('s22', cls=OVSKernelSwitch, dpid='0000000000000022')
    Haikou = net.addSwitch('s23', cls=OVSKernelSwitch, dpid='0000000000000023')
    HongKong = net.addSwitch('s24', cls=OVSKernelSwitch, dpid='0000000000000024')
    Hangzhou = net.addSwitch('s25', cls=OVSKernelSwitch, dpid='0000000000000025')
    Wuhan = net.addSwitch('s26', cls=OVSKernelSwitch, dpid='0000000000000026')
    Hefei = net.addSwitch('s27', cls=OVSKernelSwitch, dpid='0000000000000027')
    Nanjing = net.addSwitch('s28', cls=OVSKernelSwitch, dpid='0000000000000028')
    Guangzhou = net.addSwitch('s29', cls=OVSKernelSwitch, dpid='0000000000000029')
    Xiamen = net.addSwitch('s30', cls=OVSKernelSwitch, dpid='0000000000000030')
    Fuzhou = net.addSwitch('s31', cls=OVSKernelSwitch, dpid='0000000000000031')
    Nandhang = net.addSwitch('s32', cls=OVSKernelSwitch, dpid='0000000000000032')
    Xining = net.addSwitch('s33', cls=OVSKernelSwitch, dpid='0000000000000033')
    Urumqi = net.addSwitch('s34', cls=OVSKernelSwitch, dpid='0000000000000034')
    Harbin = net.addSwitch('s35', cls=OVSKernelSwitch, dpid='0000000000000035')
    Changchun = net.addSwitch('s36', cls=OVSKernelSwitch, dpid='0000000000000036')
    Shenyang = net.addSwitch('s37', cls=OVSKernelSwitch, dpid='0000000000000037')
    Dalian = net.addSwitch('s38', cls=OVSKernelSwitch, dpid='0000000000000038')
    Tianjin = net.addSwitch('s39', cls=OVSKernelSwitch, dpid='0000000000000039')
    Beijing = net.addSwitch('s40', cls=OVSKernelSwitch, dpid='0000000000000040')
    Hohhot = net.addSwitch('s41', cls=OVSKernelSwitch, dpid='0000000000000041')
    Yinchuan = net.addSwitch('s42', cls=OVSKernelSwitch, dpid='0000000000000042')

    info('[1;36m*** Add hosts[0m\n')

    Lhasa_host = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    Lanzhou_host = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    Kashi_host = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    Shiquanhe_host = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    Jinan_host = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    Qingdao_host = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    Taiyuan_host = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    Shilazhuang_host = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    Shanghai_host = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    Suzhou_host = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    InternationalLink1_host = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    InternationalLink2_host = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    Nanning_host = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    Changsha_host = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    Guiyang_host = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    Chongqing_host = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    Chengdu_host = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    Kunming_host = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    Xian_host = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    Zhengzhou_host = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    InternationalLink4_host = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    InternationalLink3_host = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    Haikou_host = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    HongKong_host = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    Hangzhou_host = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    Wuhan_host = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    Hefei_host = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    Nanjing_host = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)
    Guangzhou_host = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    Xiamen_host = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    Fuzhou_host = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    Nandhang_host = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    Xining_host = net.addHost('h33', cls=Host, ip='10.0.0.33', defaultRoute=None)
    Urumqi_host = net.addHost('h34', cls=Host, ip='10.0.0.34', defaultRoute=None)
    Harbin_host = net.addHost('h35', cls=Host, ip='10.0.0.35', defaultRoute=None)
    Changchun_host = net.addHost('h36', cls=Host, ip='10.0.0.36', defaultRoute=None)
    Shenyang_host = net.addHost('h37', cls=Host, ip='10.0.0.37', defaultRoute=None)
    Dalian_host = net.addHost('h38', cls=Host, ip='10.0.0.38', defaultRoute=None)
    Tianjin_host = net.addHost('h39', cls=Host, ip='10.0.0.39', defaultRoute=None)
    Beijing_host = net.addHost('h40', cls=Host, ip='10.0.0.40', defaultRoute=None)
    Hohhot_host = net.addHost('h41', cls=Host, ip='10.0.0.41', defaultRoute=None)
    Yinchuan_host = net.addHost('h42', cls=Host, ip='10.0.0.42', defaultRoute=None)

    info('[1;36m*** Add links[0m\n')

    local_link = {'bw': 1000.0, 'delay': '0ms'}
    net.addLink(Lhasa, Lhasa_host, cls=TCLink, **local_link)
    net.addLink(Lanzhou, Lanzhou_host, cls=TCLink, **local_link)
    net.addLink(Kashi, Kashi_host, cls=TCLink, **local_link)
    net.addLink(Shiquanhe, Shiquanhe_host, cls=TCLink, **local_link)
    net.addLink(Jinan, Jinan_host, cls=TCLink, **local_link)
    net.addLink(Qingdao, Qingdao_host, cls=TCLink, **local_link)
    net.addLink(Taiyuan, Taiyuan_host, cls=TCLink, **local_link)
    net.addLink(Shilazhuang, Shilazhuang_host, cls=TCLink, **local_link)
    net.addLink(Shanghai, Shanghai_host, cls=TCLink, **local_link)
    net.addLink(Suzhou, Suzhou_host, cls=TCLink, **local_link)
    net.addLink(InternationalLink1, InternationalLink1_host, cls=TCLink, **local_link)
    net.addLink(InternationalLink2, InternationalLink2_host, cls=TCLink, **local_link)
    net.addLink(Nanning, Nanning_host, cls=TCLink, **local_link)
    net.addLink(Changsha, Changsha_host, cls=TCLink, **local_link)
    net.addLink(Guiyang, Guiyang_host, cls=TCLink, **local_link)
    net.addLink(Chongqing, Chongqing_host, cls=TCLink, **local_link)
    net.addLink(Chengdu, Chengdu_host, cls=TCLink, **local_link)
    net.addLink(Kunming, Kunming_host, cls=TCLink, **local_link)
    net.addLink(Xian, Xian_host, cls=TCLink, **local_link)
    net.addLink(Zhengzhou, Zhengzhou_host, cls=TCLink, **local_link)
    net.addLink(InternationalLink4, InternationalLink4_host, cls=TCLink, **local_link)
    net.addLink(InternationalLink3, InternationalLink3_host, cls=TCLink, **local_link)
    net.addLink(Haikou, Haikou_host, cls=TCLink, **local_link)
    net.addLink(HongKong, HongKong_host, cls=TCLink, **local_link)
    net.addLink(Hangzhou, Hangzhou_host, cls=TCLink, **local_link)
    net.addLink(Wuhan, Wuhan_host, cls=TCLink, **local_link)
    net.addLink(Hefei, Hefei_host, cls=TCLink, **local_link)
    net.addLink(Nanjing, Nanjing_host, cls=TCLink, **local_link)
    net.addLink(Guangzhou, Guangzhou_host, cls=TCLink, **local_link)
    net.addLink(Xiamen, Xiamen_host, cls=TCLink, **local_link)
    net.addLink(Fuzhou, Fuzhou_host, cls=TCLink, **local_link)
    net.addLink(Nandhang, Nandhang_host, cls=TCLink, **local_link)
    net.addLink(Xining, Xining_host, cls=TCLink, **local_link)
    net.addLink(Urumqi, Urumqi_host, cls=TCLink, **local_link)
    net.addLink(Harbin, Harbin_host, cls=TCLink, **local_link)
    net.addLink(Changchun, Changchun_host, cls=TCLink, **local_link)
    net.addLink(Shenyang, Shenyang_host, cls=TCLink, **local_link)
    net.addLink(Dalian, Dalian_host, cls=TCLink, **local_link)
    net.addLink(Tianjin, Tianjin_host, cls=TCLink, **local_link)
    net.addLink(Beijing, Beijing_host, cls=TCLink, **local_link)
    net.addLink(Hohhot, Hohhot_host, cls=TCLink, **local_link)
    net.addLink(Yinchuan, Yinchuan_host, cls=TCLink, **local_link)

    CityLink1 = {'bw': 128.0, 'delay': '6.3577ms'}
    net.addLink(Lhasa, Chengdu, cls=TCLink, **CityLink1)
    CityLink2 = {'bw': 128.0, 'delay': '5.5765ms'}
    net.addLink(Lhasa, Shiquanhe, cls=TCLink, **CityLink2)
    CityLink3 = {'bw': 128.0, 'delay': '13.0311ms'}
    net.addLink(Lhasa, Beijing, cls=TCLink, **CityLink3)
    CityLink4 = {'bw': 128.0, 'delay': '2.5809ms'}
    net.addLink(Lanzhou, Xian, cls=TCLink, **CityLink4)
    CityLink5 = {'bw': 128.0, 'delay': '6.0144ms'}
    net.addLink(Lanzhou, Beijing, cls=TCLink, **CityLink5)
    CityLink6 = {'bw': 128.0, 'delay': '5.475ms'}
    net.addLink(Kashi, Urumqi, cls=TCLink, **CityLink6)
    CityLink7 = {'bw': 128.0, 'delay': '3.7195ms'}
    net.addLink(Jinan, Shanghai, cls=TCLink, **CityLink7)
    CityLink8 = {'bw': 128.0, 'delay': '2.2364ms'}
    net.addLink(Qingdao, Tianjin, cls=TCLink, **CityLink8)
    CityLink9 = {'bw': 128.0, 'delay': '2.6293ms'}
    net.addLink(Taiyuan, Xian, cls=TCLink, **CityLink9)
    CityLink10 = {'bw': 128.0, 'delay': '2.0428ms'}
    net.addLink(Taiyuan, Beijing, cls=TCLink, **CityLink10)
    CityLink11 = {'bw': 128.0, 'delay': '1.3499ms'}
    net.addLink(Shilazhuang, Beijing, cls=TCLink, **CityLink11)
    CityLink12 = {'bw': 128.0, 'delay': '4.8911ms'}
    net.addLink(Shanghai, Tianjin, cls=TCLink, **CityLink12)
    CityLink13 = {'bw': 128.0, 'delay': '5.4287ms'}
    net.addLink(Shanghai, Beijing, cls=TCLink, **CityLink13)
    CityLink14 = {'bw': 128.0, 'delay': '0.4088ms'}
    net.addLink(Shanghai, Suzhou, cls=TCLink, **CityLink14)
    CityLink15 = {'bw': 128.0, 'delay': '0.4088ms'}
    net.addLink(Shanghai, InternationalLink2, cls=TCLink, **CityLink15)
    CityLink16 = {'bw': 128.0, 'delay': '8.4258ms'}
    net.addLink(Shanghai, Chengdu, cls=TCLink, **CityLink16)
    CityLink17 = {'bw': 128.0, 'delay': '6.1926ms'}
    net.addLink(Shanghai, Xian, cls=TCLink, **CityLink17)
    CityLink18 = {'bw': 128.0, 'delay': '10.1803ms'}
    net.addLink(Shanghai, HongKong, cls=TCLink, **CityLink18)
    CityLink19 = {'bw': 128.0, 'delay': '0.831ms'}
    net.addLink(Shanghai, Hangzhou, cls=TCLink, **CityLink19)
    CityLink20 = {'bw': 128.0, 'delay': '3.5048ms'}
    net.addLink(Shanghai, Wuhan, cls=TCLink, **CityLink20)
    CityLink21 = {'bw': 128.0, 'delay': '2.044ms'}
    net.addLink(Shanghai, Hefei, cls=TCLink, **CityLink21)
    CityLink22 = {'bw': 128.0, 'delay': '1.3738ms'}
    net.addLink(Shanghai, Nanjing, cls=TCLink, **CityLink22)
    CityLink23 = {'bw': 128.0, 'delay': '6.1602ms'}
    net.addLink(Shanghai, Guangzhou, cls=TCLink, **CityLink23)
    CityLink24 = {'bw': 128.0, 'delay': '3.0828ms'}
    net.addLink(Shanghai, Nandhang, cls=TCLink, **CityLink24)
    CityLink25 = {'bw': 128.0, 'delay': '0.9812ms'}
    net.addLink(Suzhou, Nanjing, cls=TCLink, **CityLink25)
    CityLink26 = {'bw': 128.0, 'delay': '5.2284ms'}
    net.addLink(InternationalLink1, Beijing, cls=TCLink, **CityLink26)
    CityLink27 = {'bw': 128.0, 'delay': '2.5722ms'}
    net.addLink(Nanning, Guangzhou, cls=TCLink, **CityLink27)
    CityLink28 = {'bw': 128.0, 'delay': '1.4911ms'}
    net.addLink(Changsha, Wuhan, cls=TCLink, **CityLink28)
    CityLink29 = {'bw': 128.0, 'delay': '2.6552ms'}
    net.addLink(Guiyang, Chengdu, cls=TCLink, **CityLink29)
    CityLink30 = {'bw': 128.0, 'delay': '3.8797ms'}
    net.addLink(Guiyang, Guangzhou, cls=TCLink, **CityLink30)
    CityLink31 = {'bw': 128.0, 'delay': '1.3659ms'}
    net.addLink(Chongqing, Chengdu, cls=TCLink, **CityLink31)
    CityLink32 = {'bw': 128.0, 'delay': '4.9746ms'}
    net.addLink(Chongqing, Guangzhou, cls=TCLink, **CityLink32)
    CityLink33 = {'bw': 128.0, 'delay': '7.1361ms'}
    net.addLink(Chengdu, Nanjing, cls=TCLink, **CityLink33)
    CityLink34 = {'bw': 128.0, 'delay': '6.2894ms'}
    net.addLink(Chengdu, Guangzhou, cls=TCLink, **CityLink34)
    CityLink35 = {'bw': 128.0, 'delay': '5.5392ms'}
    net.addLink(Kunming, Guangzhou, cls=TCLink, **CityLink35)
    CityLink36 = {'bw': 128.0, 'delay': '3.5552ms'}
    net.addLink(Xian, Xining, cls=TCLink, **CityLink36)
    CityLink37 = {'bw': 128.0, 'delay': '10.7636ms'}
    net.addLink(Xian, Urumqi, cls=TCLink, **CityLink37)
    CityLink38 = {'bw': 128.0, 'delay': '2.6678ms'}
    net.addLink(Xian, Yinchuan, cls=TCLink, **CityLink38)
    CityLink39 = {'bw': 128.0, 'delay': '4.6362ms'}
    net.addLink(Xian, Beijing, cls=TCLink, **CityLink39)
    CityLink40 = {'bw': 128.0, 'delay': '3.8979ms'}
    net.addLink(Xian, Hohhot, cls=TCLink, **CityLink40)
    CityLink41 = {'bw': 128.0, 'delay': '3.2847ms'}
    net.addLink(Xian, Wuhan, cls=TCLink, **CityLink41)
    CityLink42 = {'bw': 128.0, 'delay': '4.8194ms'}
    net.addLink(Xian, Nanjing, cls=TCLink, **CityLink42)
    CityLink43 = {'bw': 128.0, 'delay': '6.6482ms'}
    net.addLink(Xian, Guangzhou, cls=TCLink, **CityLink43)
    CityLink44 = {'bw': 128.0, 'delay': '3.1607ms'}
    net.addLink(Zhengzhou, Beijing, cls=TCLink, **CityLink44)
    CityLink45 = {'bw': 128.0, 'delay': '6.7785ms'}
    net.addLink(InternationalLink4, HongKong, cls=TCLink, **CityLink45)
    CityLink46 = {'bw': 128.0, 'delay': '6.581ms'}
    net.addLink(InternationalLink3, Guangzhou, cls=TCLink, **CityLink46)
    CityLink47 = {'bw': 128.0, 'delay': '6.2814ms'}
    net.addLink(Haikou, Wuhan, cls=TCLink, **CityLink47)
    CityLink48 = {'bw': 128.0, 'delay': '2.3121ms'}
    net.addLink(Haikou, Guangzhou, cls=TCLink, **CityLink48)
    CityLink49 = {'bw': 128.0, 'delay': '7.5465ms'}
    net.addLink(HongKong, Guangzhou, cls=TCLink, **CityLink49)
    CityLink50 = {'bw': 128.0, 'delay': '9.1697ms'}
    net.addLink(HongKong, Beijing, cls=TCLink, **CityLink50)
    CityLink51 = {'bw': 128.0, 'delay': '5.3593ms'}
    net.addLink(Wuhan, Beijing, cls=TCLink, **CityLink51)
    CityLink52 = {'bw': 128.0, 'delay': '2.3321ms'}
    net.addLink(Wuhan, Nanjing, cls=TCLink, **CityLink52)
    CityLink53 = {'bw': 128.0, 'delay': '4.5646ms'}
    net.addLink(Nanjing, Beijing, cls=TCLink, **CityLink53)
    CityLink54 = {'bw': 128.0, 'delay': '3.4006ms'}
    net.addLink(Nanjing, Fuzhou, cls=TCLink, **CityLink54)
    CityLink55 = {'bw': 128.0, 'delay': '9.25ms'}
    net.addLink(Guangzhou, Tianjin, cls=TCLink, **CityLink55)
    CityLink56 = {'bw': 128.0, 'delay': '9.6066ms'}
    net.addLink(Guangzhou, Beijing, cls=TCLink, **CityLink56)
    CityLink57 = {'bw': 128.0, 'delay': '2.6141ms'}
    net.addLink(Guangzhou, Xiamen, cls=TCLink, **CityLink57)
    CityLink58 = {'bw': 128.0, 'delay': '6.7435ms'}
    net.addLink(Xining, Beijing, cls=TCLink, **CityLink58)
    CityLink59 = {'bw': 128.0, 'delay': '12.2609ms'}
    net.addLink(Urumqi, Beijing, cls=TCLink, **CityLink59)
    CityLink60 = {'bw': 128.0, 'delay': '5.3735ms'}
    net.addLink(Harbin, Beijing, cls=TCLink, **CityLink60)
    CityLink61 = {'bw': 128.0, 'delay': '4.3706ms'}
    net.addLink(Changchun, Beijing, cls=TCLink, **CityLink61)
    CityLink62 = {'bw': 128.0, 'delay': '3.1891ms'}
    net.addLink(Shenyang, Beijing, cls=TCLink, **CityLink62)
    CityLink63 = {'bw': 128.0, 'delay': '1.9469ms'}
    net.addLink(Dalian, Tianjin, cls=TCLink, **CityLink63)
    CityLink64 = {'bw': 128.0, 'delay': '0.5499ms'}
    net.addLink(Tianjin, Beijing, cls=TCLink, **CityLink64)
    CityLink65 = {'bw': 128.0, 'delay': '2.1056ms'}
    net.addLink(Beijing, Hohhot, cls=TCLink, **CityLink65)
    CityLink66 = {'bw': 128.0, 'delay': '4.5055ms'}
    net.addLink(Beijing, Yinchuan, cls=TCLink, **CityLink66)

    info('\n[1;36m*** Starting network[0m\n')

    net.build()
    info('[1;36m*** Starting controllers[0m\n')

    for controller in net.controllers:
        controller.start()

    info('[1;36m*** Starting switches[0m\n')

    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s15').start([c0])
    net.get('s16').start([c0])
    net.get('s17').start([c0])
    net.get('s18').start([c0])
    net.get('s19').start([c0])
    net.get('s20').start([c0])
    net.get('s21').start([c0])
    net.get('s22').start([c0])
    net.get('s23').start([c0])
    net.get('s24').start([c0])
    net.get('s25').start([c0])
    net.get('s26').start([c0])
    net.get('s27').start([c0])
    net.get('s28').start([c0])
    net.get('s29').start([c0])
    net.get('s30').start([c0])
    net.get('s31').start([c0])
    net.get('s32').start([c0])
    net.get('s33').start([c0])
    net.get('s34').start([c0])
    net.get('s35').start([c0])
    net.get('s36').start([c0])
    net.get('s37').start([c0])
    net.get('s38').start([c0])
    net.get('s39').start([c0])
    net.get('s40').start([c0])
    net.get('s41').start([c0])
    net.get('s42').start([c0])

    info('\n[1;36m*** Post configure switches and hosts[0m\n')

    Lhasa.cmd('ifconfig s1 10.0.8.1')
    Lanzhou.cmd('ifconfig s2 10.0.8.2')
    Kashi.cmd('ifconfig s3 10.0.8.3')
    Shiquanhe.cmd('ifconfig s4 10.0.8.4')
    Jinan.cmd('ifconfig s5 10.0.8.5')
    Qingdao.cmd('ifconfig s6 10.0.8.6')
    Taiyuan.cmd('ifconfig s7 10.0.8.7')
    Shilazhuang.cmd('ifconfig s8 10.0.8.8')
    Shanghai.cmd('ifconfig s9 10.0.8.9')
    Suzhou.cmd('ifconfig s10 10.0.8.10')
    InternationalLink1.cmd('ifconfig s11 10.0.8.11')
    InternationalLink2.cmd('ifconfig s12 10.0.8.12')
    Nanning.cmd('ifconfig s13 10.0.8.13')
    Changsha.cmd('ifconfig s14 10.0.8.14')
    Guiyang.cmd('ifconfig s15 10.0.8.15')
    Chongqing.cmd('ifconfig s16 10.0.8.16')
    Chengdu.cmd('ifconfig s17 10.0.8.17')
    Kunming.cmd('ifconfig s18 10.0.8.18')
    Xian.cmd('ifconfig s19 10.0.8.19')
    Zhengzhou.cmd('ifconfig s20 10.0.8.20')
    InternationalLink4.cmd('ifconfig s21 10.0.8.21')
    InternationalLink3.cmd('ifconfig s22 10.0.8.22')
    Haikou.cmd('ifconfig s23 10.0.8.23')
    HongKong.cmd('ifconfig s24 10.0.8.24')
    Hangzhou.cmd('ifconfig s25 10.0.8.25')
    Wuhan.cmd('ifconfig s26 10.0.8.26')
    Hefei.cmd('ifconfig s27 10.0.8.27')
    Nanjing.cmd('ifconfig s28 10.0.8.28')
    Guangzhou.cmd('ifconfig s29 10.0.8.29')
    Xiamen.cmd('ifconfig s30 10.0.8.30')
    Fuzhou.cmd('ifconfig s31 10.0.8.31')
    Nandhang.cmd('ifconfig s32 10.0.8.32')
    Xining.cmd('ifconfig s33 10.0.8.33')
    Urumqi.cmd('ifconfig s34 10.0.8.34')
    Harbin.cmd('ifconfig s35 10.0.8.35')
    Changchun.cmd('ifconfig s36 10.0.8.36')
    Shenyang.cmd('ifconfig s37 10.0.8.37')
    Dalian.cmd('ifconfig s38 10.0.8.38')
    Tianjin.cmd('ifconfig s39 10.0.8.39')
    Beijing.cmd('ifconfig s40 10.0.8.40')
    Hohhot.cmd('ifconfig s41 10.0.8.41')
    Yinchuan.cmd('ifconfig s42 10.0.8.42')

    ####################################
    #### USER SIMULATION CODE HERE #####
    ####################################

    # Your automatic simulation code.

    ####################################

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()