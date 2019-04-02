#coding=utf-8
__author__ = '冬冬'

import struct,socket,time

ICMP_ECHO_REQUEST = 8

def check_sum(source):
	sum = 0
	countTo = (len(source)//2)*2
	count = 0
	while count<countTo:
		thisVal = ord(source[count + 1])*256 + ord(source[count])
		sum = sum + thisVal
		sum = sum & 0xffffffff
		count += 2
	if countTo<len(source):
		sum = sum + ord(source[len(source)-1])
		sum = sum & 0xffffffff

	sum = (sum >> 16) + (sum &0xffff)
	sum = sum + (sum >> 16)
	answer = ~sum
	answer = answer & 0xffff
	answer = answer >>8|(answer <<8 & 0xff00)
	return answer

def send_one_packet(my_socket,dest_addr):
	my_checksum = 0
	header = struct.pack('BBHHH',ICMP_ECHO_REQUEST,0,my_checksum,0,0)#报头
	data = struct.pack("BBBB",1,2,3,4)#数据段

	my_checksum = check_sum(header + data)

	header = struct.pack('BBHHH',ICMP_ECHO_REQUEST,0,socket.htons(my_checksum),0,0)
	packet = header + data
	try:
		my_socket.sendto(packet,(dest_addr,1))
	except Exception as e:
		print(e)
def receive_one_packet(my_socket,timeout):
	my_socket.settimeout(timeout)
	starttime = time.time()
	try:
		data,addr_info = my_socket.recvfrom(1024)
	except socket.timeout:
		return None
	timeconsume = time.time() - starttime
	return timeconsume*1000

def ping(dest_addr,timeout):
	icmp = socket.getprotobyname("icmp")
	my_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)

	send_one_packet(my_socket,dest_addr)
	delaytime = receive_one_packet(my_socket,timeout)
	return delaytime


