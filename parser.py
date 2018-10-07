import re
import sys
from decimal import *

def index2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

sumtime=0
#urls_and_time={}
#urls_and_count={}
urls=[]
for line in sys.stdin:
    result=re.split(r' ',line)
    path=result[6]
    time_with_brackets=result[24]
    time=Decimal(re.sub('[\[\]\n]','',time_with_brackets))
    modified_path=re.sub('\d{1,}','%d',path)
    urls.append([modified_path, time])
    if any(modified_path in lines for lines in urls):
        print ("Ok")
        print (index2d(urls, modified_path))
#    if modified_path in urls_and_time: 
#        urls_and_time[modified_path]+=time
#        urls_and_count[modified_path]+=1
#    else:
#        urls_and_time[modified_path]=time
#        urls_and_count[modified_path]=1
    #print (modified_path," ",time) 
print (urls)
#print (urls.index(modified_path))
#print (urls_and_count)
    