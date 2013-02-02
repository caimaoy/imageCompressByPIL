#coding=utf-8
import os
import sys
import time
import Image

timeStart = time.clock()
'''
im = Image.open("1.jpg")
w,h = im.size
#out = im.resize((int(w*2),int(h*2)))
out = im.resize((int(w*0.5),int(h*0.5)))
out.save('1.jpg')

print "Done"
'''

currentDir = os.getcwd()
listfile = os.listdir(currentDir)
print currentDir
currentDirLast =  currentDir.split('\\')[-1]
newDir = currentDir + '\\' + currentDirLast + '\\'


if os.path.exists(newDir) == False:
	os.mkdir(newDir)
	#print "make"


#print 'sdf'[-10:]
numFile = len(listfile)
for index,filename in enumerate(listfile):
	if filename[-4:] == '.jpg' or filename[-5:] == '.jpeg' or filename[-4:] =='.bmp':
		im = Image.open(filename)
		wide, hight = im.size
		out = im.resize((int(wide),int(hight)))
		out.save(newDir + filename)

    #print '%.2f%%' % per
	#print 'complete' + 100 * num / numFile + '%'
	per = float(100) * index / numFile
	print 'complete files %d / %d, %.2f%%' %(index, numFile, per)


timeEnd = time.clock()
print '[Finished in %.1fs]' %(timeEnd - timeStart)
raw_input()

#print os.listdir(currentDir)