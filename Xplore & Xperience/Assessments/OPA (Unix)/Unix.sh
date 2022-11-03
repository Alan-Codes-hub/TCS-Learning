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
Displaying unix handson (1).txt.S
