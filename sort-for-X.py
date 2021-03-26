girdiList=[]
xList=[]
otherList=[]
i=0
while i!=100:
    girdi=input('')
    if girdi!="":
        girdiList.append(girdi)
    else:
        i=100

for i in range(0,len(girdiList)):
    if girdiList[i][0]=='x': # x ile başlıyorsa
        xList.append(girdiList[i]) #sona ekle
    else:
        otherList.append(girdiList[i]) #sona ekle
    
birlestir=sorted(xList)+sorted(otherList)
for i in range(0,len(birlestir)):
    print(birlestir[i])
    