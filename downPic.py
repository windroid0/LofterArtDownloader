# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re

headers={'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'}
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
def downPic(picid,path):
    req=urllib2.Request('http://www.lofter.com/art/product-'+picid,headers=headers)
    try:
        content=opener.open(req)
    except BaseException,err:
        print 'download: '+picid+'.jpg failed. Error: '+str(err)
        return 1
    else:
        result=re.findall('<img src="(.*?)" class="showimgtag">',content.read())
    for item in result:
        urllib.urlretrieve(item,path+picid+'.jpg')
        print 'download: '+picid+'.jpg over.'
    return 0
