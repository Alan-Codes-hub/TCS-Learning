class Book:
    def __init__(self,bookId,bookName,bookTechnology,bookPrice,authorname):
        self.bookId=bookId
        self.bookName=bookName
        self.bookTechnology=bookTechnology
        self.bookPrice=bookPrice
        self.authorname=authorname

class BookStore:
    def __init__(self,bookdb,bookStoreName):
        self.bookdb=bookdb
        self.bookStoreName=bookStoreName
    
    def searchByName(self,bookName):
        list=[]
        for value in self.bookdb.values():
            if value.bookName==bookName:
                list.append(value)
        return list
    
    def calculatePriceByTechnology(self,Technology):
        sum=0
        for value in self.bookdb.values():
            if value.bookTechnology==Technology:
                sum+=value.bookPrice
        sum1=sum*0.9
        return sum1
count=int(input())
bookdb={}
for i in range(count):
    bookId=int(input())
    bookName=input()
    bookTechnology=input()
    bookPrice=int(input())
    authorname=input()
    obj=Book(bookId,bookName,bookTechnology,bookPrice,authorname)
    bookdb[i]=obj
BS=BookStore(bookdb,'Janakiram store')
bookName=input()
Technology=input()
lst=BS.searchByName(bookName)
result=BS.calculatePriceByTechnology(Technology)
if len(lst)==0:
    print("No Book Exists with the BookName")
else:
    for i in lst:
        print(i.bookId)
        print(i.bookName)
        print(i.bookTechnology)
        print(i.bookPrice)
        print(i.authorname)
if result==0:
    print("0.0")
else:
    print(result) 