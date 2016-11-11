
#!/bin/bash
#Expects a test file - for development you can use Test1.txt

file=$1
cut -d , -f 2,5 $file | while read
do
  d=$(echo $REPLY | cut -d , -f 1)
  words=$(echo $REPLY | cut -d , -f 2)
  for w in $words
  do
    curl http://localhost:5000/todo1 -d "word=$w&doc=$d" -X PUT 
  done
done
