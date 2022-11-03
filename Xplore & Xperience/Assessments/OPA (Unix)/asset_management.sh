grep -i "sw" | awk '
BEGIN{FS=";"}{print $1}' | awk '
BEGIN{FS="_"}{if ($4>3){print $0;count++}}
END{if(count == 0){print "No orders found"}}'

#OR
#grep -i "sw" | awk '
#BEGIN{FS=";"}{print $1}' | awk '
#BEGIN{FS="_"}{for(i=1;i<+NR;i++){if ($NF>3){a[$0]=i;count++}}}
#END{if(count == 0){print "No orders found"} else {for (j in a){print j}}}'
