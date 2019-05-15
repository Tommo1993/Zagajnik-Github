
def Alkohole():
    Alkohol1=[0,0,0,0,"","",0] # indeks 0- trwałość, indeks 1- poziom % (od 1 do 10), indeks 2- mnożnik uzależnienia (od 1 do 10), indeks 3- narazie nic, indeks 4- Nazwa, indeks 5- Opis, 6- aktywność.
    Denaturat=[9,1,1,"Denaturat","Nemezis twojej wątroby i układu nerwowego.",0]
    DaneWszystkichAlkoholi.append(Denaturat)  
    
    
    
def SprawdzanieAlkoholi():
    CzyWypite() = 0
    StopienOdurzenia = DaneWszystkichAlkoholi[][1]/player.str
    StopienUzależnienia = DaneWszystkichAlkoholi[][2]/player.luck*10
    while DaneWszystkichAlkoholi[0][6] == 1 or DaneWszystkichAlkoholi[1][6] == 1 or DaneWszystkichAlkoholi[2][6] == 1:
        StopienOdurzenia = DaneWszystkichAlkoholi[0][1]/player.str or DaneWszystkichAlkoholi[1][1]/player.str or DaneWszystkichAlkoholi[2][1]/player.str
        StopienUzależnienia = DaneWszystkichAlkoholi[0][2]/player.luck*10 or DaneWszystkichAlkoholi[1][2]/player.luck*10 or DaneWszystkichAlkoholi[2][2]/player.luck*10
        if StopienOdurzenia =< 1:
            print('To było za dużo jak na takiego suchoklatesa jak ty, kmiotku.')
            player.HP = player.HP-10
            player.str = player.str-7
            player.end = player.end-8
            player.dex = player.dex-9
            player.luck = player.luck + 777
        if StopienOdurzenia > 1:
            print('Zapadasz w błogi stan, który tylko podchmielony może docenić!')
            player.HP = player.HP+2
            player.str = player.str+2
            player.end = player.end+2
            player.dex = player.dex+2
    if StopienUzależnienia =< 1000:
        print('Brawo, zostałeś alkoholikiem!')
        if DaneWszystkichAlkoholi[0][6] != 1 or DaneWszystkichAlkoholi[1][6] != 1 or DaneWszystkichAlkoholi[2][6] != 1:
            player.MaxHPnocalc = player.MaxHPnocalc-5
            player.MaxMPnocalc = player.MaxMPnocalc-5
            player.int = player.int-10
            player.str = player.str-2
            player.dex = player.dex-2
            player.end = player.end-2
        if DaneWszystkichAlkoholi[0][6] == 1 or DaneWszystkichAlkoholi[1][6] == 1 or DaneWszystkichAlkoholi[2][6] == 1:
            player.MaxHPnocalc = player.MaxHPnocalc-1
            player.MaxMPnocalc = player.MaxMPnocalc-1
            player.int = player.int-5
            player.str = player.str-1
            player.dex = player.dex-1
            player.end = player.end-1
