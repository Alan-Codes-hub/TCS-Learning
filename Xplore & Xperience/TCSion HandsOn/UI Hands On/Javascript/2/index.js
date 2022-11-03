let carDetails = [{carName:"Innova" ,onRoadPrice:900000,yearOfModel:2016},{carName:"Dzire" ,onRoadPrice:700000, yearOfModel:2017},{carName:"i20" ,onRoadPrice:500000, yearOfModel:2013},{carName:"i10" ,onRoadPrice:400000, yearOfModel:2016}];
function displayCarDetails(){
var x = document.getElementById("SelectCar").value;
if(x=="Innova"){
document.getElementById("CarDetail").innerHTML= carDetails[0].carName+"-"+carDetails[0].onRoadPrice+"-"+carDetails[0].yearOfModel;}
else if(x=="Dzire"){
document.getElementById("CarDetail").innerHTML=carDetails[1].carName+"-"+carDetails[1].onRoadPrice+"-"+carDetails[1].yearOfModel;}
else if(x=="i20"){
document.getElementById("CarDetail").innerHTML=carDetails[2].carName+"-"+carDetails[2].onRoadPrice+"-"+carDetails[2].yearOfModel;}
else{
document.getElementById("CarDetail").innerHTML =carDetails[3].carName+"-"+carDetails[3].onRoadPrice+"-"+carDetails[3].yearOfModel;}
}
