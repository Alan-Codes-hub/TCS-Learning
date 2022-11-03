#                             Online Bash Shell.
#                 Code, Compile, Run and Debug Bash script online.
# Write your code in this editor and press "Run" button to execute it.


awk '
BEGIN{FS="|";OFS="$"}
{
    $(NF+1)=$6-$5;print $0
}'| sort -nk7 -t "$" | tail -3
