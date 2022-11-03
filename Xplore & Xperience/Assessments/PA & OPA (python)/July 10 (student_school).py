class Student():
    def __init__(self,st_name,sub1,sub2,sub3):
        self.st_name=st_name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def calcuateResult(self):
        if self.sub1>40 and self.sub2>40 and self.sub3>40:
            avg=(self.sub1+self.sub2+self.sub3)/3
        else:
            avg=0
        return avg

class School():
    def __init__(self,sc_name,studentDict):
        self.sc_name=sc_name
        self.studentDict=studentDict
    
    def getStudentResult(self):
        for i,j in self.studentDict.items():
            if i.calcuateResult()>60:
                self.studentDict[i]="pass"
            else:
                self.studentDict[i]="fail"
        
        return studentDict
        
    def findStudentWithHighestMarks(self):
        list=[]
        
        for i,j in self.studentDict.items():
            list.append(i.calcuateResult())
        maximum=max(list)
            
        for i,j in self.studentDict.items():
            if i.calcuateResult()>=maximum and studentDict[i]=="pass":
                return i
            else:
                return None

if __name__=='__main__':
    studentDict={}
    count=int(input())
    for k in range(count):
        st_name=input()
        sub1=int(input())
        sub2=int(input())
        sub3=int(input())
        st=Student(st_name,sub1,sub2,sub3)
        studentDict[st]="fail"
    
    sc_name=input()
    sc=School(sc_name,studentDict)
    dict=sc.getStudentResult()
    result=sc.findStudentWithHighestMarks()
    
    for i,j in dict.items():
        if dict[i]=="pass":
            print(i.st_name)
        
    
    if result==None:
        print("No student passed")
    else:
        print(result.st_name)
        
        
        
        