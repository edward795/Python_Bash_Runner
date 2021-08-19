i=1
echo "sum of 1 to 100 numbers"
while [ $i -le $1 ]
do
    echo $i
    i=$(($i+1))
done