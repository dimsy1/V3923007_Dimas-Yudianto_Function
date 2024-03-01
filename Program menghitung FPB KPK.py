def fpb(x,y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x

def kpk(x,y):
    return x * y // fpb(x,y)

while True:
    print("1. KPK \n"
         "2. FPB")

    pilih = input("Pilih (1/2): ")


    if pilih == "1":
        bilangan1= int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))

        print("")

        print(f"KPK dari {bilangan1} dan {bilangan2} adalah " + str(kpk(bilangan1, bilangan2)))
        break

    elif pilih == "2":
        bilangan1= int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))

        print("")

        print(f"FPB dari {bilangan1} dan {bilangan2} adalah " + str(fpb(bilangan1, bilangan2)))
        break

    else:
        print("Mohon masukkan sesuai pilihan (1/2)")
        print("")
        continue
