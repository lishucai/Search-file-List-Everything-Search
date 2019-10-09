# find voice of vocab in files
# python collectfiles.py

import binascii
import glob, os
import shutil
import subprocess
import time

################## Parameters
ListLocation="C:\\Users\\X\\Desktop\\EXtPython\\" 	 # direction of DATA_List
dst="C:\\Users\\X\\Desktop\\EXtPython\\out\\" 	 	 # direction of result
Sur='C:\\Users\\X\\Desktop\\EXtPython\\Ref\\'	 	 # direction of Main files
FILENAME_EXTENSION = ".mp3"							 # file format
DATA_List = 'list.txt'								 # List of desire files
NotFound_List = 'NotFound.txt'						 # Files that are not found
p1='Everything.exe'									 # Everything program


################# Just For Test########
# sa='making'
# p2='-create-file-list '+dst+'"explorer.efu" '+Sur+' -create-file-list-include-only-files "%s???%s;%s%s"' % (sa,FILENAME_EXTENSION,sa,FILENAME_EXTENSION)
# #p2='-create-file-list '+dst+'"explorer.efu" '+Sur+' -create-file-list-include-only-files "%s???.mp3;%s.mp3"' % (sa,sa)
# os.system(p1+" "+p2)
###########################################

os.chdir(ListLocation)#r"C:\Users\X"

fl = open(DATA_List, 'r')
fe = open(NotFound_List, 'w')
dl=fl.readline()
i=1

while dl.rstrip() != "" :
	ck=0
	print("word "+str(i)+" :"+dl.rstrip()+"\n")
	p2='-create-file-list '+ListLocation+'"explorer.efu" '+Sur+' -create-file-list-include-only-files "%s(?)%s;%s%s"' % (dl.rstrip(),FILENAME_EXTENSION,dl.rstrip(),FILENAME_EXTENSION)
	
	os.system(p1+" "+p2)
	fs = open('explorer.efu', 'r')
	d=fs.readline()
	while d != "":
		num=d.find(FILENAME_EXTENSION)#find position of char in string -1:if not find Else: position
		if (num != -1): 
			ck=1
			# print ("Contains given substring ", num)
			# print (d[1:(num+4)])
			try:
				shutil.copy2(d[1:(num+4)], dst)
				ck=1
			except:
				ck=1
		# else: 
			# print ("Doesn't contains given substring") 
		d=fs.readline()
	fs.close()
	# time.sleep(5)
	os.remove('explorer.efu')
	if ck==0:
		fe.writelines(dl)
		print("'"+dl.rstrip()+"' was not found X\n")
	i=i+1
	dl=fl.readline()
fe.close()	
fs.close()	
fl.close()	
print('end')
