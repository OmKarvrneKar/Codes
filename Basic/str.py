text='aabbcdde'
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]==1:
        print(i)
        break

