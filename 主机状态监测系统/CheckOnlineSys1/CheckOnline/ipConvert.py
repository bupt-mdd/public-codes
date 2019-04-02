#coding=utf-8
__author__ = '冬冬'
import struct,socket
from CheckOnline.models import Item

def ipToLong(ip):                #ip地址到整形
	IP = socket.inet_aton(ip)
	return struct.unpack("!L",IP)[0]

def longToIp(long):              #整形到ip地址
	return socket.inet_ntoa(struct.pack("!L",long))

def netSegToList(startIp,endIp):
	startIp = ipToLong(startIp)
	endIp = ipToLong(endIp)
	ls = []
	for x in range(startIp,endIp + 1):
		ls.append(longToIp(x))
	return ls

