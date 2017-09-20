# coding: utf-8
import os
import time
import datetime
from stat import *
topdir = '/data/backup/'
for dirpath, dirnames, files in os.walk(topdir):
    for folder in dirnames:
        pwdfolder= os.path.join(dirpath,folder)
        permission = oct(os.stat(pwdfolder)[ST_MODE])
        datemod = os.path.getmtime(pwdfolder) 
        print (datemod)
        print (pwdfolder + ", " + str(permission[-3:]) )    
        nd = pwdfolder + "," + str(permission[-3:] + ","+ str(datemod))
        with open("Output.txt", "a") as text_file:
           text_file.write(nd + '\n')
           text_file.close()


