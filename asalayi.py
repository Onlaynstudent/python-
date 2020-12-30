sayac=0
sayi=input('Sayı: ')
for x in range(2,int(sayi)):
      if(int(sayi)%x==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")