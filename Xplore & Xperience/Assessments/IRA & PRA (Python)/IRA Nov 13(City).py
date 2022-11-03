from collections import OrderedDict
class City():
    def __init__(self,city_id,state_name,city_name,no_of_tests,no_of_positive):
        self.city_id=city_id
        self.state_name=state_name
        self.city_name=city_name
        self.no_of_tests=no_of_tests
        self.no_of_positive=no_of_positive

class PandemicAnalysis():
    def __init__(self,analysis_name,city_list):
        self.analysis_name=analysis_name
        self.city_list=city_list

    def get_StateWithMaxPositiveCases(self):
        dictionary={}
        for i in self.city_list:
            dictionary[i.state_name]=0
        for city in self.city_list:
            dictionary[city.state_name]+=city.no_of_positive
        dict1=sorted(dictionary,key=lambda x:dictionary[x],reverse=True)
        return dict1[0]

    def get_citiesMoreThanPercentage(self,percentage):
        temp=[]
        for city in city_list:
            if (city.no_of_positive*100)/city.no_of_tests >= percentage:
                tup=(city.state_name,city.city_name)
                temp.append(tup)
        return temp

if __name__=='__main__':
    city_list=[]
    count=int(input())
    for c in range(count):
        city_id=int(input())
        state_name=input()
        city_name=input()
        no_of_tests=int(input())
        no_of_positive=int(input())
        City_obj=City(city_id,state_name,city_name,no_of_tests,no_of_positive)
        city_list.append(City_obj)
    percentage=int(input())
    Analysis_obj=PandemicAnalysis("ABC",city_list)
    max_city=Analysis_obj.get_StateWithMaxPositiveCases()
    percentage_list=Analysis_obj.get_citiesMoreThanPercentage(percentage)
    print(max_city)
    for city in percentage_list:
        print(city[0],city[1])
