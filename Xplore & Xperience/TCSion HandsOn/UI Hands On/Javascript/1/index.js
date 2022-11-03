/* exported callMe */
function callMe() {
var Passenger=new Object();
Passenger.name="Arun";
Passenger.age=28;
Passenger.reservedStatus='true';
document.write('<div id="name">'+Passenger.name+'</div>');
document.write('<div id="age">'+Passenger.age+'</div>');
document.write('<div id="reservedStatus">'+Passenger.reservedStatus+'</div>');
}
