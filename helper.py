#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
import os 
import sys
import time
import datetime
import Image
'''
def openlogfile():
	if os.path.exists('log.log'):	
		logFile = open('log.log', 'a')
		logFile.writelines('='*80 + '\n') 
		logFile.writelines('Executed at ' + timeNow() + '\n'*2) 
		logFile.writelines('='*80 + '\n') 
	else:
		logFile = open('log.log', 'a')
	return logFile
'''

def openlogfile():
	logFile = open('log.log', 'a')
	logFile.writelines('='*80 + '\n') 
	logFile.writelines('Executed at ' + timeNow() + '\n'*2) 
	#logFile.writelines('='*80 + '\n') 
	return logFile


def log(logFile, logInfo):
	logFile.writelines(logInfo + '\n')

def timeNow():
	return datetime.datetime.now().strftime('[%Y %b %d %H:%M:%S %a]')
	#[Sat Jul 07 10:34:39 2012] 

def getdirsize(dir):
	size = 0L
	for root, dirs, files in os.walk(dir):
		size += sum(
		[os.path.getsize(os.path.join(root, name)) for name in files])
	return size

def byte2MB(byteSize):
	return '%.3fMB' %(float (byteSize) / 1024 / 1024)

def main():
	print timeNow()
#	print getdirsize(os.getcwd())
	cdir = os.getcwd()
	print cdir
	print getdirsize(cdir)
	print byte2MB(getdirsize(cdir))


if __name__ == '__main__':
	main()