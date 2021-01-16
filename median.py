import csv 
with open("HeightWeight.csv",newline="" ) as f :
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
newdata=[]
for i in range(len(data)):
    num= data[i][1]
    newdata.append(float(num))
n=len(newdata)
#print(n)
newdata.sort()
if n%2==0 :
    median1= float(newdata[n//2])
    median2= float(newdata[n//2 -1])
    median=(median1+median2)/2
else :
    median= float(newdata[n//2])
print(median)    
