import modulVolumebr

def main():
    r = 28
    t = 14

    vTabung = modulVolumebr.volumeTabung(r,t)
    print ("Rumus Volume Tabung")
    print ("Jari-jari : ", r)
    print ("Tinggi :", t)
    print ("Hasil = ", vTabung)

    r = 3

    vBola = modulVolumebr.volumeBola(r)
    print ("\nRumus Volume Bola")
    print ("Jari-jari : ", r)
    print ("Hasil = ", vBola)

    p = 2
    l = 6
    t = 10

    vPrismaSegitiga = modulVolumebr.volumePrismaSegitiga(p,l,t)
    print ("\nRumus Volume Prisma Segitiga")
    print ("Panjang : ", p)
    print ("Lebar : ", l)
    print ("Tinggi : ", t)
    print ("Hasil : ", vPrismaSegitiga)

if __name__ == "__main__":
    main()
