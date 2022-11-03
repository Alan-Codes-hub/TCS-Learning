class Booking():
    def __init__(self,bookingID,tableNO,BookingDate,Guests,Status):
        self.bookingID=bookingID
        self.tableNO=tableNO
        self.BookingDate=BookingDate
        self.Guests=Guests
        self.Status=Status
    
class Restaurant():
    def __init__(self,tableList,bookingList):
        self.tableList=tableList
        self.bookingList=bookingList
        
    def bookTable(self,Guests_in,date_in,request):
        lst=[]
        for k in self.tableList:
            if self.tableList[k]==Guests_in:
                for i in self.bookingList:
                    lst.append(i.bookingID)
                    if i.BookingDate!=date_in and i.tableNO!=k:
                        self.bookingList.append(Booking(max(lst)+1,k,date_in,Guests_in,request.capitalize()+"ed")))
                        
    def updateBookingStatus(self,date_in):
        for j in self.bookingList:
            if int(j.BookingDate[0:2])-2==int(date_in[0:2]) and j.Status=="Reserved":
                j.Status="Cancelled"
            elif int(j.BookingDate[0:2])-1==int(date_in[0:2]) and j.Status=="Booked":
                j.status="Closed"
                
if __name__=='__main__':
    tableList={}
    bookingList=[]
    count=int(input())
    for c in range(count):
        key=int(input())
        value=int(input())
        tableList[key]=value
    count2=int(input())
    BookingDate=input()
    for g in range(count2):
        bookingID=g
        tableNO=int(input())
        Guests=int(input())
        Status=input()
        obj=Booking(bookingID,tableNO,BookingDate,Guests,Status)
        bookingList.append(obj)
    date_in=input()
    Guests_in=int(input())
    request=input()
                        
        