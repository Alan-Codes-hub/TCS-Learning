from itertools import permutations

def All_Possible_Combination(string):
    arr=[]
    arr[:0]=string
    lst=permutations(arr,3)
    return lst

if __name__=='__main__':
    string=input()
    lst=All_Possible_Combination(string)
    for i in lst:
        for j in i:
            print(j,end="")
        print()