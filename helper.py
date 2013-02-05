#codeing = utf-8
import os 
import sys
import time
import datetime
import Image

def openlogfile():
	if os.path.exists('log.log'):	
		logFile = open('log.log', 'a')
		logFile.writelines('\n')
	else:
		logFile = open('log.log', 'a')
	return logFile

def log(logFile, logInfo):
	logFile.writelines(logInfo + '\n')


def timeNow():
	return datetime.datetime.now().strftime('[%Y %b %d %H:%M:%S %a]')
	#[Sat Jul 07 10:34:39 2012] 
def main():
	print timeNow()


if __name__ == '__main__':
	main()