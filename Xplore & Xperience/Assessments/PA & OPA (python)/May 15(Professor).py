class Professor:
    def __init__(self,profId,profName,subjectsDict):
        self.profId=profId
        self.profName=profName
        self.subjectsDict=subjectsDict
class University:
    def getTotalExperience(proflist,reqProfId):
        total=0
        for i in proflist:
            if i.profId==reqProfId:
                total=sum(i.subjectsDict.values())
                return total
    def selectSeniorProfessorBySubject(proflist,reqSubjectName):
        HighExpProf=None
        max=0
        for i in proflist:
            for j in i.subjectsDict.keys():
                if reqSubjectName.lower()==j.lower():
                    if i.subjectsDict[j]>max:
                        max=i.subjectsDict[j]
                        HighExpProf=i
        return HighExpProf
if __name__=="__main__":
    proflist=[]
    count=int(input())
    for i in range(count):
        profId=int(input())
        profName=input()
        dictcount=int(input())
        subjectsDict={}
        for i in range(dictcount):
            key=input()
            value=int(input())
            subjectsDict[key]=value
        profObj=Professor(profId,profName,subjectsDict)
        proflist.append(profObj)
    reqProfId=int(input())
    print(University.getTotalExperience(proflist,reqProfId))
    reqSubjectName=input()
    HighExpProf=University.selectSeniorProfessorBySubject(proflist,reqSubjectName)
    if HighExpProf!=None:
            print(str(HighExpProf.profId)+" "+ HighExpProf.profName+" "+str(HighExpProf.subjectsDict))
    else:
        print("None")
