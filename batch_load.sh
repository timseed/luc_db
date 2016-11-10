
#!/bin/bash
#Expects a test file - for development you can use Test1.txt


file=$1
for a in $(cut -d , -f 5 $file | tr -s '[[:punct:][:space:]]' '\n' )
do
  curl -S http://localhost:5000/todo1 -d "word=$a&doc=$file" -X PUT 
done
