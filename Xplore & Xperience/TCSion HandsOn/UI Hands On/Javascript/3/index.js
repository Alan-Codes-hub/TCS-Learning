function getAge() {
var age=document.getElementById("dob").value;
var l=age.toString();
var kk= l.substring(0,4);
var year=parseInt(kk);
var d= new Date();
var n=d.getFullYear();
var k=n.toString();
var m=parseInt(k);
if(year>=m){
document.getElementById("showresults").innerText="Wrong date!!";
}
else{
document.getElementById("showresults").innerText="You are "+(m-year)+" year(s) old!!";
}
}
