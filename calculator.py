print("Hangi işlemi yapmak istiyorsunuz?")
print("Toplama için 1'e\nÇıkarma için 2'ye basınız.")  # Sonra?
print("Çarpma için 3'e\nBölme için 4'e basınız.")
cevap = input("İşlem yapmak istediğiniz sayıyı giriniz:")

a = int(input("1.sayı giriniz."))
b = int(input("2.sayı giriniz."))

if cevap == "1":  # bura niye yanlış oldı?
    print(a, "+", b, "=", (a + b))

elif cevap == "2":
    print(a, "-", b, "=", (a - b))

elif cevap == "3":
    print(a, "*", b, "=", (a * b))

elif cevap == "4":
    print(a, "/", b, "=", int(a / b))