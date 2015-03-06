#-*- coding: utf-8 -*-
import urllib2
import gzip
import StringIO
import re
def getPage(page):
    '加载页面,返回list，数据格式：productId=23123720'
    BATCHID=196800-page*13
    #if page==1:
    #    page=0
    #    PARAM2=32
    #elif page<=50:
    #    PARAM2=16
    #else:
    #    PARAM2=8
    PARAM2=8

    postdata='''callCount=1
scriptSessionId=${scriptSessionId}187
httpSessionId=
c0-scriptName=SaleBean
c0-methodName=getSaleRecommendItemList
c0-id=0
c0-param0=number:1
c0-param1=number:-1
c0-param2=number:%d
c0-param3=number:%d
batchId=%d'''%(PARAM2, PARAM2*page, BATCHID)

    url='http://www.lofter.com/dwr/call/plaincall/SaleBean.getSaleRecommendItemList.dwr'

    myheaders={
        'Host':'www.lofter.com',
        'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Accept-Encoding':'gzip, deflate',
        'Content-Type':'text/plain; charset=UTF-8',
        'Referer':'http://www.lofter.com/art/print',
    }
    opener=urllib2.build_opener()
    req=urllib2.Request(url,data=postdata,headers=myheaders)
    f=opener.open(req)
    rawdata=StringIO.StringIO(f.read())
    resdata=gzip.GzipFile(fileobj=rawdata).read()
    reslist=re.findall('productId=\d*',resdata)
    #print reslist
    return reslist
#getPage(1)#184
