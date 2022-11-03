from collections import OrderedDict
class Qpaper():
    def __init__(self,QPaperId,QPaperType,nUsed,Complexity,dtUsed):
        self.QPaperId=QPaperId
        self.QPaperType=QPaperType
        self.nUsed=nUsed
        self.Complexity=Complexity
        self.dtUsed=dtUsed

class Qbank():
    def SelectQuestionPaper(Qpaper_list,Qtype,comp,date):
        lst=[]
        for paper in Qpaper_list:
            if paper.QPaperType.lower()==Qtype.lower():
                if paper.Complexity.lower()==comp.lower():
                    if (int(date[3:5])-int(paper.dtUsed[3:5]))*30+(int(date[0:2])-int(paper.dtUsed[0:2]))>=90:
                        paper.nUsed+=1
                        paper.dtUsed=date
                        lst=[paper.QPaperId,paper.QPaperType,paper.nUsed]
        return lst

    def countQpapers(self,Qpaper_list):
        temp=[]
        dict1={}
        dict2={}
        for paper in Qpaper_list:
            dict1[paper.QPaperType]=0
        for paper in Qpaper_list:
            dict2[paper.Complexity]=0
        for paper in Qpaper:
            dict1[paper.QPaperType]+=1
            dict2[paper.Complexity]+=1
        dict1_s=dict(sorted(dict1.items()))
        dict2_s=dict(sorted(dict2.items()))
        temp=[dict1_s,dict2_s]
        return temp

if __name__=='__main__':
    Qpaper_list=[]
    count=int(input())
    for c in range(count):
        QPaperId=int(input())
        QPaperType=input()
        nUsed=int(input())
        Complexity=input()
        dtUsed=input()
        Qpaper_obj=Qpaper(QPaperId,QPaperType,nUsed,Complexity,dtUsed)
        Qpaper_list.append(Qpaper_obj)

    Qtype=input()
    comp=input()
    date=input()
    Qbank_obj=Qbank()
    result_lst=Qbank_obj.SelectQuestionPaper(Qpaper_list,Qtype,comp,date)
    if len(result_lst)==0:
        print("No paper found")
    else:
        print(result_lst[0],result_lst[1],result_lst[2])
    output=Qbank_obj.countQpapers()
    for (k,v) in output[0].items():
        print(k.upper(),v)
    for (k,v) in output[1].items():
        print(k.upper(),v)
