class ParkedVehicle():
    def __init__(self,vehicleSeq,fourWheeler,parkedFor,valetParking,parkedStatus):
        self.vehicleSeq=vehicleSeq
        self.fourWheeler=fourWheeler
        self.parkedFor=parkedFor
        self.valetParking=valetParking
        self.parkedStatus=parkedStatus

class ParkingLot():
    def __init__(self,parkd_vehicles):
        self.parkd_vehicles=parkd_vehicles
    
    def updateParkedStatus(self,lot_number_in):
        self.lot_number_in=lot_number_in
        temp=[]
        for k in self.parkd_vehicles:
            if k==self.lot_number_in:
                parkd_vehicles[k].parkedStatus="Cleared"
                temp.append(k)
                temp.append(parkd_vehicles[k].parkedStatus)
        return tuple(temp)
        
    def getParkingCharges(self,lot_number_in):
        charge=0
        for key in self.parkd_vehicles:
            if key==self.lot_number_in:
                if parkd_vehicles[key].fourWheeler=="Yes" and parkd_vehicles[key].valetParking=="Yes":
                    charge=parkd_vehicles[key].parkedFor*50 + 10
                elif parkd_vehicles[key].fourWheeler=="No" and parkd_vehicles[key].valetParking=="No":
                    charge=parkd_vehicles[key].parkedFor*30
                
        return charge
        
if __name__=='__main__':
    parkd_vehicles={}
    count=int(input())
    for c in range(count):
        vehicleSeq=int(input())
        fourWheeler=input()
        parkedFor=float(input())
        valetParking=input()
        lot_number=int(input())
        
        obj=ParkedVehicle(vehicleSeq,fourWheeler,parkedFor,valetParking,"Parked")
        parkd_vehicles[lot_number]=obj
    lot_number_in=int(input())    
    ParkingLot_obj=ParkingLot(parkd_vehicles)
    tup_res=ParkingLot_obj.updateParkedStatus(lot_number_in)
    parking_charge=ParkingLot_obj.getParkingCharges(lot_number_in)
    
    if len(tup_res)==0:
        print("Lot Number Invalid")
    else:
        print(tup_res[0],tup_res[1])
    
    if parking_charge==0:
        print("Lot Number Invalid")
    else:
        print(parking_charge)
        
        
            
        