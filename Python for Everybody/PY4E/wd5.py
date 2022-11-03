import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

a=0
while True:
    address = input('Enter location: ')
    sum=0
    if len(address) < 1:
        address='http://py4e-data.dr-chuck.net/comments_42.xml'
    elif address=='done':
        break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print('\n\n')
    #print(data.decode())
    tree = ET.fromstring(data)

    #results = tree.findall('commentinfo/comments/comment')
    counts = tree.findall('.//count')
    #print(counts)
    print(len(counts))
    for x in counts:
        print(x.text)
        sum=sum+int(x.text)
    print(sum)
