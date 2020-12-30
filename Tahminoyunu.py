from random import randint
rand = randint(0, 101)
sayac = 0
while True:
    sayac += 1
    sayi = int(input("Bir Değer giriniz 0 Girerseniz oyun biter:"))
    if sayi == 0:
        print("oyunu bitirdiniz.")
        break
    elif sayi < rand:
        print("Daha büyük bir sayı giriniz.")
        continue
    elif sayi > rand:
        print("Daha Küçük bir sayı giriniz.")
    elif sayac == 10:
        print("Efendim biraz daha düşünün...")

    else:
        print("Rastgele seçileen sayı {}".format(rand))
        print("{} kere denediniz".format(sayac))
