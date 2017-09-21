# coding: utf-8
import os
import time
import datetime
from stat import *
import ftplib

def ftpupload(ip, user, passwd, fileup):
    session = ftplib.FTP(ip,user,passwd)
    file = open(fileup,'rb')                  # file to send
    session.storbinary('STOR ' + fileup,file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
def main():
    topdir = '/data/backup/'
    for dirpath, dirnames, files in os.walk(topdir):
        for folder in dirnames:
            pwdfolder= os.path.join(dirpath,folder)
            permission = oct(os.stat(pwdfolder)[ST_MODE])
            datemod = os.path.getmtime(pwdfolder)
            nd = pwdfolder + "," + dirpath + "," + str(permission[-3:] + ","+ str(datemod))
            with open(filename, "a") as text_file:
               text_file.write(nd + '\n')
               text_file.close()
if __name__ == "__main__":
    today = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
    filename = today + "_output.log"
    ftpip = "1.55.145.28"
    ftpuser = "fptlms"
    ftppass = "lsm123$%^"
    main()
    ftpupload(ftpip,ftpuser,ftppass,filename)
