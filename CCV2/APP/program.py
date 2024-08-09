import sys

arr = sys.argv[1].split(" ")

content = ""
count = 0
for i in arr:
    if count == len(arr)-1:
        content = content + i    
    else:
        content = content + i + " "
    count += 1
    
print(content)