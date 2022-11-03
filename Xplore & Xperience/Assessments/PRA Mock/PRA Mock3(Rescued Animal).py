class RescuedAnimal():
    def __init__(self,animalID,category,breed,healthStatus):
        self.animalID=animalID
        self.category=category
        self.breed=breed
        self.healthStatus=healthStatus

class AnimalAdoptionCentre():
    def __init__(self,centerID,RescuedAnimal_list):
        self.centerID=centerID
        self.RescuedAnimal_list=RescuedAnimal_list

    def CountAnimalsPerCategory(self):
        dictionary={}
        for animal in self.RescuedAnimal_list:
            dictionary[animal.category]=0
        for animal in self.RescuedAnimal_list:
            dictionary[animal.category]+=1
        return dictionary

    def isAnimalForAdoption(self,animalID_in):
        value=0
        status={"healthy":1,"unhealthy":2,"traumatized":3,"critical":4}
        for animal in self.RescuedAnimal_list:
            if animal.animalID==animalID_in:
                value=return status[animal.healthStatus.lower()]
        return value

if __name__=='__main__':
    RescuedAnimal_list=[]
    count=int(input())
    for c in range(count):
        animalID=int(input())
        category=input()
        breed=input()
        healthStatus=input()
        Animal_obj=RescuedAnimal(animalID,category,breed,healthStatus)
        RescuedAnimal_list.append(Animal_obj)
    animalID_in=int(input())
    Adoption_obj=AnimalAdoptionCentre(34,RescuedAnimal_list)
    dictionary=Adoption_obj.CountAnimalsPerCategory()
    for k,v in dictionary.items():
        print(k,v)
    value=Adoption_obj.isAnimalForAdoption(animalID_in)
    if value==1:
        print(animalID_in,": Available for Adoption")
    elif value==2:
        print(animalID_in,": Undergoing Treatment")
    elif value==3:
        print(animalID_in,": Undergoing Trauma Care")
    elif value==4:
        print(animalID_in,": Unavailable for Adoption")
    else:
        print("No animal found")
