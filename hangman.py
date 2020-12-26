from random import choice

userName = input("Enter your Name and Surname:")
while True:
    print("    _    ____    _    __  __      _    ____  __  __    _    ____    _    ")
    print("   / \  |  _ \  / \  |  \/  |    / \  / ___||  \/  |  / \  / ___|  / \   ")
    print("  / _ \ | | | |/ _ \ | |\/| |   / _ \ \___ \| |\/| | / _ \| |     / _ \  ")
    print(" / ___ \| |_| / ___ \| |  | |  / ___ \ ___) | |  | |/ ___ \ |___ / ___ \ ")
    print("/_/   \_\____/_/   \_\_|  |_| /_/   \_\____/|_|  |_/_/   \_\____/_/   \_\ ")
    print("By Muhammet Ali ŞAHİN")

    sifir = (
        "                                      \n"
        "                 \ _ /                \n"
        "               -= (_) =-              \n"
        "                 /   \                \n"
        "  ,\//,.\//\/.           ,\/,   ,\/.//, \n"
        "  //o\ \/o//o\ \ ,.,.,   //o\   /o\ \o\\ \n"
        "    |    |  |  /###/#\     |     |  |   \n"
        "    |    |  |  |' '|:|     |`=.='|  |   \n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    bir = (
        "    ________\n"
        "   |/      |\n"
        "   |      \n"
        "   |      \n"
        "   |       \n"
        "   |       \n"
        "   |\n"
        "___|__________")
    iki = (
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |      \n"
        "   |      \n"
        "   |       \n"
        "   |\n"
        "___|__________")
    uc = (
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |       |\n"
        "   |       |\n"
        "   |       \n"
        "   |\n"
        "___|__________")
    dort = (
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |      \| \n"
        "   |       |\n"
        "   |       \n"
        "   |\n"
        "___|__________")
    bes = (
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |      \|/\n"
        "   |       |\n"
        "   |       \n"
        "   |\n"
        "___|__________")
    alti = (
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |      \|/\n"
        "   |       |\n"
        "   |      /  \n"
        "   |\n"
        "___|__________")
    yedi = (
        "RAHMETLİ DE BİLEMEZDİ\n"
        "    ________\n"
        "   |/      |\n"
        "   |      (_)\n"
        "   |      \|/\n"
        "   |       |\n"
        "   |      / \ \n"
        "   |\n"
        "___|__________\n"
        "OYUNU KAYBETTİN")

    kelime = choice(["ankara", "istanbul", "Malatya", "Kars"])

    kelime = kelime.upper()
    harfsayisi = len(kelime)
    girilenHarfler = ""

    print("\nKELİMEN {} HARFLİDİR.".format(harfsayisi))

    tahminler = []
    hata = []

    deneme = 7

    while deneme > 0:

        tabela = ""

        for harf in kelime:
            if harf in tahminler:
                tabela = tabela + harf

            else:
                tabela = tabela + " _ "

        if tabela == kelime:
            print('TEBRİKLER KAZANDIN {}!!!!'.format(userName))
            break

        print("KELİMEYİ TAHMİN EDİNİZ", tabela)
        print("ÖNCEKİ TAHMİNLER:"+girilenHarfler)
        print(deneme, "CANIN KALDI")
        if deneme == 1:
            print(alti)
        if deneme == 2:
            print(bes)
        if deneme == 3:
            print(dort)
        if deneme == 4:
            print(uc)
        if deneme == 5:
            print(iki)
        if deneme == 6:
            print(bir)
        if deneme == 7:
            print(sifir)

        Tahmin = input('BİR HARF SÖYLE {}!!!!'.format(userName))
        if len(Tahmin) == 1:
            girilenHarfler = girilenHarfler+", "+Tahmin
        Tahmin = Tahmin.upper()

        if Tahmin == kelime:
            print("\n"*50, "BRAVO DOĞRU BİLDİN\n\n")
            break

        if Tahmin in tahminler or Tahmin in hata:
            print("\n"*50, "{} DAHA ÖNCE SÖYLENDİ. BAŞKA BİR HARF SÖYLE".format(Tahmin))

        elif Tahmin in kelime:
            rpt = kelime.count(Tahmin)
            print(
                "\n"*50, "DOĞRU.{0} HARFİ KELİMENİZ İÇİNDE {1} KERE GEÇİYOR".format(Tahmin, rpt))
            tahminler.append(Tahmin)

        else:
            print("\n"*50,)
            print("YANLIŞ. KELİMEDE BÖYLE BİR HARF YOK")
            hata.append(Tahmin)
            if len(Tahmin) > 1:
                print("'{}' BİR HARF DEĞİLDİR!!!".format(Tahmin))
            elif Tahmin.isnumeric():
                print("'{}' BİR HARF DEĞİL!!!".format(Tahmin))
            else:
                deneme = deneme - 1

    if deneme == 0:
        print("\n"+yedi)
        print("KELİMEN {}\n".format(kelime))

    print('TEKRAR BAŞLAMAK İÇİN BİR DEĞER GİR {}!!!!'.format(userName))
    devam = input(">>>")
    devam = devam.upper()
