text='aabbcdde'
data=len(text)
for i in range(data):
    for j in range(i+1,data):
        if text[i]==text[j]:
            break
    else:
        print(text[i])
