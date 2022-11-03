
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
xxx=None
url = input('Enter - ')
if len(url)<1 :
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
red=1
while red<8 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    red=red+1
    print('red value',red)
    print(url)
    # Retrieve all of the anchor tags
    i=0
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        i=i+1
        #print(i)
        if i==18 :
            url=tag.get('href', None)
            #print('url changed')
            #print(url)
            xxx=tag.get('href', None)
        else: continue

print(xxx)
y=re.findall('http://py4e-data.dr-chuck.net/known_by_(.+).htm',xxx)
print(y)
