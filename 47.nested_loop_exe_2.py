# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1 
count=0
num=1
line=1
for item in range(0,1):
    count+=1

    if count %2==0:
        print(0,end=' ')

    else:
        print(1,end=' ')

print()

while line<=2:
    count=1
    for item in range(0,line+1):
        
        count+=1
        if count %2==0:
            print(0,end=' ')

        else:
            print(1,end=' ')
    print()
    line+=1
    
while num>0 and num<3: 
    count=0
    for item in range(1,num+4):
        count+=1
        
        if count %2==0:
            print(0,end=' ')

        else:
            print(1,end=' ')

    print()
    num+=1