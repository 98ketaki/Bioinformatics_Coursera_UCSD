num=8943
k=10
i=0
a=[]
while i<k:
    q=num/4
    r=num%4
    r1=int(r)
    num=q
    a.append(r1)
    i=i+1
print(a)
b=[]
for x in a:
    if x==0:
        b.append("A")
    elif x==1:
        b.append("C")
    elif x==2:
        b.append("G")
    else:
        b.append("T")
b.reverse()
print((b))
    
        
    
