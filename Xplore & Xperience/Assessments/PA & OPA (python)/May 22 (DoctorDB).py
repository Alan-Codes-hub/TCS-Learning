class Doctor():
    def __init__(self,doctorId,doctorName,specialization,consutationFee):
        self.doctorId=doctorId
        self.doctorName=doctorName
        self.specialization=specialization
        self.consultationFee=consultationFee
        
class Hospital():
    def __init__(self,doctorDB):
        self.doctorDB=doctorDB
    
    def searchByDoctorName(self,doc_Name):
        temp=[]
        self.doc_Name=doc_Name
        for k in doctorDB:
            if doctorDB[k].doctorName==self.doc_Name:
                temp.append(doctorDB[k])
        return temp
    
    def calculateConsultationFeeBySpecialisation(self,doc_spec):
        fee=0
        self.doc_spec=doc_spec
        for key in doctorDB:
            if doctorDB[key].specialization==self.doc_spec:
                fee+=doctorDB[key].consultationFee
        return fee
        
if __name__=='__main__':
    doctorDB={}
    count=int(input())
    for c in range(count):
        doctorId=int(input())
        doctorName=input()
        specialization=input()
        consultationFee=int(input())
        obj=Doctor(doctorId,doctorName,specialization,consultationFee)
        doctorDB[c]=obj
        
    doc_Name=input()
    doc_spec=input()
    Hospital_obj=Hospital(doctorDB)
    doc_Name_list=Hospital_obj.searchByDoctorName(doc_Name)
    doc_cons_fee=Hospital_obj.calculateConsultationFeeBySpecialisation(doc_spec)
        
    if len(doc_Name_list)==0:
        print("No doctor found for the name")
    else:
        for f in doc_Name_list:
            print(f.doctorId)
            print(f.doctorName)
            print(f.specialization)
            print(f.consultationFee)
        
    if doc_cons_fee==0:
        print("No doctor with given spec")
    else:
        print(doc_cons_fee)
        