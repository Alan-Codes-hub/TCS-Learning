function SumOfSeries(){
var a=0;
var b=1;
var sum=0;
var tmp;
while((a<100)&&(b<100)){
sum=sum+b;
tmp=a;
a=b;
b=b+tmp;
}
document.getElementById("result").innerText=sum;

}
