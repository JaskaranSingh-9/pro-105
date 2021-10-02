import math 
data=[60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+x

    mean=total/n
    return mean

square_list=[]
for number in data:
    f=number-mean(data)
    f=f**2
    square_list.append(f)

sum=0
for i in square_list:
    sum += i

result=sum/(len(data)-1)

deviation=math.sqrt(result)
print(deviation)