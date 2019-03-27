
import re
import sys
from decimal import *
from operator import itemgetter

def index2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

urls=[]
for line in sys.stdin:
    result=re.split(r' ',line)
    path=result[6]
    time_with_brackets=result[24]
    time=Decimal(re.sub('[\[\]\n]','',time_with_brackets))
    modified_path=re.sub('\d{1,}','%d',path)
    if any(modified_path in lines for lines in urls):
        nrow_url=index2d(urls, modified_path)[0]
        urls[nrow_url][1]+=time
        urls[nrow_url][2]+=1
        urls[nrow_url][3]=round(urls[nrow_url][1]/urls[nrow_url][2],3)
    else:    
        urls.append([modified_path, time,1,time])
        
sorted_urls=sorted(urls, key=itemgetter(3), reverse=True)
print ('URL','\t','SUM','\t','COUNT','\t','AVG')
for rows in sorted_urls:
    for cells in rows:    
        print (cells,'\t',end='')
    print ('')
