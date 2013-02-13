#!/usr/bin/env python2.7
#codeing = utf-8
import os
import sys
import time
import Image
import helper


def fileCountIn(dir):
    return sum([len(files) for root,dirs,files in os.walk(dir)])

def compress(fullPathOfFile, ratio = 1.0):
	dirname, filename = os.path.split(fullPathOfFile)
	try:
		im = Image.open(fullPathOfFile)
	except Exception, e:
		#print '%s can not open'% filename
		#info = filename + ' can no open'
		print e
		return  ('[file]'.ljust(6) + ':' + fullPathOfFile + '\n' +
				'[Exception]: ' + str(e)
				)
		#return str(e)
	wide, hight = im.size
	wide *= ratio
	hight *= ratio
	out = im.resize((int(wide),int(hight)))
	try:
		out.save(fullPathOfFile)
	except Exception, e:
		print e
		#info = filename + ' can no save'
		return  ('[file]'.ljust(6) + ':' + fullPathOfFile + '\n' +
				'[Exception]: ' + str(e)
				)

	info = '[file]'.ljust(6) + ':' + fullPathOfFile  + '\nwide:' + str(int(wide)) + ', hight:' + str(int(hight)) + '\n'
	return info
	
def isImage(filename):
	filename = filename.lower()
	if filename[-4:] == '.jpg' or filename[-5:] == '.jpeg': #or filename[-4:] =='.bmp':
		return True;
	else:
		return False;

def main():
	timeStart = time.clock()
	if 2 == len(sys.argv) or 1 == len(sys.argv):
		bInput = raw_input("!"* 80 +
							"Warning:".center(79, '_')+ "\n" + 
							"!This executable program will compress ALL JPEG files\n" 
							"!in your current dir\n"  + 
							os.getcwd().center(79,'_') + '\n'
							"!and REPLACE the original files!!!\n" +  
							'!'*79 + '\n'
							"continue? \n"
							 "y? or n?\n")
		if (bInput.lower().strip() == 'y' or 
			bInput.lower().strip() == 'yes'):
			print 'yes'
		else:
			print 'More to read README or -h --help'
			os.system('pause')
			return
		timeStart = time.clock()
		logfile = helper.openlogfile()
		if 2 == len(sys.argv):
			try:
				ratio =  float(sys.argv[1])
				if ratio > 10:
					ratio = ratio / 100
				elif ratio > 1:
					print 'cannot compress this ratio'
					sys.exit()
				elif ratio > 0:
					pass
				else:
					print 'error: ratio'
					sys.exit()

			except Exception, e:
				print '"%s" is a number?' %sys.argv[1]
				print 'Are you kidding?'
				sys.exit()
		else:
			ratio = 1.0

		numCompleted = 0
		numFile = fileCountIn(os.getcwd())
		bPrintedDir = False
		for root,dirs,files in os.walk(os.getcwd()):
			bPrintedDir = False
			for filename in files:
				fullPathOfFile = root +'\\' + filename
				#helper.log(logfile, fullPathOfFile)
				if isImage(fullPathOfFile):
					if False == bPrintedDir:
						info = '-'* 80 + '\n' +'[dir]'.ljust(6) +":"+  root + '\n' + helper.timeNow() + '\n'
						helper.log(logfile, info)
						bPrintedDir = True
					info = compress(fullPathOfFile,ratio)
					print info
					helper.log(logfile, info)
					#print fullPathOfFile
				numCompleted += 1
				per = float(100) * numCompleted / numFile 
				print 'complete files: %d / %d, %.2f%%' %(numCompleted, numFile, per)
		timeEnd = time.clock()
		info = '[Finished in %.1fs]\n' %(timeEnd - timeStart)
		helper.log(logfile, info)
		print info
		logfile.close()


	else:
		print error

	timeEnd = time.clock()

	'''
	if raw_input("press any key to continue:"):
		pass
	'''
	#print "press any key to continue:"
	os.system('pause')
	#raw_input()
	#input()

if __name__ == '__main__':
	main()
