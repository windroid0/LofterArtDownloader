#-*- coding:utf-8 -*-
#lofterartdownloader
#author:windroid
#15/3/5
import getPage
import downPic
import re
import time

MAXPAGE=184
SPAGE=46
PATH='D:\\lofter\\'
print PATH
print SPAGE
print 'downloading...'
for downpage in range(SPAGE,MAXPAGE+1): 
    pagelist=getPage.getPage(downpage)
    for v in pagelist:
        #time.sleep(1)#404
        downPic.downPic(v[10:],PATH)
        #print v[10:]
    open('set.ini','w').write(str(downpage))
print 'download is over.'
