x=$1
y=$2
i=1
sum_x=0
while [$i -lt $x]
do
 if [$x % $i -eq 0]
  then
   sum_x=$sum_x + $i
   ((i++))
  fi
done
j=1
sum_y=0
while [$j -lt $y]
do
 if [$y % $j -eq 0]
 then
  sum_y=$sum_y + $j
  ((j++))
 fi
done

if [$sum_x -eq $y -a $sum_y -eq $x]
then
 echo "Amicable pair"
else
 echo "Not an Amicable pair"
fi
