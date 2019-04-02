#coding=utf-8
__author__ = '冬冬'

from CheckOnline.ping import ping
import threading
lock = threading.Lock()
ipAddressDict={}

def scan(ip,timeout = 0.1):
	global ipAddressDict
	if ping(ip,timeout) != None:
		lock.acquire()
		ipAddressDict[ip] = 'YES'
		lock.release()
	else:
		lock.acquire()
		ipAddressDict[ip] = 'NO'
		lock.release()

def netTest(ipAddressList):
	global ipAddressDict

	threads = []

	for ip in ipAddressList:
		threads.append(threading.Thread(target = scan,args = (ip,)))

	for x in range(len(ipAddressList)):
		threads[x].start()

	for x in range(len(ipAddressList)):
		threads[x].join()

	return ipAddressDict
