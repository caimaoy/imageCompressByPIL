#codeing = utf-8
import os
import sys
import time
import Image
timeStart = time.clock()

'''
def listyoudir(level, path):  
    for i in os.listdir(path):  
        print '  '*(level+1) + i  
        if os.path.isdir(path + '\\' + i):  
            listyoudir(level+1, path + '\\' + i)  
          

rootpath = os.path.abspath('.')  
print rootpath  
listyoudir(0, rootpath) 
'''

'''
numFile = 0
def listdir(path):
	global numFile
	for filename in os.listdir(path):
		numFile +=1


'''

def fileCountIn(dir):
    return sum([len(files) for root,dirs,files in os.walk(dir)])

def compress(filename, ratio = 1.0):
	try:
		im = Image.open(filename)
	except Exception, e:
		print '%s can not open'% filename
		return 
	wide, hight = im.size
	wide *= ratio
	hight *= ratio
	out = im.resize((int(wide),int(hight)))
	try:
		out.save(filename)
	except Exception, e:
		print e
		return

def isImage(filename):
	if filename[-4:] == '.jpg' or filename[-5:] == '.jpeg' or filename[-4:] =='.bmp':
		return True;
	else:
		return False;

def log(logFile, logInfo):
	logFile.writelnes(logInfo)




def main():
	timeStart = time.clock()
	logFile = open('log.log', 'a')
	logFile.writelnes('\n')
	if 2 == len(sys.argv) or 1 == len(sys.argv):
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
		for root,dirs,files in os.walk(os.getcwd()):
			for filename in files:
				fullPathOfFile = root +'\\' + filename
				if isImage(fullPathOfFile):
					compress(fullPathOfFile,ratio)
					print fullPathOfFile
				numCompleted += 1
				per = float(100) * numCompleted / numFile 
				print 'complete files: %d / %d, %.2f%%' %(numCompleted, numFile, per)

	else:
		print error

	timeEnd = time.clock()
	print '[Finished in %.1fs]' %(timeEnd - timeStart)
	raw_input()

if __name__ == '__main__':
	main()

#rootPath = os.getcwd()

#print fileCountIn(rootPath)

#compress('a.jpg')