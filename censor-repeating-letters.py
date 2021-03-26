girdi=input('')

for i in range(2,len(girdi)):
    if girdi[0]==girdi[i]:
        sonuc=girdi[0]+girdi[1:].replace(girdi[0],'*')
        i=len(girdi)

print(sonuc)
        
    