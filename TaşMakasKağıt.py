import random
secim=input("Seçmek istediğinizi yazınız:\nTaş\nKağıt\nMakas:\n")
x=random.randint(0,3)
if x==0 and secim.lower()=="taş":
    print("Bilgisayarın Seçimi Taş")
    print("Berabere")
elif x==0 and secim.lower()=="kağıt":
    print("Bilgisayarın Seçimi Taş")
    print("Kaybettiniz")
elif x==0 and secim.lower()=="makas":
    print("Bilgisayarın Seçimi Taş")
    print("Kaybettiniz")
elif x==1 and secim.lower()=="taş":
    print("Bilgisayarın Seçimi Kağıt")
    print("Kazandınız")
elif x==1 and secim.lower()=="kağıt":
    print("Bilgisayarın Seçimi Kağıt")
    print("Beraber")
elif x==1 and secim.lower()=="makas":
    print("Bilgisayarın Seçimi Kağıt")
    print("Kaybettiniz")
elif x==2 and secim.lower()=="taş":
    print("Bilgisayarın Seçimi Makas")
    print("Kaybettiniz")
elif x==2 and secim.lower()=="kağıt":
    print("Bilgisayarın Seçimi Makas")
    print("Kazandınız")
elif x==2 and secim.lower()=="makas":
    print("Bilgisayarın Seçimi Makas")
    print("Berabere")
else:
    print("Doğru gir puşt")
