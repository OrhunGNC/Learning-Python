print("Secenekler")
print("1.Toplama")
print("2.Cikarma")
print("3.Bolme")
print("4.Carpma")
c=input("Islem:")

if c=="Toplama":
    a=float(input("Birinci Sayi:"))
    b=float(input("Ikinci Sayi:"))
    z=str(a+b)
    print(z)
elif c=="Cikarma":
    a=float(input("Birinci Sayi:"))
    b=float(input("Ikinci Sayi:"))
    z=str(a-b)
    print(z)
elif c=="Bolme":
    a=float(input("Birinci Sayi:"))
    b=float(input("Ikinci Sayi:"))
    z=str(a/b)
    print(z)
elif c=="Carpma":
    a=float(input("Birinci Sayi:"))
    b=float(input("Ikinci Sayi:"))
    z=str(a*b)
    print(z)
else:
    print("Gecersiz Islem!")

