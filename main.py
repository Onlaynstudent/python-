"""Girilen sayının onlar ve yüzler basamağını değiştiren"""
sayi=int(input("Bir sayı giriniz: "))
yuzler=int((sayi%1000)/100)
onlar=int((sayi%100)/10)
sayi=sayi-(yuzler*100)-(onlar*10)
sayi=sayi+(yuzler*10)+(onlar*100)
print(sayi)
