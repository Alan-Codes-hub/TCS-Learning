from collections import OrderedDict 
class Donor():
    def __init__(self,Donor_Id,Donor_Name,Contact,Blood_Group,PrevDonMonth,AwayFrom):
        self.Donor_Id=Donor_Id
        self.Donor_Name=Donor_Name
        self.Contact=Contact
        self.Blood_Group=Blood_Group
        self.PrevDonMonth=PrevDonMonth
        self.AwayFrom=AwayFrom
        
class BloodBank():
    def __init__(self,Bank_Name,Donor_List):
        self.Bank_Name=Bank_Name
        self.Donor_List=Donor_List
        
    def getListofAvailableDonors(self):
        dictionary={}
        for j in Donor_List:
            dictionary[j.Blood_Group]=0
        for Donor in self.Donor_List:
            if 11-MonthDict[Donor.PrevDonMonth]>=4:
                if Donor.AwayFrom<=50:
                    dictionary[Donor.Blood_Group]+=1
        return OrderedDict(sorted(dictionary.items()))
        
    def getAndUpdateDonor(self,Req_Group,Req_Count):

        if Req_Count>dictionary[Req_Group]:
            for Donor in self.Donor_List:
                if Donor.Blood_Group==Req_Group:
                    Donor.PrevDonMonth="Dec"
            val=False
        elif Req_Count<=dictionary[Req_Group]:
            count=0
            val=True
            for Donor in self.Donor_List:
                if Donor.Blood_Group==Req_Group and count<Req_Count:
                    Donor.PrevDonMonth="Dec"
                    count+=1
                
        return val           
            
        
if __name__=='__main__':
    MonthDict={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    Donor_List=[]
    count=int(input())
    for c in range(count):
        Donor_Id=int(input())
        Donor_Name=input()
        Contact=int(input())
        Blood_Group=input()
        PrevDonMonth=input()
        AwayFrom=int(input())
        Donor_obj=Donor(Donor_Id,Donor_Name,Contact,Blood_Group,PrevDonMonth,AwayFrom)
        Donor_List.append(Donor_obj)
    Bank_obj=BloodBank("ABC",Donor_List)
    Req_Group=input()
    Req_Count=int(input())
    dictionary=Bank_obj.getListofAvailableDonors()
    for k,v in dictionary.items():
        print(k,"-",v)
    val=Bank_obj.getAndUpdateDonor(Req_Group,Req_Count)
    if val==True:
        print("Donor Count Available")
    else:
        print("Donor count not Available")
    dictionary2=Bank_obj.getListofAvailableDonors()
    for k,v in dictionary2.items():
        print(k,"-",v)
    
    
        
        