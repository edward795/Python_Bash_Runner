i=1
sum=0

while [ $i -le 100 ]
do
  num=$i          #get number
  sum=$((sum + num)) #sum+=num
  i=$((i + 1))
done

echo "sum of numbers:$sum"