class Player():
    def __init__(self,PlayerName,PlayerCountry,PlayerAge,Matches,Runs,Wickets):
        self.PlayerName=PlayerName
        self.PlayerCountry=PlayerCountry
        self.PlayerAge=PlayerAge
        self.Matches=Matches
        self.Runs=Runs
        self.Wickets=Wickets

class Team():
    def getMinRuns(self,lst):
        lst.sort(key=lambda x:x.Runs)
        return lst[0]
       
    
    def getMaxWickets(self,lst):
        lst.sort(key=lambda x:x.Wickets,reverse=True)
        return lst[0]
        
if __name__=='__main__':
    lst=[]
    count=int(input())
    for k in range(count):
        PlayerName=input()
        PlayerCountry=input()
        PlayerAge=int(input())
        Matches=int(input())
        Runs=int(input())
        Wickets=int(input())
        player_obj=Player(PlayerName,PlayerCountry,PlayerAge,Matches,Runs,Wickets)
        lst.append(player_obj)
    
    res_obj=Team()
    res1=res_obj.getMinRuns(lst)
    res2=res_obj.getMaxWickets(lst)
    print(res1.PlayerName)
    print(res1.Runs)
    print(res1.PlayerCountry)
    print()
    print(res2.PlayerName)
    print(res2.Wickets)
    print(res2.PlayerCountry)
    
    
    
    
    
    
    
    
    
    
    
            
            