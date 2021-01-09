##frequenr k-mer given the sequence and value of k
s="CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
k=3
a={}
for i in range(len(s)-k+1):
    kmer=s[i:i+k]
    if kmer in a:
        a[kmer]+=1
    else:
        a[kmer]=1
        
all_values=a.values()
max_value=max(all_values)
print(max_value)

all_items=a.items()
print(all_items)

def get_key(val): 
    for key, value in a.items(): 
         if value == val: 
             return key 
         
print(get_key(max_value))