class Flat():
    def __init__(self,flatNo,OwnerName,status,noOfOccupant):
        self.flatNo=flatNo
        self.OwnerName=OwnerName
        self.status=status
        self.noOfOccupant=noOfOccupant

class Apartment():
    def __init__(self,apartmentName,flatList):
        self.apartmentName=apartmentName
        self.flatList=flatList

    def findStatuswiseTotalNoOfPeople(self):
        dictionary={}
        for flat in self.flatList:
            dictionary[flat.status]=0
        for flat in self.flatList:
            dictionary[flat.status]+=flat.noOfOccupant
        return dictionary

    def findFlatByFlatNo(self,flatNo_in):
        for flat in self.flatList:
            if flat.flatNo==flatNo_in:
                return flat

if __name__=='__main__':
    flatList=[]
    count=int(input())
    for c in range(count):
        flatNo=int(input())
        OwnerName=input()
        status=input()
        noOfOccupant=int(input())
        flat_obj=Flat(flatNo,OwnerName,status,noOfOccupant)
        flatList.append(flat_obj)

    flatNo_in=int(input())
    apartment_obj=Apartment("ASSET",flatList)
    dictionary_out=apartment_obj.findStatuswiseTotalNoOfPeople()
    result_obj=apartment_obj.findFlatByFlatNo(flatNo_in)
    for k in sorted(dictionary_out.keys()):
        print(str(k)+"#"+str(dictionary_out[k]))
    if result_obj==None:
        print("No Flat Found")
    else:
        print(str(result_obj.OwnerName)+"#"+str(result_obj.noOfOccupant))
