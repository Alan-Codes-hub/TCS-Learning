# Hands On 1

grep -i -o "Unix"|wc -l


# Hands on 2

head -n3|wc -w


# Hands On 3
read c
sum=0
i=1
while [ $i -le $c ]
do
read num
if [ $((num%2)) -eq 0 ]
then
sum=$((sum+num))
fi
i=$((i+1))
done
echo "Total = "$sum



 or



read c
awk '
    BEGIN {
        sum=0;
        }
     { if ( $0%2==0 ){
         sum+=$0;
     }
     }
     END { print "Total =",sum}'


# Hands On 4


awk'BEGIN
{max=0;}
{if(($3)>max && $3 !="Score")
{max=$3;
output=$2;}}END
{print output}'

or

sort -k3,3rn -t " "|head -n1|awk'{print $2}'


#  Hands On 5

read c
lim=10
max=0
salary=0
n=0
for i in $(seq $lim)
do
read line
num=$(echo "$line"|cut -d ";" -f3)
if [ $num > 0 ];
then
salary=$((salary+num))
arr[n]=$num
n=$((n+1))
fi
done;
avg=$((salary/n))
count=0
for val in ${arr[@]}
do
if [ $val -lt $avg ];
then
count=$((count+1))
fi
done;
echo "$count"
unix handson (1).txt
Displaying unix handson (1).txt.
