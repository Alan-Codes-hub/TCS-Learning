def Is_Leap(year):
    if year%100==0 and year%400==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

if __name__=="__main__":
    year=int(input())
    Is_Leap(year)