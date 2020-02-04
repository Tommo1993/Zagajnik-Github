
import time
import random
from data.locdesc import *
#from data.locdefs import *
#from data.enemydefs import *
#from data.enemylist import *
#from data.itemdefs import *
#from data.leveldefs import *
#from data.statdefs import PlayerStats
#from data.classdefs import ClassDefs

#####OBRAŻENIA#####
#Obrażenia*typ* - Rodzaj zadawanych obrażeń zawartych w definicji (def)
#Kłute i Cięte skalują się ze zręcznością Kłute bardziej natomiast z drugiej strony obrażenia bazowe bronii posiadających ten typ są niższe.
#Obuchowe skalują się z siłą, skalują się najlepiej ze wszystkich typów, natomiast obrażenia bazowe są najniższe ze wszystkich.
#ObrażeniaInput*cyfra* - surowe obrażenia surowe przemnożone przez dopowiedni mnożnik.
#ObrażeniaOutput*cyfra* - Obrażenia niesurowe (XD) surowe obliczone wraz z atrybutem przy odpowiednim mnożnikiem (dex, str)
#ObrażeniaWychodzące- faktyczne obrażenia zadawane przez gracza, program sprawdza jakie obrażenia zadaje broń na podstawie jej ID czyli
#playerOutputDMG - Wartość obrażeń wychodzących

def ObrażeniaKłute(player):
	ObrażeniaInput1 = 0.60*player.weapondamage
	ObrażeniaOutput1 = ObrażeniaInput1*(0.10*player.dex)

def ObrażeniaCięte(player):
	ObrażeniaInput2 = 0.40*player.weapondamage
	ObrażeniaOutput2 = ObrażeniaInput2*(0.10*player.dex)

def ObrażeniaObuchowe(player):
	ObrażeniaInput3 = 0.75*player.weapondamage
	ObrażeniaOutput3 = ObrażeniaInput3*(0.10*player.str)
    
def ObrażeniaWychodzące(ObrażeniaCięte, ObrażeniaKłute, ObrażeniaObuchowe, player):
	if item.itemslotweapon1[16] in range(0,30) and item.itemslotweapon1[21] == 1:
		playerOutputDMG = ObrażeniaOutput1 #-entity.Odporność
	if item.itemslotweapon1[16] in range(31,60) and item.itemslotweapon1[21] == 2:
		playerOutputDMG = ObrażeniaOutput2
	if item.itemslotweapon1[16] in range(61,90) and item.itemslotweapon1[21] == 3:
		playerOutputDMG = ObrażeniaOutput3
	return playerOutputDMG
	
	
def Bronie(defineinventory,item):
	if item.itemslotweapon1[16] == 1:
		[1,"Miecz Testowy","Tego tu nie powinno być!","weapon","shortsword",0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,2]
		[1,"Bastardowy Miecz Testowy","Tego tu nie powinno być!","weapon","longsword",0,0,0,0,0,0,0,0,0,0,12,0,0,0,0,2]
		[1,"Testowa Szabla","Tego tu nie powinno być!","weapon","sabre",0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,2]
		
	if item.itemslotweapon1[16] == 2:
		[1,"Testowa Pika","Tego tu nie powinno być!","weapon","polearms",0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,1]
		[1,"Testowy Rapier","Tego tu nie powinno być!","weapon","rapier",0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,1]
		
	if item.itemslotweapon1[16] == 3:
		[1,"Testowy Buzdygan","Tego tu nie powinno być!","weapon","mace",0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3]
		[1,"Pięści","Twoje wierne pięści!","weapon","fists",0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,3]
		[1,"Testowy Młot Bojowy","Tego tu nie powinno być!","weapon","hammer",0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,3]
	
#####OBRAŻENIA#####

#####SYSTEM WALKI#####
tekstBrakuMany="Nie masz many! WRÓĆ lub Wybierz"
class EnemyStats:
    def __init__(self, name, ID, HP, MP, attackdmg, EXPreward):
        self.name = name
        self.ID = ID
        self.HP = HP
        self.MP = MP
        self.attackdmg = attackdmg
        self.EXPreward = EXPreward
def EnemySpawn(entity): #(w systemie): def Łyżeczka Dżemu(ID):
                            #                    ID=1 , itd. 
    if entity.ID == 1:
        entity.name = "Łyżeczka Dżemu"
        entity.HP = 14
        entity.MP = 2
        entity.attackdmg = 1
        entity.EXPreward = 10
    if entity.ID == 2:
        entity.name = "Mysz Polna"
        entity.HP = 5
        entity.MP = 1
        entity.attackdmg = 2
        entity.EXPreward = 3
    if entity.ID == 3:
        entity.name = "Myszoskoczek"
        entity.HP = 10
        entity.MP = 1
        entity.attackdmg = 1
        entity.EXPreward = 5
    if entity.ID == 4:
        entity.name = "Konik Polny"
        entity.HP = 4
        entity.MP = 3
        entity.attackdmg = 2
        entity.EXPreward = 2
    if entity.ID == 5:
        entity.name = "Mały Lis"
        entity.HP = 20
        entity.MP = 5
        entity.attackdmg = 4
        entity.EXPreward = 9
    if entity.ID == 6:
        entity.name = "Młody Wilk"
        entity.HP = 35
        entity.MP = 10
        entity.attackdmg = 7
        entity.EXPreward = 25
    if entity.ID == 7:
        entity.name = "Wyjątkowo Prymitywny Troglodyta"
        entity.HP = 60
        entity.MP = 10
        entity.attackdmg = 10
        entity.EXPreward = 100
    if entity.ID == 8:
        entity.name = "Serek Szczura"
        entity.HP = 2
        entity.MP = 80
        entity.attackdmg = 15
        entity.EXPreward = 80
    if entity.ID == 9:
        entity.name = "Mommy"
        entity.HP = 130
        entity.MP = 0
        entity.attackdmg = 7
        entity.EXPreward = 120	
    if entity.ID == 10:
        entity.name = "Projekt B.E.R.T.O."
        entity.HP = 70
        entity.MP = 20
        entity.attackdmg = 20
        entity.EXPreward = 150
    if entity.ID==11:
        entity.name = "Ździczały pies"
        entity.HP = 30
        entity.MP = 10
        entity.attackdmg = 5
        entity.EXPreward = 15
    if entity.ID==12:
        entity.name = "Jaskółka"
        entity.HP =10
        entity.MP =25
        entity.attackdmg =3
        entity.EXPreward =5
    if entity.ID==13:
        entity.name = "Gruby"
        entity.HP = 100
        entity.MP = 5
        entity.attackdmg = 4
        entity.EXPreward = 100
    if entity.ID==14:
        entity.name = "Kamyk"
        entity.HP = 10
        entity.MP = 0
        entity.attackdmg = 0
        entity.EXPreward = 1
    if entity.ID==15:
        entity.name = "Shrek"
        entity.HP = 80
        entity.MP = 25
        entity.attackdmg = 3
        entity.EXPreward = 5
    if entity.ID==16:
        entity.name = "Gromada Rycerzy Cheddara"
        entity.HP = 90
        entity.MP = 15
        entity.attackdmg = 18
        entity.EXPreward = 250
    if entity.ID==17:
        entity.name = "Bandyta"
        entity.HP = 75
        entity.MP = 10
        entity.attackdmg = 16
        entity.EXPreward = 150
    if entity.ID==18:
        entity.name = "Ogr"
        entity.HP = 90
        entity.MP = 9
        entity.attackdmg = 15
        entity.EXPreward = 250
    if entity.ID==19:
        entity.name = "Kłusownik"
        entity.HP = 30
        entity.MP = 4
        entity.attackdmg = 4
        entity.EXPreward = 50

        
def Występowanie_Przeciwnika(Lokacja,entity):
    #if Lokacja in range(Lokacje przeciwników)
        if entity.ID in range(1,19):
            print (entity.name)
            print ("HP wynosi") + entity.HP
            print ("MP wynosi") + entity.MP
            print()
            print()
            print()

def MagiaWroga(player,entity):
    MagicEntDec=random.randint(0,6) 
    def KulaOgnia1(player,entity):
            entity.MP -= 3
            player.HP -= 5
            Wybór(player,entity)
            return player,entity
    def WysysanieŻycia1(player,entity):
            entity.MP -= 5
            player.HP -= 2
            entity.HP += 2
            Wybór(player,entity)
            return player,entity
    def MroźnyPodmuch1(player,entity):
            entity.MP -= 5
            player.HP -= 4
            Wybór(player,entity)
            return player,entity
    def Bertserker1(player,entity):
            entity.HP -= 2
            entity.MP -= 5
            player.HP -= 9
            Wybór(player,entity)
            return player,entity
    def Wstrząs1(player,entity):
            entity.MP -= 6
            player.HP -= 4
            player.MP -= 3
            Wybór(player,entity)
            return player,entity
    def Otrucie1(player,entity):
            entity.MP -= 7
            player.HP -= 3
            Wybór(player,entity)
            Trucizna1 = 1
            return player, entity
    if MagicEntDec==1: # gdy test się nie uda Robi cały proceder raz jeszcze
        if entity.MP >= 3:
            KulaOgnia1(player,entity)
        else:
            del MagicEntDec # OPtyMaLIZacJa BErTO
            MagiaWroga(player,entity)
    if MagicEntDec==2:
        if entity.MP >= 5:
            WysysanieŻycia1(player,entity)
        else:
            del MagicEntDec
            MagiaWroga(player,entity)
    if MagicEntDec==3:
        if entity.MP >= 5:
            MroźnyPodmuch(player,entity)
        else:
            del MagicEntDec
            MagiaWroga(player,entity)
    if MagicEntDec==4:
        if entity.MP >= 5 and entity.HP > 2: # no bo jak byłoby równe to by był autokil heh
            Bertserker1(player,entity)
        else:
            del MagicEntDec
            MagiaWroga(player,entity)
    if MagicEntDec==5:
        if entity.MP >= 6:
            Wstrząs1(player,entity)
        else:
            del MagicEntDec
            MagiaWroga(player,entity)
    if MagicEntDec==6:
        if entity.MP >= 7:
            Otrucie1(player,entity)
        else:
            del MagicEntDec
            MagiaWroga

def Magia(player,entity):
    print("Co chciałbyś wybrać?")
    print("(Aby użyć coś innego wpisz WRÓĆ.)")
    Magicstr = str(input())
    Magiclist=["Kula ognia","Wysysanie Życia","Mroźny Podmuch","Berserker","Wstząs","Otrucie"]
    print(Magiclist)
    def KulaOgnia(player,entity): #3
        if player.MP < 3:
            print(NoManaVerse)
            Wybór(player,entity)
        if player.MP >= 3:
            player.MP -= 3
            entity.HP -= 5
            return player, entity
    def WysysanieŻycia(player,entity): #5
        if player.MP < 3:
            print(NoManaVerse)
            Wybór(player,entity)
            if player.MP > 3 and player.MP < 5:
                print(" Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia.")
                print("Czy chcesz ją użyć?")
                SpellDec = str(input()).lower()
                if SpellDec == "tak":
                        del SpellDec
                        KulaOgnia(player,entity)
                if SpellDec == "nie":
                        del SpellDec
                        Wybór(player,entity)
                else:
                        print("Co? Co powiedziałeś?")
                        return SpellDec
        if player.MP >= 5:
            player.MP -= 5
            entity.HP -= 2
            player.HP += 2
            return player, entity
    def MroźnyPodmuch(player,entity): #5
        if player.MP < 3:
            print(NoManaVerse)
            Wybór(player,entity)
        if player.MP > 3 and player.MP < 5:
            print("Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia.")
            print("Czy chcesz ją użyć?")
            SpellDec = str(input()).lower()
            if SpellDec == "tak":
                del SpellDec
                KulaOgnia(player,entity)
            if SpellDec in "nie":
                del SpellDec
                Wybór(player,entity)
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP >= 5:
            player.MP -= 5
            entity.HP -= 4
        return player, entity
    def Berserker(player,entity): #5
        if player.MP < 3:
            print(NoManaVerse)
            Wybór(player,entity)
        if player.MP > 3 and player.MP < 5:
                print("Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia.")
                print("Czy chcesz ją użyć?")
                SpellDec = str(input()).lower()
                if SpellDec == "tak":
                    del SpellDec
                    KulaOgnia(player,entity)
                if SpellDec == "nie":
                    del SpellDec
                    Wybór(player,entity)
                else:
                    print("Co? Co powiedziałeś?")
                    return SpellDec
        if player.MP >= 5:
             if player.HP <= 2 :
                print("...ale przecież wykonując to zaklęcie popełnisz sudoku (seppuku dla niekumatych)")
                print("Czy na pewno chcesz to zrobić?")
                Sudoku=str(input()).lower()
                if Sudoku == "tak":
                    player.HP -= 2
                    player.MP -= 5
                    entity.HP -= 9
                if Sudoku == "nie":
                    if player.MP > 3 and player.MP < 5:
                        print ("Zawsze stać cię jeszcze na Kulę Ognia.")
                        print ("Czy chcesz ją użyć?")
                        SpellDec = str(input()).lower()
                        if SpellDec == "nie":
                            del SpellDec
                            KulaOgnia(player,entity)
                        if SpellDec == "tak":
                            del SpellDec
                            Wybór(player,entity)
                        else:
                            print("Co? Co powiedziałeś?")
                            return SpellDec
                    else:
                        print ("No więc musisz wybrać atak.")
                        time.sleep(2)
                        Wybór(player,entity)
                else:
                    player.HP -= 2
                    player.MP -= 5
                    entity.HP -= 9
                    return player, entity
    def Wstrząs(player,entity): #6
        if player.MP < 3:
            print(NoManaVerse)
            Wybór(player)
        if player.MP > 3 and player.MP < 5:
            print(" Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia.")
            print("Czy chcesz ją użyć?")
            SpellDec = str(input()).lower()
            if SpellDec == "tak":
                del SpellDec
                KulaOgnia
            if SpellDec == "nie":
                del SpellDec
                Wybór
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP > 3 and player.MP < 6:
            print("Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia, Mroźny Podmuch i Berserkera.")
            print("Czy zechcesz użyć, którejchś z tych zaklęć?") #  którejchś - nie wiem czy to poprawna forma gramatyczna
            print("Aby wybrać Kulę Ognia wciśnij 1, aby użyć Mroźnego Podmuchu wciśnij 2")
            print("Aby rzucić Berserkera wciśnij 3")
            SpellDec=str(input())
            if SpellDec == "1":
                del SpellDec
                KulaOgnia(player,entity)
            if SpellDec == "2":
                del SpellDec
                MroźnyPodmuch(player,entity)
            if SpellDec == "3":
                del SpellDec
                Berserker(player,entity)
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP >= 6:
            player.MP -= 6
            entity.HP -= 4
            entity.MP -= 3
            return player, entity
    def Otrucie(player,entity): #7
        if player.MP < 3:
            print(NoManaVerse)
            Wybór
        if player.MP > 3 and player.MP < 5:
            print(" Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia.")
            print("Czy chcesz ją użyć?")
            SpellDec = str(input())
            if SpellDec == "tak":
                del SpellDec
                KulaOgnia(player,entity)
            if SpellDec == "nie":
                del SpellDec
                Wybór(player,entity)
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP > 3 and player.MP < 6:
            print("Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia, Mroźny Podmuch i Berserkera.")
            print("Czy zechcesz użyć, którejchś z tych zaklęć?") #  którejchś - nie wiem czy to poprawna forma gramatyczna
            print("Aby wybrać Kulę Ognia wciśnij 1, aby użyć Mroźnego Podmuchu wciśnij 2")
            print("Aby rzucić Berserkera wciśnij 3")
            SpellDec=str(input())
            if SpellDec == "1":
                del SpellDec
                KulaOgnia(player,entity)
            if SpellDec == "2":
                del SpellDec
                MroźnyPodmuch(player,entity)
            if SpellDec == "3":
                del SpellDec
                Berserker(player,entity)
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP > 3 and player.MP < 7:
            print("Nie stać cię na to zaklęcie, ale stać cię jeszcze na Kulę Ognia, Mroźny Podmuch, Berserkera i Wstrząs.")
            print("Czy zechcesz użyć, którejchś z tych zaklęć?") #  którejchś - nie wiem czy to poprawna forma gramatyczna
            print("Aby wybrać Kulę Ognia wciśnij 1, aby użyć Mroźnego Podmuchu wciśnij 2")
            print("Aby rzucić Berserkera wciśnij 3, zaś aby powalić wroga Wstrząsem wciśnij 4")
            SpellDec=str(input())
            if SpellDec == "1":
                del SpellDec
                KulaOgnia(player,entity)
            if SpellDec == "2":
                del SpellDec
                MroźnyPodmuch(player,entity)
            if SpellDec == "3":
                del SpellDec
                Berserker(player,entity)
            if SpellDec == "4":
                del SpellDec
                Wstrząs(player,entity)
            else:
                print("Co? Co powiedziałeś?")
                return SpellDec
        if player.MP >= 7:
             player.MP -= 7
             Trucizna = 1
             return player, entity
    if Magicstr == Magiclist[0]:
        KulaOgnia(player,entity)
    if Magicstr == Magiclist[1]:
        WysysanieŻycia(player,entity)
    if Magicstr == Magiclist[2]:
        MroźnyPodmuch(player,entity)
    if Magicstr == Magiclist[3]:
        Bertserker(player,entity)
    if Magicstr == Magiclist[4]:
        Wstrząs(player,entity)
    if Magicstr == Magiclist[5]:
        Otrucie(player,entity)
    if Magicstr == "WRÓĆ":
        Wybór(player,entity)
    if Magicstr not in Magiclist and Magicstr != "WRÓĆ":
        print("Chyba coś pomyliłeś.")
        #miejsce celowo pozostawione puste

def WybórPrzeciwnika(player,entity): # czyli jego atak lub magia.
    if Trucizna in range (0,3):
        entity.HP -= 3
    if Trucizna > 0:
        Trucizna += 1
    LosDecWalkiPrzeciwnika=random.randint(0,2)
    if LosDecWalkiPrzeciwnika==1:
        if entity.MP not in range(0,3):
            MagiaWroga(player,entity)
        else:
            AtakPrzeciwnika(player,entity)
def Atak(player,entity,Trucizna1):			
    Los=random.randint(0,9)
    if Los==1 or Los==2:
        print("DoStaŁ, ALe PrawIE Go NIe ZarYSOwalIŚmY.")
        entity.HP -= 0.2* playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los ==3:
        print("Machłeś się i ledwo żeś go trafił.")
        entity.HP-=0.4* playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los ==4:
        print("No,no,no... Całkiem, całkiem. ")
        entity.HP-=0.6*playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los ==5:
        print("Ała to musiało boleć.")
        entity.HP-=0.8* playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los ==6:
        print("Ach jak przyjemnie poczuć czyjąś krew.")
        entity.HP-=playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los ==7:
        print("ZDEWASTOWAŁEŚ swojego wroga! Popamięta sobie na zawsze.")
        entity.HP-=1.2*playerOutputDMG
        WybórPrzeciwnika(player,entity)
    if Los==8 or Los==9:
        LosChybienia==random.randint(0,8)
        if LosChybienia==1:
            print("Wróg uskoczył i uderzył cię od boku.")
            player.HP-=2
            WybórPrzeciwnika(player,entity)
        if LosChybienia==8:
            print("Oponent zrobił serię przewrotów ninja po czym uderzył się o parapet.")
            entity.HP-=1
            WybórPrzeciwnika(player,entity)
        if LosChybienia==2:
            print("Ciosy wyprowadza się z nadgarstka, a nie od łokcia!!!")
            WybórPrzeciwnika(player,entity)
        if LosChybienia==3:
            print("Słońce oślepiło cię swoim jasnym blaskiem i nie zaatakowałeś.")
            WybórPrzeciwnika(player,entity)
        if LosChybienia==4:
            print("Masz kryzys egzystencjalny.")
            WybórPrzeciwnika(player,entity)
        if LosChybienia==5:
            print("Zamiast atakować przeciwnika zacząłeś go obrażać.")
            WybórPrzeciwnika(player,entity)
        if LosChybienia==6:
            print("Przeciwnik uszedł z pola walki ale pojawił się następny łudząco podobny")
            print("do poprzedniego.")
            WybórPrzeciwnika(player,entity)
        if LosChybienia==7:
            print("Począłeś dyplomatyczną konwersację z przeciwnikiem, lecz on nie podzielał ")
            print("twoich pacyfistycznych intencji.")
            WybórPrzeciwnika(player,entity)
def AtakPrzeciwnika(player,entity):
    Los2=random.randint(0,8)
    Los3=random.randint(0,9)
    if Los3==1 or Los3==2:
        LosOrganów = "rączki"
    if Los3==3 or Los3==4:
        LosOrganów = "nóżki"
    if Los3==5 or Los3==6:
        LosOrganów = "śledziony"
    if Los3==7 or Los3==8:
        LosOrganów = "części płynu mózgowo-rdzeniowego"
    if Los3==9:
        LosOrganów = "ucha"

    if Los2==1 or Los2==7:
        print("Twój przeciwnik jakoś oka do tego ataku nie miał.")
        player.HP-=0.2*entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==2:
        print("I to ma być cios?!")
        player.HP-=0.4*entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==3:
        print("Jakoś to zniosę. Bywało gorzej.")
        player.HP-=0.6*entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==4:
        print("Silny skurczybyk jak stu chłopa.")
        player.HP-=0.8*entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==5:
        print("Twój przeciwnik wie jak zrobić, żeby bolało.")
        player.HP-=entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==6:
        print("Brak" + LosOrganów +  "hmmm... To chyba dobrze.")
        player.HP-=1.2*entity.attackdmg
        Wybór(player,entity,Trucizna1)
    if Los2==7 or Los2==8:
        LosChybienia2=random.randint(0,7)
        if LosChybienia2==1:
            print("Sprzedałeś przeciwnikiowi psztyczka w nos i wytrąciłeś")
            print("go z równowagi.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==2:
            print("Przeciwnika zaswędziało coś w nosie i musiał odkichnąć.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==3:
            print("Oponent zobaczył króliczka, a wiesz że ma do nich słabość.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==4:
            print("Twój wróg umiejętnością się nie popisał.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==5:
            print("Niemcy proszę pana.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==6:
            print("Twój antagonista poślizgnął się na kawałku słomy z twojej zbroi.")
            Wybór(player,entity,Trucizna1)
        if LosChybienia2==7:
            print("Twój przeciwnik poszedł AFK.")
            Wybór(player,entity,Trucizna1)
			
def FirstBlood(entity,player,playerOutputDMG):
    if entity.attackdmg > playerOutputDMG:
        Atak(player,entity)
    if entity.attackdmg < playerOutputDMG:
        WybórPrzeciwnika(player,entity,Trucizna)
    if entity.attackdmg == playerOutputDMG:
        LosAtaku=random.randint(0,2)
        if LosAtaku==1:
            Atak(player,entity,Trucizna1)
        if LosAtaku==2:
            WybórPrzeciwnika(player,entity,Trucizna)


def Wybór(player,entity,Trucizna1):
    if Trucizna1 == 4:
        Trucizna1 = 0
    if Trucizna1 in range (0,3):
        player.HP-=3
        print("Otruto cię!")
    if Trucizna1 > 0:
        Trucizna1 += 1
    print("Chcesz użyć ATAK, MAGIA, EKWIPUNEK, czy UCIECZKA?")
    wybór=str(input())
    if wybór == "ATAK":
        Atak(player,entity)
    if wybór == "MAGIA":
        Magia(player,entity)
   # if wybór == "EKWIPUNEK": I tu Berto z pomocą idą podki i inne pierdoły
    if wybór =="UCIECZKA":
        if player.dex*0.6+player.HP*0.6-entity.attackdmg*0.2>5:
            A=1     #(kontunuuje dalej do funkcji opisu i czynności danej lokacji) to A=1, bo błąd wyskakiwał
        else:
            print("Twoja ucieczka się nie powiedzie. GUŁAG albo SUDOKU")
            ssij=str(input())
            if ssij == "GUŁAG":
                WybórPrzeciwnika(player,entity,Trucizna)
            if ssij =="SUDOKU":
                player.HP=0
                


def DeathStats(player,entity):
    if entity.HP<0:
        entity.HP=0
        LosWroga=random.randint(0,5)
    if player.HP == MaxHP:
        LosWroga2= " i wcale cię nie ruszyli Wilk syty i owca, no cóż..."
    if player.HP <= MaxHP - MaxHP*0.1 and player.HP >= MaxHP - MaxHP*0.3:
        LosWroga2= ", lecz nieźle cię poturbowali."
    if player.HP <= MaxHP - MaxHP*0.31 and player.HP >= MaxHP - MaxHP*0.5:
        LosWroga2= ", ale twoje rany szybko się nie zagoją."
    if player.HP <= MaxHP - MaxHP*0.51 and player.HP >= MaxHP - MaxHP*0.7:
        LosWroga2= ", ale dali ci w kość."
    if player.HP <= MaxHP - MaxHP*0.71 and player.HP >= MaxHP - MaxHP*0.99:
        LosWroga2= ". Mimo to szukałbym medyka. Te rany nie wyglądają dobrze..."
    if LosWroga==1:
        print("Uporałeś się z nim. Hura!")
    if LosWroga==2:
        print("No, no no... Nieźle ci poszło")
    if LosWroga==3 or LosWroga==5:
        print("Nie było źle" + LosWroga2)
    if LosWroga==4:
        print("Uporałeś się z nim. Hurra!")
    if entity.MP<0:
        entity.MP=0
        AtakPrzeciwnika(player,entity)
    if player.HP<0:
        player.HP=0
    if  player.MP<0:
        player.MP=0
    if player.HP==0:
        print("U n00b")
        Lokacja=0 # śmierdź się zrobi później
#####SYSTEM WALKI#####

#####SYSTEM QUESTÓW#####
def Questy():
        
    DaneQuesta=[0,"","","","",0,0,0,0] #Slot 0- Aktywność questa Slot 1- Nazwa Slot 2- Opis Slot 3- Zleceniodawca Slot 4- Nagroda przedmiot Slot 5- ilość exp Slot 6- nagroda pieniądze 7- ID questa 8- status
    DaneQuesta1=[0,"Miejscowy Bohater","Zostało mi powierzone bardzo trudne zadanie - odnaleźć łyżeczkę dżemu.","Staruszek z Crosset","",100,5,1,0]
    DaneWszystkichQuestów=[]
    DaneWszystkichQuestów.append(DaneQuesta)
    DaneWszystkichQuestów.append(DaneQuesta1)
    #print(DaneWszystkichQuestów)
    return DaneWszystkichQuestów

def SprawdzanieStatusu(DaneWszystkichQuestów, ActionInput, SzukanieMiejscaNaPrzedmiot, KoniecQuesta):
    while DaneWszystkichQuestów[1][0] == 1 and DaneWszystkichQuestów[1][7] >0:
        if DaneWszystkichQuestów[1][8] == 0 and DaneWszystkichQuestów[1][7] == 1 and ActionInput == "quests":
            print('''Miejscowy Bohater - Odnajdź łyżeczkę dżemu.
            Nagroda - 5 Koron, 100exp
            Zleceniodawca - Staruszek z Crosset''')
        if DaneWszystkichQuestów[1][8] == 1 and DaneWszystkichQuestów[1][7] == 1 and ActionInput == "quests":
            print('''Miejscowy Bohater - Wykonane.
            Nagroda - 5 Koron, 100exp
            Zleceniodawca - Staruszek z Crosset''')
        if DaneWszystkichQuestów[1][8] == 1 and DaneWszystkichQuestów[1][7] == 1:
            print('''Zadanie "Miejscowy Bohater" zostało ukończone.
            Wróć do zleceniodawcy po nagrodę.''')
            if DaneWszystkichQuestów[1][8] == 1 and Lokacja == 12:
                print('''Dziękuje Ci! Kto jest małą łyżeczką, no kto!
            Żebym nie wyszedł na dusigrosza o to mała nagroda.''')
                print('Otrzymano: 5 Koron')
                if DaneWszystkichQuestów[1][4] == 0:
                    KoniecQuesta(player, Questy)
                    DaneQuesta1[0] == 3
                if DaneWszystkichQuestów[1][4] != 0:
                    SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta)
                    KoniecQuesta(player, Questy)
                    DaneWszystkichQuestów[1][0] == 3
    
def PrintQuest(Questy):
    print()
    print(DaneQuesta[1])
    print(DaneQuesta[2])
    print(DaneQuesta[3])
    print(DaneQuesta[4])
    print(DaneQuesta[5])
    print(DaneQuesta[6])
    print()

def KoniecQuesta(player, Questy):
    player.EXP += DaneQuesta[5]
    item.gold += DaneQuesta[6]
    OtrzymanyPRZEDMIOT = DaneQuesta[4]
    return player.EXP
    return item.gold

def SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta):
    SprawdzenieMiejsca = []
    
    if item.inventoryslot1[0] == 0:
        item.inventoryslot1 == OtrzymanyPRZEDMIOT
    if item.inventoryslot1[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(1)
        return SprawdzenieMiejsca
        
    if item.inventoryslot2[0] == 0:
        item.inventoryslot2 == OtrzymanyPRZEDMIOT      
    if SprawdzenieMiejsca[0] == 1:
        if item.inventoryslot2[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(2)
            return SprawdzenieMiejsca
            
    if item.inventoryslot3[0] == 0:
        item.inventoryslot3 == OtrzymanyPRZEDMIOT            
    if SprawdzenieMiejsca[0] == 2:
        if item.inventoryslot3[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(3)
            return SprawdzenieMiejsca
            
    if item.inventoryslot4[0] == 0:
        item.inventoryslot4 == OtrzymanyPRZEDMIOT
    if SprawdzenieMiejsca[0] == 3:        
        if item.inventoryslot4[0] == 1:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(4)
            return SprawdzenieMiejsca
    
    if item.inventoryslot5[0] == 0:
        item.inventoryslot5 == OtrzymanyPRZEDMIOT
    if item.inventoryslot5[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(5)
        return SprawdzenieMiejsca
        
    if item.inventoryslot6[0] == 0:
        item.inventoryslot6 == OtrzymanyPRZEDMIOT
    if item.inventoryslot6[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(6)
        return SprawdzenieMiejsca
        
    if item.inventoryslot7[0] == 0:
        item.inventoryslot7 == OtrzymanyPRZEDMIOT
    if item.inventoryslot7[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(7)
        return SprawdzenieMiejsca
    
    if item.inventoryslot8[0] == 0:
        item.inventoryslot8 == OtrzymanyPRZEDMIOT
    if item.inventoryslot8[0] == 1:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(8)
        return SprawdzenieMiejsca
    
    if item.inventoryslot10[0] == 0:
        item.inventoryslot10 == OtrzymanyPRZEDMIOT
    if item.inventoryslot10[0] == 1:
        print('Brak miejsca w ekwipunku!')
        #PrzedmiotNaGape1 = 1
        #while PrzedmiotNaGape1 == 1 and Lokacja == LokacjaZleceniodawcy:
        #   SzukanieMiejscaNaPrzedmiot(item, KoniecQuesta)
#####SYSTEM QUESTÓW#####

#####GRACZ#####
class PlayerStats:
    def __init__(player, name, HP, MP, MaxHP, MaxMP, MaxHPnocalc, MaxMPnocalc, EXP, level, str, dex, int, end, luck, basedamage, weapondamage, statpoint, pclass, subclass):
        player.name = name
        player.HP = HP
        player.MP = MP
        player.MaxHP = MaxHP
        player.MaxMP = MaxMP
        player.MaxHPnocalc = MaxHPnocalc
        player.MaxMPnocalc = MaxMPnocalc
        player.EXP = EXP
        player.level = level
        player.str = str
        player.dex = dex
        player.int = int
        player.end = end
        player.luck = luck
        player.basedamage = basedamage
        player.weapondamage = weapondamage
        player.statpoint = statpoint
        player.pclass = pclass
        player.subclass = subclass
def ClassChoice(player,item,StartInput):		
    if StartInput == "1" or StartInput == "zbrojny":
        print("Twoja klasa to zbrojny.")
        player.MaxHP == 20
        player.HP == 20
        player.MaxMP == 5
        player.MP == 5
        player.str = 3
        player.dex = 2
        player.int = 1
        player.end = 2
        player.luck = 1
        player.pclass = 1
        item.itemslotchest = [1,"Stary skórzany napierśnik","Jeszcze się trzyma...","armor","armorchest",0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.1,0.05,0]
        item.itemslotlegs = [1,"Dziurawe włókniane spodnie","Więcej dziur niż nitek.","armor","armorlegs",0,0,0,0,0,0,0,0,0,0,0,0,0,0.05,0,0]
        item.itemslotfoot = [1,"Buty bez podeszwy","ochroniają podbicie stopy przed podmuchem wiatru!","armor","armorfoot",0,0,0,0,0,0,0,0,0,0,0,0,0.05,0.05,0.5,0]
        item.itemslotweapon1 = [1,"Drewniana pałka","W zasadzie grubszy kij.","weapon","mace",0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3]
        item.inventoryslot1 = [1,2,"Bochenek Chleba","Czerstwy, ale da się zjeść.","consumable","food",4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        item.inventoryslot2 = [1,1,"Bukłak wody","Mmm... bardzo błotnista i prosto z bagna.","consumable","food",0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    if StartInput == "2" or StartInput == "zwiadowca":
        rint("Twoja klasa to zwiadowca.")
        player.MaxHP == 15
        player.HP == 15
        player.MaxMP == 10
        player.MP == 5
        player.pclass = 2
    if StartInput == "3" or StartInput == "łotr":
        print("Twoja klasa to łotr.")
        player.MaxHP == 10
        player.HP == 10
        player.MaxMP == 15
        player.MP == 15
        player.pclass = 3
    return player, item

#####GRACZ#####

######ALKOHOLE######
def Alkohole(DaneWszystkichAlkoholi):
    #
    #Alkohol=[0,0,0,0,"","",0] # indeks 0- trwałość, indeks 1- poziom % (od 1 do 10), indeks 2- mnożnik uzależnienia (od 1 do 10), indeks 3- narazie nic, indeks 4- Nazwa, indeks 5- Opis, 6- aktywność.
    #
    Denaturat=[10,9,1,1,"Denaturat","Nemezis twojej wątroby i układu nerwowego.",0]
    KordiałZeStokrotek=[4,5,2,1,"Kordiał ze stokrotek","Szlachecki trunek z miętowym posmakiem.",0]
    TrillskieJasne=[2,1,4,1,"Trillskie jasne","Specjalność browarów Trill.",0]
 
    DaneWszystkichAlkoholi.append(Denaturat)
    DaneWszystkichAlkoholi.append(KordiałZeStokrotek)
    DaneWszystkichAlkoholi.append(TrillskieJasne)
    
    #turazakończenia = 0    
    #StopienOdurzenia = DaneWszystkichAlkoholi[0][1]/player.str or DaneWszystkichAlkoholi[1][1]/player.str or DaneWszystkichAlkoholi[2][1]/player.str
    #StopienUzależnienia = DaneWszystkichAlkoholi[0][2]/player.luck*10 or DaneWszystkichAlkoholi[1][2]/player.luck*10 or DaneWszystkichAlkoholi[2][2]/player.luck*10
    return DaneWszystkichAlkoholi

def SprawdzanieAlkoholi(DaneWszystkichAlkoholi,player,StopienOdurzenia,StopienUzależnienia,Turn,turazakończenia):
    turazakończenia = 0    
    while DaneWszystkichAlkoholi[0][6] == 1 or DaneWszystkichAlkoholi[1][6] == 1 or DaneWszystkichAlkoholi[2][6] == 1:
        if StopienOdurzenia <= 1:
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
        if DaneWszystkichAlkoholi[0][6] == 1:
            turazakończenia = Turn + DaneWszystkichAlkoholi[0][0]
            if turazakończenia == Turn:
                DaneWszystkichAlkoholi[0][6] == 0
        if DaneWszystkichAlkoholi[1][6] == 1:
            turazakończenia = Turn + DaneWszystkichAlkoholi[1][0]
            if turazakończenia == Turn:
                DaneWszystkichAlkoholi[1][6] == 0
        if DaneWszystkichAlkoholi[2][6] == 1:
            turazakończenia = Turn + DaneWszystkichAlkoholi[2][0]
            if turazakończenia == Turn:
                DaneWszystkichAlkoholi[2][6] == 0
    return DaneWszystkichAlkoholi, player, StopienOdurzenia, StopienUzależnienia, Turn, turazakończenia
    if StopienUzależnienia <= 1000:
        print('Brawo, zostałeś alkoholikiem!')
        if DaneWszystkichAlkoholi[0][6] != 1 or DaneWszystkichAlkoholi[1][6] != 1 or DaneWszystkichAlkoholi[2][6] != 1:
            player.MaxHPnocalc = player.MaxHPnocalc-5
            player.MaxMPnocalc = player.MaxMPnocalc-5
            player.int = player.int-10
            player.str = player.str-2
            player.dex = player.dex-2
            player.end = player.end-2
        return DaneWszystkichAlkoholi, player, StopienOdurzenia, StopienUzależnienia, Turn, turazakończenia
        if DaneWszystkichAlkoholi[0][6] == 1 or DaneWszystkichAlkoholi[1][6] == 1 or DaneWszystkichAlkoholi[2][6] == 1:
            player.MaxHPnocalc = player.MaxHPnocalc-1
            player.MaxMPnocalc = player.MaxMPnocalc-1
            player.int = player.int-5
            player.str = player.str-1
            player.dex = player.dex-1
            player.end = player.end-1
        return DaneWszystkichAlkoholi, player, StopienOdurzenia, StopienUzależnienia, Turn, turazakończenia
            #BERTEK PAMIĘTAJ O ZROBIENIU TRWAŁOŚCI EFEKTÓW, ALKOHOLIZM MOŻNA WYLECZYĆ JEDYNIE WYPIJAJĄC SPECJALNĄ POTKĘ.
            #OK!
            
######ALKOHOLE######    


#####EKWIPUNEK#####
def Zbroje(defineinventory, item):  
    [1,"Lekka Przeszywanica","Cieńka osłona z wełny nikomu nie zaszkodzi.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.80,1,0.85,0,0]
    [1,"Zużyta Przeszywanica","Ta przeszywanica najlepsze lata ma już za sobą.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.95,0.95,1,0,0]
    [1,"Solidna Przeszywanica","Krawiec odwalił kawał SOLIDNEJ roboty!","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.75,0.85,0.75,0,0]
    [1,"Wzmocniona Przeszywanica","Przeszywanica wzmacniana dodatkowymy warstwami materiału w nerwalgicznych miejscach.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.70,0.80,0.70,0,0]
    [1,"Bandycka Przeszywanica","Praktycznie uszyta, i przesiąknięta krwią przeszywanica.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.70,0.70,70,0,0]
    [1,"Szlachecka Przeszywanica","Najwyższej jakości przeszywanica przeznaczona dla najbardziej wymagających konsumentów.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.65,0.70,65,0,0]
    [1,"Lekki Kirys","Kirys o grubości 2nm.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.60,0.50,1,0,0]
    [1,"Zużyty Kirys","Wgniotka na wgniotce.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.85,0.90,1,0,0]
    [1,"Solidny Kirys","Płatnerz odwalił kawał SOLIDNEJ roboty!","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.55,0.45,1,0,0]
    [1,"Wzmocniony Kirys","Ocynkowany, i wypolerowany, od wewnątrz podbity słomą, to się nazywa upgrade!","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.55,0.40,0.90,0,0]
    [1,"Bandycki Kirys","W zasadzie to kawał blachy wiązany rzemyczkami za plecami.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.70,0.65,1,0,0]
    [1,"Szlachecki Kirys","Wykonany przez najlepszego płatnerza z Trill, lepszego nie znajdziesz!","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.50,0.35,0.90,0,0]
    [1,"Lekka Brygantyna","Składa się z 3 warstw. Słomy, siana i patyczków.","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0.65,0.65,0.65,0,0]
    [1,"Zużyta Brygantyna","Przypomina połamane kafelki od pieca połączone ze sobą sznurkami.","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0.80,0.80,0.80,0,0]
    [1,"Solidna Brygantyna","Płatnerz odwalił kawał SOLIDNEJ roboty!","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0.60,0.60,0.60,0,0]
    [1,"Wzmocniona Brygantyna","Dodatkowa warstwa słomy zwiększa szanse przeżycia o 1%!","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0.55,0.55,0.55,0,0]
    [1,"Bandycka Brygantyna","Podrąbana biednemu kmiotkowi podczas ostatniego napadu, ponoć wciąż jej szuka.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.75,0.75,0.75,0,0]
    [1,"Szlachecka Brygantyna","Stworzona z porcelany, uranu zubożonego i stali, wyposażona w pancerz reaktywny i system chłodzenia.","armor","armorchest",0,0,4,0,0,0,0,0,0,0,0,0,0,0.40,0.40,0.45,0,0]
    [1,"Lekka Kolczuga","Zaraz czemu z tej zbroi wystaje ogon szczura. Ughhh... mniejsza z tym.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.85,0.95,1,0,0]
    [1,"Zużyta Kolczuga","Kolczuga ledwo smaga oblicze twojej skóry.","armor","armorchest",0,0,1,0,0,0,0,0,0,0,0,0,0,0.75,0.85,0.90,0,0]
    [1,"Solidna Kolczuga","Płatnerz odwalił kawał SOLIDNEJ roboty.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.65,0.80,0.85,0,0]
    [1,"Wzmocniona Kolczuga","Wypolerowane obręcze aż błyszczą od krwi twoich wrogów.","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0.65,0.70,0.75,0,0]
    [1,"Bandycka Kolczuga","Współczuje PRAWOWITEMU właścicielowi.","armor","armorchest",0,0,2,0,0,0,0,0,0,0,0,0,0,0.80,0.75,0.85,0,0]
    [1,"Szlachecka Kolczuga","Zrobiona na zamówienie jakiejś szlacheckiej mości, nic dziwnego że jest na ciebie jak worek.","armor","armorchest",0,0,3,0,0,0,0,0,0,0,0,0,0,0,0.40,0.50,0.65,0,0]
    [1,"Skórzana Kamiezelka","Równie dobrze mogłbyś nic nie zakładać, zapewne przeżyła nie jednego właściciela.","armor","armorchest",0,0,0,0,0,0,0,0,0,0,0,0,0,0.95,1,0.95,0,0]
class Inventory:
    def __init__(item, gold, X, itemslotactive1, itemslotactive2, itemslotactive3, itemslotactive4, itemslotactive5, itemslotactive6, itemslotweapon1, itemslotweapon2, itemslothead, itemslotchest, itemslotarms, itemslothands, itemslotlegs, itemslotfoot, itemslotacc1, itemslotacc2, itemslotacc3, inventoryslot1, inventoryslot2, inventoryslot3, inventoryslot4, inventoryslot5, inventoryslot6, inventoryslot7, inventoryslot8, inventoryslot9, inventoryslot10, assignmentinvslot):
        item.gold=0
        item.X=0
        item.itemslotactive1=itemslotactive1
        item.itemslotactive2=itemslotactive2
        item.itemslotactive3=itemslotactive3
        item.itemslotactive4=itemslotactive4
        item.itemslotactive5=itemslotactive5
        item.itemslotactive6=itemslotactive6 
        item.itemslotweapon1=itemslotweapon1
        item.itemslotweapon2=itemslotweapon2
        item.itemslothead=itemslothead
        item.itemslotchest=itemslotchest
        item.itemslotarms=itemslotarms
        item.itemslothands=itemslothands
        item.itemslotlegs=itemslotlegs
        item.itemslotfoot=itemslotfoot
        item.itemslotacc1=itemslotacc1
        item.itemslotacc2=itemslotacc2
        item.itemslotacc3=itemslotacc3
        item.inventoryslot1=inventoryslot1
        item.inventoryslot2=inventoryslot2 
        item.inventoryslot3=inventoryslot3 
        item.inventoryslot4=inventoryslot4 
        item.inventoryslot5=inventoryslot5 
        item.inventoryslot6=inventoryslot6 
        item.inventoryslot7=inventoryslot7
        item.inventoryslot8=inventoryslot8
        item.inventoryslot9=inventoryslot9
        item.inventoryslot10=inventoryslot10
        item.assignmentinvslot=assignmentinvslot
def defineinventory(item):
    item.itemslotactive1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #sloty ekwipunku (indeksy):
    item.itemslotactive2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 0 = czy jakiś przedmiot tam jest,
    item.itemslotactive3=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 1 = nazwa, slot 2 = opis, slot 3 = typ, slot 4 = podtyp,
    item.itemslotactive4=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 5 = +hp, slot 6 = +mp, slot 7 = maxhp, slot 8 = maxmp,
    item.itemslotactive5=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 9 = +exp, slot 10 = str, slot 11 = dex, slot 12 = int
    item.itemslotactive6=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 13 = end, slot 14 = luck, slot 15 = weapon dmg, slot 16 = ID
    item.itemslotweapon1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 17 = obrona przed obr. kłutymi, slot 18 = obrona przed obr. ciętymi,
    item.itemslotweapon2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 19 = obrona przed obr. obuchowymi, slot 20 = obrona przed magią
    item.itemslothead=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotchest=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotarms=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslothands=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotlegs=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotfoot=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc1=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc2=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.itemslotacc3=[0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot1=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #sloty ekwipunku (indeksy):
    item.inventoryslot2=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 0 = czy jakiś przedmiot tam jest, slot 1 = ilość,
    item.inventoryslot3=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 2 = nazwa, slot 3 = opis, slot 4 = typ, slot 5 = podtyp,
    item.inventoryslot4=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 6 = +hp, slot 7 = +mp, slot 8 = maxhp, slot 9 = maxmp,
    item.inventoryslot5=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 10 = +exp, slot 11 = str, slot 12 = dex, slot 13 = int
    item.inventoryslot6=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 14 = end, slot 15 = luck, slot 16 = weapon dmg, slot 17 = ID
    item.inventoryslot7=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 18 = obrona przed obr. kłutymi, slot 19 = obrona przed obr. ciętymi,
    item.inventoryslot8=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #slot 20 = obrona przed obr. obuchowymi, slot 21 = obrona przed magią
    item.inventoryslot9=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.inventoryslot10=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    item.assignmentinvslot=[0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return item
def itemuse(lookforinv,ActionInput):
    if ActionInput == 'zjedz':
        print("Co chciałbyś zjeść?")
        ActionInput = input().lower()
        lookforinv="food"
        return lookforinv, ActionInput
    if ActionInput == 'użyj':
        print("Co chciałbyś użyć?")
        ActionInput = input().lower()
        lookforinv="consumable"
        return lookforinv, ActionInput
    if ActionInput == 'opis':
        print("O którym przedmiocie chcesz wiedzieć więcej?")
        ActionInput = input().lower()
        lookforinv="desc"
        return lookforinv, ActionInput
    if ActionInput == 'ubierz':
        print("Co chciałbyś ubrać na siebię?")
        ActionInput = input().lower()
        lookforinv="armor"
        return lookforinv, ActionInput
    if ActionInput == 'dobądź':
        print("Jaką broń chciałbyś dobyć?")
        ActionInput = input().lower()
        lookforinv="weapon"
        return lookforinv, ActionInput
    if ActionInput == 'zdejmij':
        print("Co chciałbyś zdjąć z siebie?")
        ActionInput = input().lower()
        lookforinv="armoroff"
        return lookforinv, ActionInput
    if ActionInput == 'schowaj':
        print("Jaką broń chciałbyś schować?")
        ActionInput = input().lower()
        lookforinv="weaponoff"
        return lookforinv, ActionInput
    if ActionInput == 'upuść':
        print("Jaki przedmiot chciałbyś upuścić? Tej akcji nie można cofnąć! (Wybierz przedmiot nie używany przez ciebię)")
        ActionInput = input().lower()
        return ActionInput
    if ActionInput == 'ekwipunek':
        lookforinvtype(ActionInput)
        
def lookforinventory(lookforinv,ActionInput,item): #do zrobienia
    if lookforinv == "food":
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            if item.inventoryslot1[0] == 1:
                player.HP+=item.inventoryslot1[6]
                player.MP+=item.inventoryslot1[7]
                if item.inventoryslot1[1] > 1:
                    item.inventoryslot1[1]-=1
                if item.inventoryslot1[1] == 1:
                    item.inventoryslot1[0] = 0
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            if item.inventoryslot2[0] == 1:
                player.HP+=item.inventoryslot2[6]
                player.MP+=item.inventoryslot2[7]
                if item.inventoryslot2[1] > 1:
                    item.inventoryslot2[1]-=1
                if item.inventoryslot2[1] == 1:
                    item.inventoryslot2[0] = 0
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            if item.inventoryslot3[0] == 1:
                player.HP+=item.inventoryslot3[6]
                player.MP+=item.inventoryslot3[7]
                if item.inventoryslot3[1] > 1:
                    item.inventoryslot3[1]-=1
                if item.inventoryslot3[1] == 1:
                    item.inventoryslot3[0] = 0
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            if item.inventoryslot4[0] == 1:
                player.HP+=item.inventoryslot4[6]
                player.MP+=item.inventoryslot4[7]
                if item.inventoryslot4[1] > 1:
                    item.inventoryslot4[1]-=1
                if item.inventoryslot4[1] == 1:
                    item.inventoryslot4[0] = 0
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            if item.inventoryslot5[0] == 1:
                player.HP+=item.inventoryslot5[6]
                player.MP+=item.inventoryslot5[7]
                if item.inventoryslot5[1] > 1:
                    item.inventoryslot5[1]-=1
                if item.inventoryslot5[1] == 1:
                    item.inventoryslot5[0] = 0
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            if item.inventoryslot6[0] == 1:
                player.HP+=item.inventoryslot6[6]
                player.MP+=item.inventoryslot6[7]
                if item.inventoryslot6[1] > 1:
                    item.inventoryslot6[1]-=1
                if item.inventoryslot6[1] == 1:
                    item.inventoryslot6[0] = 0
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            if item.inventoryslot7[0] == 1:
                player.HP+=item.inventoryslot7[6]
                player.MP+=item.inventoryslot7[7]
                if item.inventoryslot7[1] > 1:
                    item.inventoryslot7[1]-=1
                if item.inventoryslot7[1] == 1:
                    item.inventoryslot7[0] = 0
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            if item.inventoryslot8[0] == 1:
                player.HP+=item.inventoryslot8[6]
                player.MP+=item.inventoryslot8[7]
                if item.inventoryslot8[1] > 1:
                    item.inventoryslot8[1]-=1
                if item.inventoryslot8[1] == 1:
                    item.inventoryslot8[0] = 0
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            if item.inventoryslot9[0] == 1:
                player.HP+=item.inventoryslot9[6]
                player.MP+=item.inventoryslot9[7]
                if item.inventoryslot9[1] > 1:
                    item.inventoryslot9[1]-=1
                if item.inventoryslot9[1] == 1:
                    item.inventoryslot9[0] = 0
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            if item.inventoryslot10[0] == 1:
                player.HP+=item.inventoryslot10[6]
                player.MP+=item.inventoryslot10[7]
                if item.inventoryslot10[1] > 1:
                    item.inventoryslot10[1]-=1
                if item.inventoryslot10[1] == 1:
                    item.inventoryslot10[0] = 0
        
    if lookforinv == "consumable":
        print()
        
    if lookforinv == "armor": #do zrobienia
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot1
            if item.inventoryslot1[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot1[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot1[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot2
            if item.inventoryslot2[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot2[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot2[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot3
            if item.inventoryslot3[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot3[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot3[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot4
            if item.inventoryslot4[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot4[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot4[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot5
            if item.inventoryslot5[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot5[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot5[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot6
            if item.inventoryslot6[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot6[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot6[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot7
            if item.inventoryslot7[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot7[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot7[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot8
            if item.inventoryslot8[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot8[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot8[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot9
            if item.inventoryslot9[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot9[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot9[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot10
            if item.inventoryslot10[5] == 'armorhead':
                item.itemslothead[0] = item.assignmentinvslot[0]
                item.itemslothead[1] = item.assignmentinvslot[2]
                item.itemslothead[2] = item.assignmentinvslot[3]
                item.itemslothead[3] = item.assignmentinvslot[4]
                item.itemslothead[4] = item.assignmentinvslot[5]
                item.itemslothead[5] = item.assignmentinvslot[6]
                item.itemslothead[6] = item.assignmentinvslot[7]
                item.itemslothead[7] = item.assignmentinvslot[8]
                item.itemslothead[8] = item.assignmentinvslot[9]
                item.itemslothead[9] = item.assignmentinvslot[10]
                item.itemslothead[10] = item.assignmentinvslot[11]
                item.itemslothead[11] = item.assignmentinvslot[12]
                item.itemslothead[12] = item.assignmentinvslot[13]
                item.itemslothead[13] = item.assignmentinvslot[14]
                item.itemslothead[14] = item.assignmentinvslot[15]
                item.itemslothead[15] = item.assignmentinvslot[16]
                item.itemslothead[16] = item.assignmentinvslot[17]
                item.itemslothead[17] = item.assignmentinvslot[18]
                item.itemslothead[18] = item.assignmentinvslot[19]
                item.itemslothead[19] = item.assignmentinvslot[20]
                item.itemslothead[20] = item.assignmentinvslot[21]
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armorchest':
                item.itemslotchest[0] = item.assignmentinvslot[0]
                item.itemslotchest[1] = item.assignmentinvslot[2]
                item.itemslotchest[2] = item.assignmentinvslot[3]
                item.itemslotchest[3] = item.assignmentinvslot[4]
                item.itemslotchest[4] = item.assignmentinvslot[5]
                item.itemslotchest[5] = item.assignmentinvslot[6]
                item.itemslotchest[6] = item.assignmentinvslot[7]
                item.itemslotchest[7] = item.assignmentinvslot[8]
                item.itemslotchest[8] = item.assignmentinvslot[9]
                item.itemslotchest[9] = item.assignmentinvslot[10]
                item.itemslotchest[10] = item.assignmentinvslot[11]
                item.itemslotchest[11] = item.assignmentinvslot[12]
                item.itemslotchest[12] = item.assignmentinvslot[13]
                item.itemslotchest[13] = item.assignmentinvslot[14]
                item.itemslotchest[14] = item.assignmentinvslot[15]
                item.itemslotchest[15] = item.assignmentinvslot[16]
                item.itemslotchest[16] = item.assignmentinvslot[17]
                item.itemslotchest[17] = item.assignmentinvslot[18]
                item.itemslotchest[18] = item.assignmentinvslot[19]
                item.itemslotchest[19] = item.assignmentinvslot[20]
                item.itemslotchest[20] = item.assignmentinvslot[21]
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armorarms':
                item.itemslotarms[0] = item.assignmentinvslot[0]
                item.itemslotarms[1] = item.assignmentinvslot[2]
                item.itemslotarms[2] = item.assignmentinvslot[3]
                item.itemslotarms[3] = item.assignmentinvslot[4]
                item.itemslotarms[4] = item.assignmentinvslot[5]
                item.itemslotarms[5] = item.assignmentinvslot[6]
                item.itemslotarms[6] = item.assignmentinvslot[7]
                item.itemslotarms[7] = item.assignmentinvslot[8]
                item.itemslotarms[8] = item.assignmentinvslot[9]
                item.itemslotarms[9] = item.assignmentinvslot[10]
                item.itemslotarms[10] = item.assignmentinvslot[11]
                item.itemslotarms[11] = item.assignmentinvslot[12]
                item.itemslotarms[12] = item.assignmentinvslot[13]
                item.itemslotarms[13] = item.assignmentinvslot[14]
                item.itemslotarms[14] = item.assignmentinvslot[15]
                item.itemslotarms[15] = item.assignmentinvslot[16]
                item.itemslotarms[16] = item.assignmentinvslot[17]
                item.itemslotarms[17] = item.assignmentinvslot[18]
                item.itemslotarms[18] = item.assignmentinvslot[19]
                item.itemslotarms[19] = item.assignmentinvslot[20]
                item.itemslotarms[20] = item.assignmentinvslot[21] 
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armorhands':
                item.itemslothands[0] = item.assignmentinvslot[0]
                item.itemslothands[1] = item.assignmentinvslot[2]
                item.itemslothands[2] = item.assignmentinvslot[3]
                item.itemslothands[3] = item.assignmentinvslot[4]
                item.itemslothands[4] = item.assignmentinvslot[5]
                item.itemslothands[5] = item.assignmentinvslot[6]
                item.itemslothands[6] = item.assignmentinvslot[7]
                item.itemslothands[7] = item.assignmentinvslot[8]
                item.itemslothands[8] = item.assignmentinvslot[9]
                item.itemslothands[9] = item.assignmentinvslot[10]
                item.itemslothands[10] = item.assignmentinvslot[11]
                item.itemslothands[11] = item.assignmentinvslot[12]
                item.itemslothands[12] = item.assignmentinvslot[13]
                item.itemslothands[13] = item.assignmentinvslot[14]
                item.itemslothands[14] = item.assignmentinvslot[15]
                item.itemslothands[15] = item.assignmentinvslot[16]
                item.itemslothands[16] = item.assignmentinvslot[17]
                item.itemslothands[17] = item.assignmentinvslot[18]
                item.itemslothands[18] = item.assignmentinvslot[19]
                item.itemslothands[19] = item.assignmentinvslot[20]
                item.itemslothands[20] = item.assignmentinvslot[21]
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armorlegs':
                item.itemslotlegs[0] = item.assignmentinvslot[0]
                item.itemslotlegs[1] = item.assignmentinvslot[2]
                item.itemslotlegs[2] = item.assignmentinvslot[3]
                item.itemslotlegs[3] = item.assignmentinvslot[4]
                item.itemslotlegs[4] = item.assignmentinvslot[5]
                item.itemslotlegs[5] = item.assignmentinvslot[6]
                item.itemslotlegs[6] = item.assignmentinvslot[7]
                item.itemslotlegs[7] = item.assignmentinvslot[8]
                item.itemslotlegs[8] = item.assignmentinvslot[9]
                item.itemslotlegs[9] = item.assignmentinvslot[10]
                item.itemslotlegs[10] = item.assignmentinvslot[11]
                item.itemslotlegs[11] = item.assignmentinvslot[12]
                item.itemslotlegs[12] = item.assignmentinvslot[13]
                item.itemslotlegs[13] = item.assignmentinvslot[14]
                item.itemslotlegs[14] = item.assignmentinvslot[15]
                item.itemslotlegs[15] = item.assignmentinvslot[16]
                item.itemslotlegs[16] = item.assignmentinvslot[17]
                item.itemslotlegs[17] = item.assignmentinvslot[18]
                item.itemslotlegs[18] = item.assignmentinvslot[19]
                item.itemslotlegs[19] = item.assignmentinvslot[20]
                item.itemslotlegs[20] = item.assignmentinvslot[21] 
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armorfoot':
                item.itemslotfoot[0] = item.assignmentinvslot[0]
                item.itemslotfoot[1] = item.assignmentinvslot[2]
                item.itemslotfoot[2] = item.assignmentinvslot[3]
                item.itemslotfoot[3] = item.assignmentinvslot[4]
                item.itemslotfoot[4] = item.assignmentinvslot[5]
                item.itemslotfoot[5] = item.assignmentinvslot[6]
                item.itemslotfoot[6] = item.assignmentinvslot[7]
                item.itemslotfoot[7] = item.assignmentinvslot[8]
                item.itemslotfoot[8] = item.assignmentinvslot[9]
                item.itemslotfoot[9] = item.assignmentinvslot[10]
                item.itemslotfoot[10] = item.assignmentinvslot[11]
                item.itemslotfoot[11] = item.assignmentinvslot[12]
                item.itemslotfoot[12] = item.assignmentinvslot[13]
                item.itemslotfoot[13] = item.assignmentinvslot[14]
                item.itemslotfoot[14] = item.assignmentinvslot[15]
                item.itemslotfoot[15] = item.assignmentinvslot[16]
                item.itemslotfoot[16] = item.assignmentinvslot[17]
                item.itemslotfoot[17] = item.assignmentinvslot[18]
                item.itemslotfoot[18] = item.assignmentinvslot[19]
                item.itemslotfoot[19] = item.assignmentinvslot[20]
                item.itemslotfoot[20] = item.assignmentinvslot[21]  
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            if item.inventoryslot10[5] == 'armoracc':
                if item.itemslotacc1[0] == 0:    
                    item.itemslotacc1[0] = item.assignmentinvslot[0]
                    item.itemslotacc1[1] = item.assignmentinvslot[2]
                    item.itemslotacc1[2] = item.assignmentinvslot[3]
                    item.itemslotacc1[3] = item.assignmentinvslot[4]
                    item.itemslotacc1[4] = item.assignmentinvslot[5]
                    item.itemslotacc1[5] = item.assignmentinvslot[6]
                    item.itemslotacc1[6] = item.assignmentinvslot[7]
                    item.itemslotacc1[7] = item.assignmentinvslot[8]
                    item.itemslotacc1[8] = item.assignmentinvslot[9]
                    item.itemslotacc1[9] = item.assignmentinvslot[10]
                    item.itemslotacc1[10] = item.assignmentinvslot[11]
                    item.itemslotacc1[11] = item.assignmentinvslot[12]
                    item.itemslotacc1[12] = item.assignmentinvslot[13]
                    item.itemslotacc1[13] = item.assignmentinvslot[14]
                    item.itemslotacc1[14] = item.assignmentinvslot[15]
                    item.itemslotacc1[15] = item.assignmentinvslot[16]
                    item.itemslotacc1[16] = item.assignmentinvslot[17]
                    item.itemslotacc1[17] = item.assignmentinvslot[18]
                    item.itemslotacc1[18] = item.assignmentinvslot[19]
                    item.itemslotacc1[19] = item.assignmentinvslot[20]
                    item.itemslotacc1[20] = item.assignmentinvslot[21]
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] == 0):
                    item.itemslotacc2[0] = item.assignmentinvslot[0]
                    item.itemslotacc2[1] = item.assignmentinvslot[2]
                    item.itemslotacc2[2] = item.assignmentinvslot[3]
                    item.itemslotacc2[3] = item.assignmentinvslot[4]
                    item.itemslotacc2[4] = item.assignmentinvslot[5]
                    item.itemslotacc2[5] = item.assignmentinvslot[6]
                    item.itemslotacc2[6] = item.assignmentinvslot[7]
                    item.itemslotacc2[7] = item.assignmentinvslot[8]
                    item.itemslotacc2[8] = item.assignmentinvslot[9]
                    item.itemslotacc2[9] = item.assignmentinvslot[10]
                    item.itemslotacc2[10] = item.assignmentinvslot[11]
                    item.itemslotacc2[11] = item.assignmentinvslot[12]
                    item.itemslotacc2[12] = item.assignmentinvslot[13]
                    item.itemslotacc2[13] = item.assignmentinvslot[14]
                    item.itemslotacc2[14] = item.assignmentinvslot[15]
                    item.itemslotacc2[15] = item.assignmentinvslot[16]
                    item.itemslotacc2[16] = item.assignmentinvslot[17]
                    item.itemslotacc2[17] = item.assignmentinvslot[18]
                    item.itemslotacc2[18] = item.assignmentinvslot[19]
                    item.itemslotacc2[19] = item.assignmentinvslot[20]
                    item.itemslotacc2[20] = item.assignmentinvslot[21]
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] == 0):
                    item.itemslotacc3[0] = item.assignmentinvslot[0]
                    item.itemslotacc3[1] = item.assignmentinvslot[2]
                    item.itemslotacc3[2] = item.assignmentinvslot[3]
                    item.itemslotacc3[3] = item.assignmentinvslot[4]
                    item.itemslotacc3[4] = item.assignmentinvslot[5]
                    item.itemslotacc3[5] = item.assignmentinvslot[6]
                    item.itemslotacc3[6] = item.assignmentinvslot[7]
                    item.itemslotacc3[7] = item.assignmentinvslot[8]
                    item.itemslotacc3[8] = item.assignmentinvslot[9]
                    item.itemslotacc3[9] = item.assignmentinvslot[10]
                    item.itemslotacc3[10] = item.assignmentinvslot[11]
                    item.itemslotacc3[11] = item.assignmentinvslot[12]
                    item.itemslotacc3[12] = item.assignmentinvslot[13]
                    item.itemslotacc3[13] = item.assignmentinvslot[14]
                    item.itemslotacc3[14] = item.assignmentinvslot[15]
                    item.itemslotacc3[15] = item.assignmentinvslot[16]
                    item.itemslotacc3[16] = item.assignmentinvslot[17]
                    item.itemslotacc3[17] = item.assignmentinvslot[18]
                    item.itemslotacc3[18] = item.assignmentinvslot[19]
                    item.itemslotacc3[19] = item.assignmentinvslot[20]
                    item.itemslotacc3[20] = item.assignmentinvslot[21]      
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotacc1[0] != 0) and (item.itemslotacc2[0] != 0) and (item.itemslotacc3[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na akcesoria są w użyciu')
            if item.inventoryslot10[5] == 'armoractive': 
                if (item.itemslotactive1[0] == 0):
                    item.itemslotactive1[0] = item.assignmentinvslot[0]
                    item.itemslotactive1[1] = item.assignmentinvslot[2]
                    item.itemslotactive1[2] = item.assignmentinvslot[3]
                    item.itemslotactive1[3] = item.assignmentinvslot[4]
                    item.itemslotactive1[4] = item.assignmentinvslot[5]
                    item.itemslotactive1[5] = item.assignmentinvslot[6]
                    item.itemslotactive1[6] = item.assignmentinvslot[7]
                    item.itemslotactive1[7] = item.assignmentinvslot[8]
                    item.itemslotactive1[8] = item.assignmentinvslot[9]
                    item.itemslotactive1[9] = item.assignmentinvslot[10]
                    item.itemslotactive1[10] = item.assignmentinvslot[11]
                    item.itemslotactive1[11] = item.assignmentinvslot[12]
                    item.itemslotactive1[12] = item.assignmentinvslot[13]
                    item.itemslotactive1[13] = item.assignmentinvslot[14]
                    item.itemslotactive1[14] = item.assignmentinvslot[15]
                    item.itemslotactive1[15] = item.assignmentinvslot[16]
                    item.itemslotactive1[16] = item.assignmentinvslot[17]
                    item.itemslotactive1[17] = item.assignmentinvslot[18]
                    item.itemslotactive1[18] = item.assignmentinvslot[19]
                    item.itemslotactive1[19] = item.assignmentinvslot[20]
                    item.itemslotactive1[20] = item.assignmentinvslot[21]   
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] == 0):
                    item.itemslotactive2[0] = item.assignmentinvslot[0]
                    item.itemslotactive2[1] = item.assignmentinvslot[2]
                    item.itemslotactive2[2] = item.assignmentinvslot[3]
                    item.itemslotactive2[3] = item.assignmentinvslot[4]
                    item.itemslotactive2[4] = item.assignmentinvslot[5]
                    item.itemslotactive2[5] = item.assignmentinvslot[6]
                    item.itemslotactive2[6] = item.assignmentinvslot[7]
                    item.itemslotactive2[7] = item.assignmentinvslot[8]
                    item.itemslotactive2[8] = item.assignmentinvslot[9]
                    item.itemslotactive2[9] = item.assignmentinvslot[10]
                    item.itemslotactive2[10] = item.assignmentinvslot[11]
                    item.itemslotactive2[11] = item.assignmentinvslot[12]
                    item.itemslotactive2[12] = item.assignmentinvslot[13]
                    item.itemslotactive2[13] = item.assignmentinvslot[14]
                    item.itemslotactive2[14] = item.assignmentinvslot[15]
                    item.itemslotactive2[15] = item.assignmentinvslot[16]
                    item.itemslotactive2[16] = item.assignmentinvslot[17]
                    item.itemslotactive2[17] = item.assignmentinvslot[18]
                    item.itemslotactive2[18] = item.assignmentinvslot[19]
                    item.itemslotactive2[19] = item.assignmentinvslot[20]
                    item.itemslotactive2[20] = item.assignmentinvslot[21]    
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] == 0):
                    item.itemslotactive3[0] = item.assignmentinvslot[0]
                    item.itemslotactive3[1] = item.assignmentinvslot[2]
                    item.itemslotactive3[2] = item.assignmentinvslot[3]
                    item.itemslotactive3[3] = item.assignmentinvslot[4]
                    item.itemslotactive3[4] = item.assignmentinvslot[5]
                    item.itemslotactive3[5] = item.assignmentinvslot[6]
                    item.itemslotactive3[6] = item.assignmentinvslot[7]
                    item.itemslotactive3[7] = item.assignmentinvslot[8]
                    item.itemslotactive3[8] = item.assignmentinvslot[9]
                    item.itemslotactive3[9] = item.assignmentinvslot[10]
                    item.itemslotactive3[10] = item.assignmentinvslot[11]
                    item.itemslotactive3[11] = item.assignmentinvslot[12]
                    item.itemslotactive3[12] = item.assignmentinvslot[13]
                    item.itemslotactive3[13] = item.assignmentinvslot[14]
                    item.itemslotactive3[14] = item.assignmentinvslot[15]
                    item.itemslotactive3[15] = item.assignmentinvslot[16]
                    item.itemslotactive3[16] = item.assignmentinvslot[17]
                    item.itemslotactive3[17] = item.assignmentinvslot[18]
                    item.itemslotactive3[18] = item.assignmentinvslot[19]
                    item.itemslotactive3[19] = item.assignmentinvslot[20]
                    item.itemslotactive3[20] = item.assignmentinvslot[21]     
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] == 0):
                    item.itemslotactive4[0] = item.assignmentinvslot[0]
                    item.itemslotactive4[1] = item.assignmentinvslot[2]
                    item.itemslotactive4[2] = item.assignmentinvslot[3]
                    item.itemslotactive4[3] = item.assignmentinvslot[4]
                    item.itemslotactive4[4] = item.assignmentinvslot[5]
                    item.itemslotactive4[5] = item.assignmentinvslot[6]
                    item.itemslotactive4[6] = item.assignmentinvslot[7]
                    item.itemslotactive4[7] = item.assignmentinvslot[8]
                    item.itemslotactive4[8] = item.assignmentinvslot[9]
                    item.itemslotactive4[9] = item.assignmentinvslot[10]
                    item.itemslotactive4[10] = item.assignmentinvslot[11]
                    item.itemslotactive4[11] = item.assignmentinvslot[12]
                    item.itemslotactive4[12] = item.assignmentinvslot[13]
                    item.itemslotactive4[13] = item.assignmentinvslot[14]
                    item.itemslotactive4[14] = item.assignmentinvslot[15]
                    item.itemslotactive4[15] = item.assignmentinvslot[16]
                    item.itemslotactive4[16] = item.assignmentinvslot[17]
                    item.itemslotactive4[17] = item.assignmentinvslot[18]
                    item.itemslotactive4[18] = item.assignmentinvslot[19]
                    item.itemslotactive4[19] = item.assignmentinvslot[20]
                    item.itemslotactive4[20] = item.assignmentinvslot[21] 
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] == 0):
                    item.itemslotactive5[0] = item.assignmentinvslot[0]
                    item.itemslotactive5[1] = item.assignmentinvslot[2]
                    item.itemslotactive5[2] = item.assignmentinvslot[3]
                    item.itemslotactive5[3] = item.assignmentinvslot[4]
                    item.itemslotactive5[4] = item.assignmentinvslot[5]
                    item.itemslotactive5[5] = item.assignmentinvslot[6]
                    item.itemslotactive5[6] = item.assignmentinvslot[7]
                    item.itemslotactive5[7] = item.assignmentinvslot[8]
                    item.itemslotactive5[8] = item.assignmentinvslot[9]
                    item.itemslotactive5[9] = item.assignmentinvslot[10]
                    item.itemslotactive5[10] = item.assignmentinvslot[11]
                    item.itemslotactive5[11] = item.assignmentinvslot[12]
                    item.itemslotactive5[12] = item.assignmentinvslot[13]
                    item.itemslotactive5[13] = item.assignmentinvslot[14]
                    item.itemslotactive5[14] = item.assignmentinvslot[15]
                    item.itemslotactive5[15] = item.assignmentinvslot[16]
                    item.itemslotactive5[16] = item.assignmentinvslot[17]
                    item.itemslotactive5[17] = item.assignmentinvslot[18]
                    item.itemslotactive5[18] = item.assignmentinvslot[19]
                    item.itemslotactive5[19] = item.assignmentinvslot[20]
                    item.itemslotactive5[20] = item.assignmentinvslot[21]  
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] == 0):
                    item.itemslotactive6[0] = item.assignmentinvslot[0]
                    item.itemslotactive6[1] = item.assignmentinvslot[2]
                    item.itemslotactive6[2] = item.assignmentinvslot[3]
                    item.itemslotactive6[3] = item.assignmentinvslot[4]
                    item.itemslotactive6[4] = item.assignmentinvslot[5]
                    item.itemslotactive6[5] = item.assignmentinvslot[6]
                    item.itemslotactive6[6] = item.assignmentinvslot[7]
                    item.itemslotactive6[7] = item.assignmentinvslot[8]
                    item.itemslotactive6[8] = item.assignmentinvslot[9]
                    item.itemslotactive6[9] = item.assignmentinvslot[10]
                    item.itemslotactive6[10] = item.assignmentinvslot[11]
                    item.itemslotactive6[11] = item.assignmentinvslot[12]
                    item.itemslotactive6[12] = item.assignmentinvslot[13]
                    item.itemslotactive6[13] = item.assignmentinvslot[14]
                    item.itemslotactive6[14] = item.assignmentinvslot[15]
                    item.itemslotactive6[15] = item.assignmentinvslot[16]
                    item.itemslotactive6[16] = item.assignmentinvslot[17]
                    item.itemslotactive6[17] = item.assignmentinvslot[18]
                    item.itemslotactive6[18] = item.assignmentinvslot[19]
                    item.itemslotactive6[19] = item.assignmentinvslot[20]
                    item.itemslotactive6[20] = item.assignmentinvslot[21]   
                    item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                if (item.itemslotactive1[0] != 0) and (item.itemslotactive2[0] != 0) and (item.itemslotactive3[0] != 0) and (item.itemslotactive4[0] != 0) and (item.itemslotactive5[0] != 0) and (item.itemslotactive6[0] != 0):
                    print('Nie można założyć przedmiotu, ponieważ wszystkie sloty na przedmioty aktywne są w użyciu')

                                        
                                                                                                                                                                                                           
    if lookforinv == "armoroff": 
        lookforinv = "armor"
        if (item.itemslothead[3] == lookforinv) and (item.itemslothead[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslothead[1]
            item.assignmentinvslot[3] = item.itemslothead[2]
            item.assignmentinvslot[4] = item.itemslothead[3]
            item.assignmentinvslot[5] = item.itemslothead[4]
            item.assignmentinvslot[6] = item.itemslothead[5]
            item.assignmentinvslot[7] = item.itemslothead[6]
            item.assignmentinvslot[8] = item.itemslothead[7]
            item.assignmentinvslot[9] = item.itemslothead[8]
            item.assignmentinvslot[10] = item.itemslothead[9]
            item.assignmentinvslot[11] = item.itemslothead[10]
            item.assignmentinvslot[12] = item.itemslothead[11]
            item.assignmentinvslot[13] = item.itemslothead[12]
            item.assignmentinvslot[14] = item.itemslothead[13]
            item.assignmentinvslot[15] = item.itemslothead[14]
            item.assignmentinvslot[16] = item.itemslothead[15]
            item.assignmentinvslot[17] = item.itemslothead[16]
            item.assignmentinvslot[18] = item.itemslothead[17]
            item.assignmentinvslot[19] = item.itemslothead[18]
            item.assignmentinvslot[20] = item.itemslothead[19]
            item.assignmentinvslot[21] = item.itemslothead[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothead = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotchest[3] == lookforinv) and (item.itemslotchest[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotchest[1]
            item.assignmentinvslot[3] = item.itemslotchest[2]
            item.assignmentinvslot[4] = item.itemslotchest[3]
            item.assignmentinvslot[5] = item.itemslotchest[4]
            item.assignmentinvslot[6] = item.itemslotchest[5]
            item.assignmentinvslot[7] = item.itemslotchest[6]
            item.assignmentinvslot[8] = item.itemslotchest[7]
            item.assignmentinvslot[9] = item.itemslotchest[8]
            item.assignmentinvslot[10] = item.itemslotchest[9]
            item.assignmentinvslot[11] = item.itemslotchest[10]
            item.assignmentinvslot[12] = item.itemslotchest[11]
            item.assignmentinvslot[13] = item.itemslotchest[12]
            item.assignmentinvslot[14] = item.itemslotchest[13]
            item.assignmentinvslot[15] = item.itemslotchest[14]
            item.assignmentinvslot[16] = item.itemslotchest[15]
            item.assignmentinvslot[17] = item.itemslotchest[16]
            item.assignmentinvslot[18] = item.itemslotchest[17]
            item.assignmentinvslot[19] = item.itemslotchest[18]
            item.assignmentinvslot[20] = item.itemslotchest[19]
            item.assignmentinvslot[21] = item.itemslotchest[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotchest = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotarms[3] == lookforinv) and (item.itemslotarms[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotarms[1]
            item.assignmentinvslot[3] = item.itemslotarms[2]
            item.assignmentinvslot[4] = item.itemslotarms[3]
            item.assignmentinvslot[5] = item.itemslotarms[4]
            item.assignmentinvslot[6] = item.itemslotarms[5]
            item.assignmentinvslot[7] = item.itemslotarms[6]
            item.assignmentinvslot[8] = item.itemslotarms[7]
            item.assignmentinvslot[9] = item.itemslotarms[8]
            item.assignmentinvslot[10] = item.itemslotarms[9]
            item.assignmentinvslot[11] = item.itemslotarms[10]
            item.assignmentinvslot[12] = item.itemslotarms[11]
            item.assignmentinvslot[13] = item.itemslotarms[12]
            item.assignmentinvslot[14] = item.itemslotarms[13]
            item.assignmentinvslot[15] = item.itemslotarms[14]
            item.assignmentinvslot[16] = item.itemslotarms[15]
            item.assignmentinvslot[17] = item.itemslotarms[16]
            item.assignmentinvslot[18] = item.itemslotarms[17]
            item.assignmentinvslot[19] = item.itemslotarms[18]
            item.assignmentinvslot[20] = item.itemslotarms[19]
            item.assignmentinvslot[21] = item.itemslotarms[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotarms = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslothands[3] == lookforinv) and (item.itemslothands[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslothands[1]
            item.assignmentinvslot[3] = item.itemslothands[2]
            item.assignmentinvslot[4] = item.itemslothands[3]
            item.assignmentinvslot[5] = item.itemslothands[4]
            item.assignmentinvslot[6] = item.itemslothands[5]
            item.assignmentinvslot[7] = item.itemslothands[6]
            item.assignmentinvslot[8] = item.itemslothands[7]
            item.assignmentinvslot[9] = item.itemslothands[8]
            item.assignmentinvslot[10] = item.itemslothands[9]
            item.assignmentinvslot[11] = item.itemslothands[10]
            item.assignmentinvslot[12] = item.itemslothands[11]
            item.assignmentinvslot[13] = item.itemslothands[12]
            item.assignmentinvslot[14] = item.itemslothands[13]
            item.assignmentinvslot[15] = item.itemslothands[14]
            item.assignmentinvslot[16] = item.itemslothands[15]
            item.assignmentinvslot[17] = item.itemslothands[16]
            item.assignmentinvslot[18] = item.itemslothands[17]
            item.assignmentinvslot[19] = item.itemslothands[18]
            item.assignmentinvslot[20] = item.itemslothands[19]
            item.assignmentinvslot[21] = item.itemslothands[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslothands = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotlegs[3] == lookforinv) and (item.itemslotlegs[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotlegs[1]
            item.assignmentinvslot[3] = item.itemslotlegs[2]
            item.assignmentinvslot[4] = item.itemslotlegs[3]
            item.assignmentinvslot[5] = item.itemslotlegs[4]
            item.assignmentinvslot[6] = item.itemslotlegs[5]
            item.assignmentinvslot[7] = item.itemslotlegs[6]
            item.assignmentinvslot[8] = item.itemslotlegs[7]
            item.assignmentinvslot[9] = item.itemslotlegs[8]
            item.assignmentinvslot[10] = item.itemslotlegs[9]
            item.assignmentinvslot[11] = item.itemslotlegs[10]
            item.assignmentinvslot[12] = item.itemslotlegs[11]
            item.assignmentinvslot[13] = item.itemslotlegs[12]
            item.assignmentinvslot[14] = item.itemslotlegs[13]
            item.assignmentinvslot[15] = item.itemslotlegs[14]
            item.assignmentinvslot[16] = item.itemslotlegs[15]
            item.assignmentinvslot[17] = item.itemslotlegs[16]
            item.assignmentinvslot[18] = item.itemslotlegs[17]
            item.assignmentinvslot[19] = item.itemslotlegs[18]
            item.assignmentinvslot[20] = item.itemslotlegs[19]
            item.assignmentinvslot[21] = item.itemslotlegs[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotlegs = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotfoot[3] == lookforinv) and (item.itemslotfoot[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotfoot[1]
            item.assignmentinvslot[3] = item.itemslotfoot[2]
            item.assignmentinvslot[4] = item.itemslotfoot[3]
            item.assignmentinvslot[5] = item.itemslotfoot[4]
            item.assignmentinvslot[6] = item.itemslotfoot[5]
            item.assignmentinvslot[7] = item.itemslotfoot[6]
            item.assignmentinvslot[8] = item.itemslotfoot[7]
            item.assignmentinvslot[9] = item.itemslotfoot[8]
            item.assignmentinvslot[10] = item.itemslotfoot[9]
            item.assignmentinvslot[11] = item.itemslotfoot[10]
            item.assignmentinvslot[12] = item.itemslotfoot[11]
            item.assignmentinvslot[13] = item.itemslotfoot[12]
            item.assignmentinvslot[14] = item.itemslotfoot[13]
            item.assignmentinvslot[15] = item.itemslotfoot[14]
            item.assignmentinvslot[16] = item.itemslotfoot[15]
            item.assignmentinvslot[17] = item.itemslotfoot[16]
            item.assignmentinvslot[18] = item.itemslotfoot[17]
            item.assignmentinvslot[19] = item.itemslotfoot[18]
            item.assignmentinvslot[20] = item.itemslotfoot[19]
            item.assignmentinvslot[21] = item.itemslotfoot[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotfoot = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotacc1[3] == lookforinv) and (item.itemslotacc1[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc1[1]
            item.assignmentinvslot[3] = item.itemslotacc1[2]
            item.assignmentinvslot[4] = item.itemslotacc1[3]
            item.assignmentinvslot[5] = item.itemslotacc1[4]
            item.assignmentinvslot[6] = item.itemslotacc1[5]
            item.assignmentinvslot[7] = item.itemslotacc1[6]
            item.assignmentinvslot[8] = item.itemslotacc1[7]
            item.assignmentinvslot[9] = item.itemslotacc1[8]
            item.assignmentinvslot[10] = item.itemslotacc1[9]
            item.assignmentinvslot[11] = item.itemslotacc1[10]
            item.assignmentinvslot[12] = item.itemslotacc1[11]
            item.assignmentinvslot[13] = item.itemslotacc1[12]
            item.assignmentinvslot[14] = item.itemslotacc1[13]
            item.assignmentinvslot[15] = item.itemslotacc1[14]
            item.assignmentinvslot[16] = item.itemslotacc1[15]
            item.assignmentinvslot[17] = item.itemslotacc1[16]
            item.assignmentinvslot[18] = item.itemslotacc1[17]
            item.assignmentinvslot[19] = item.itemslotacc1[18]
            item.assignmentinvslot[20] = item.itemslotacc1[19]
            item.assignmentinvslot[21] = item.itemslotacc1[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotacc2[3] == lookforinv) and (item.itemslotacc2[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc2[1]
            item.assignmentinvslot[3] = item.itemslotacc2[2]
            item.assignmentinvslot[4] = item.itemslotacc2[3]
            item.assignmentinvslot[5] = item.itemslotacc2[4]
            item.assignmentinvslot[6] = item.itemslotacc2[5]
            item.assignmentinvslot[7] = item.itemslotacc2[6]
            item.assignmentinvslot[8] = item.itemslotacc2[7]
            item.assignmentinvslot[9] = item.itemslotacc2[8]
            item.assignmentinvslot[10] = item.itemslotacc2[9]
            item.assignmentinvslot[11] = item.itemslotacc2[10]
            item.assignmentinvslot[12] = item.itemslotacc2[11]
            item.assignmentinvslot[13] = item.itemslotacc2[12]
            item.assignmentinvslot[14] = item.itemslotacc2[13]
            item.assignmentinvslot[15] = item.itemslotacc2[14]
            item.assignmentinvslot[16] = item.itemslotacc2[15]
            item.assignmentinvslot[17] = item.itemslotacc2[16]
            item.assignmentinvslot[18] = item.itemslotacc2[17]
            item.assignmentinvslot[19] = item.itemslotacc2[18]
            item.assignmentinvslot[20] = item.itemslotacc2[19]
            item.assignmentinvslot[21] = item.itemslotacc2[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
                    item.assignmentinvslot[0] = 0            
        if (item.itemslotacc3[3] == lookforinv) and (item.itemslotacc3[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotacc3[1]
            item.assignmentinvslot[3] = item.itemslotacc3[2]
            item.assignmentinvslot[4] = item.itemslotacc3[3]
            item.assignmentinvslot[5] = item.itemslotacc3[4]
            item.assignmentinvslot[6] = item.itemslotacc3[5]
            item.assignmentinvslot[7] = item.itemslotacc3[6]
            item.assignmentinvslot[8] = item.itemslotacc3[7]
            item.assignmentinvslot[9] = item.itemslotacc3[8]
            item.assignmentinvslot[10] = item.itemslotacc3[9]
            item.assignmentinvslot[11] = item.itemslotacc3[10]
            item.assignmentinvslot[12] = item.itemslotacc3[11]
            item.assignmentinvslot[13] = item.itemslotacc3[12]
            item.assignmentinvslot[14] = item.itemslotacc3[13]
            item.assignmentinvslot[15] = item.itemslotacc3[14]
            item.assignmentinvslot[16] = item.itemslotacc3[15]
            item.assignmentinvslot[17] = item.itemslotacc3[16]
            item.assignmentinvslot[18] = item.itemslotacc3[17]
            item.assignmentinvslot[19] = item.itemslotacc3[18]
            item.assignmentinvslot[20] = item.itemslotacc3[19]
            item.assignmentinvslot[21] = item.itemslotacc3[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotacc3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive1[3] == lookforinv) and (item.itemslotactive1[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive1[1]
            item.assignmentinvslot[3] = item.itemslotactive1[2]
            item.assignmentinvslot[4] = item.itemslotactive1[3]
            item.assignmentinvslot[5] = item.itemslotactive1[4]
            item.assignmentinvslot[6] = item.itemslotactive1[5]
            item.assignmentinvslot[7] = item.itemslotactive1[6]
            item.assignmentinvslot[8] = item.itemslotactive1[7]
            item.assignmentinvslot[9] = item.itemslotactive1[8]
            item.assignmentinvslot[10] = item.itemslotactive1[9]
            item.assignmentinvslot[11] = item.itemslotactive1[10]
            item.assignmentinvslot[12] = item.itemslotactive1[11]
            item.assignmentinvslot[13] = item.itemslotactive1[12]
            item.assignmentinvslot[14] = item.itemslotactive1[13]
            item.assignmentinvslot[15] = item.itemslotactive1[14]
            item.assignmentinvslot[16] = item.itemslotactive1[15]
            item.assignmentinvslot[17] = item.itemslotactive1[16]
            item.assignmentinvslot[18] = item.itemslotactive1[17]
            item.assignmentinvslot[19] = item.itemslotactive1[18]
            item.assignmentinvslot[20] = item.itemslotactive1[19]
            item.assignmentinvslot[21] = item.itemslotactive1[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive2[3] == lookforinv) and (item.itemslotactive2[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive2[1]
            item.assignmentinvslot[3] = item.itemslotactive2[2]
            item.assignmentinvslot[4] = item.itemslotactive2[3]
            item.assignmentinvslot[5] = item.itemslotactive2[4]
            item.assignmentinvslot[6] = item.itemslotactive2[5]
            item.assignmentinvslot[7] = item.itemslotactive2[6]
            item.assignmentinvslot[8] = item.itemslotactive2[7]
            item.assignmentinvslot[9] = item.itemslotactive2[8]
            item.assignmentinvslot[10] = item.itemslotactive2[9]
            item.assignmentinvslot[11] = item.itemslotactive2[10]
            item.assignmentinvslot[12] = item.itemslotactive2[11]
            item.assignmentinvslot[13] = item.itemslotactive2[12]
            item.assignmentinvslot[14] = item.itemslotactive2[13]
            item.assignmentinvslot[15] = item.itemslotactive2[14]
            item.assignmentinvslot[16] = item.itemslotactive2[15]
            item.assignmentinvslot[17] = item.itemslotactive2[16]
            item.assignmentinvslot[18] = item.itemslotactive2[17]
            item.assignmentinvslot[19] = item.itemslotactive2[18]
            item.assignmentinvslot[20] = item.itemslotactive2[19]
            item.assignmentinvslot[21] = item.itemslotactive2[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive3[3] == lookforinv) and (item.itemslotactive3[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive3[1]
            item.assignmentinvslot[3] = item.itemslotactive3[2]
            item.assignmentinvslot[4] = item.itemslotactive3[3]
            item.assignmentinvslot[5] = item.itemslotactive3[4]
            item.assignmentinvslot[6] = item.itemslotactive3[5]
            item.assignmentinvslot[7] = item.itemslotactive3[6]
            item.assignmentinvslot[8] = item.itemslotactive3[7]
            item.assignmentinvslot[9] = item.itemslotactive3[8]
            item.assignmentinvslot[10] = item.itemslotactive3[9]
            item.assignmentinvslot[11] = item.itemslotactive3[10]
            item.assignmentinvslot[12] = item.itemslotactive3[11]
            item.assignmentinvslot[13] = item.itemslotactive3[12]
            item.assignmentinvslot[14] = item.itemslotactive3[13]
            item.assignmentinvslot[15] = item.itemslotactive3[14]
            item.assignmentinvslot[16] = item.itemslotactive3[15]
            item.assignmentinvslot[17] = item.itemslotactive3[16]
            item.assignmentinvslot[18] = item.itemslotactive3[17]
            item.assignmentinvslot[19] = item.itemslotactive3[18]
            item.assignmentinvslot[20] = item.itemslotactive3[19]
            item.assignmentinvslot[21] = item.itemslotactive3[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive3 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive4[3] == lookforinv) and (item.itemslotactive4[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive4[1]
            item.assignmentinvslot[3] = item.itemslotactive4[2]
            item.assignmentinvslot[4] = item.itemslotactive4[3]
            item.assignmentinvslot[5] = item.itemslotactive4[4]
            item.assignmentinvslot[6] = item.itemslotactive4[5]
            item.assignmentinvslot[7] = item.itemslotactive4[6]
            item.assignmentinvslot[8] = item.itemslotactive4[7]
            item.assignmentinvslot[9] = item.itemslotactive4[8]
            item.assignmentinvslot[10] = item.itemslotactive4[9]
            item.assignmentinvslot[11] = item.itemslotactive4[10]
            item.assignmentinvslot[12] = item.itemslotactive4[11]
            item.assignmentinvslot[13] = item.itemslotactive4[12]
            item.assignmentinvslot[14] = item.itemslotactive4[13]
            item.assignmentinvslot[15] = item.itemslotactive4[14]
            item.assignmentinvslot[16] = item.itemslotactive4[15]
            item.assignmentinvslot[17] = item.itemslotactive4[16]
            item.assignmentinvslot[18] = item.itemslotactive4[17]
            item.assignmentinvslot[19] = item.itemslotactive4[18]
            item.assignmentinvslot[20] = item.itemslotactive4[19]
            item.assignmentinvslot[21] = item.itemslotactive4[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive4 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive5[3] == lookforinv) and (item.itemslotactive5[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive5[1]
            item.assignmentinvslot[3] = item.itemslotactive5[2]
            item.assignmentinvslot[4] = item.itemslotactive5[3]
            item.assignmentinvslot[5] = item.itemslotactive5[4]
            item.assignmentinvslot[6] = item.itemslotactive5[5]
            item.assignmentinvslot[7] = item.itemslotactive5[6]
            item.assignmentinvslot[8] = item.itemslotactive5[7]
            item.assignmentinvslot[9] = item.itemslotactive5[8]
            item.assignmentinvslot[10] = item.itemslotactive5[9]
            item.assignmentinvslot[11] = item.itemslotactive5[10]
            item.assignmentinvslot[12] = item.itemslotactive5[11]
            item.assignmentinvslot[13] = item.itemslotactive5[12]
            item.assignmentinvslot[14] = item.itemslotactive5[13]
            item.assignmentinvslot[15] = item.itemslotactive5[14]
            item.assignmentinvslot[16] = item.itemslotactive5[15]
            item.assignmentinvslot[17] = item.itemslotactive5[16]
            item.assignmentinvslot[18] = item.itemslotactive5[17]
            item.assignmentinvslot[19] = item.itemslotactive5[18]
            item.assignmentinvslot[20] = item.itemslotactive5[19]
            item.assignmentinvslot[21] = item.itemslotactive5[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive5 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        if (item.itemslotactive6[3] == lookforinv) and (item.itemslotactive6[1] == ActionInput):
            item.assignmentinvslot[0] = 1
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotactive6[1]
            item.assignmentinvslot[3] = item.itemslotactive6[2]
            item.assignmentinvslot[4] = item.itemslotactive6[3]
            item.assignmentinvslot[5] = item.itemslotactive6[4]
            item.assignmentinvslot[6] = item.itemslotactive6[5]
            item.assignmentinvslot[7] = item.itemslotactive6[6]
            item.assignmentinvslot[8] = item.itemslotactive6[7]
            item.assignmentinvslot[9] = item.itemslotactive6[8]
            item.assignmentinvslot[10] = item.itemslotactive6[9]
            item.assignmentinvslot[11] = item.itemslotactive6[10]
            item.assignmentinvslot[12] = item.itemslotactive6[11]
            item.assignmentinvslot[13] = item.itemslotactive6[12]
            item.assignmentinvslot[14] = item.itemslotactive6[13]
            item.assignmentinvslot[15] = item.itemslotactive6[14]
            item.assignmentinvslot[16] = item.itemslotactive6[15]
            item.assignmentinvslot[17] = item.itemslotactive6[16]
            item.assignmentinvslot[18] = item.itemslotactive6[17]
            item.assignmentinvslot[19] = item.itemslotactive6[18]
            item.assignmentinvslot[20] = item.itemslotactive6[19]
            item.assignmentinvslot[21] = item.itemslotactive6[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        item.inventoryslot1[0] = 1
                        return item
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotactive6 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        
    if lookforinv == "weapon": #do zrobienia
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot1
            if item.inventoryslot1[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot2
            if item.inventoryslot2[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot3
            if item.inventoryslot3[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot4
            if item.inventoryslot4[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot5
            if item.inventoryslot5[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot6
            if item.inventoryslot6[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot7
            if item.inventoryslot7[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot8
            if item.inventoryslot8[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot9
            if item.inventoryslot9[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot10
            if item.inventoryslot10[4] == 'weapon':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]     
        lookforinv == "offhand"
        if (item.inventoryslot1[4] == lookforinv) and (item.inventoryslot1[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot1
            if item.inventoryslot1[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot1 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot2[4] == lookforinv) and (item.inventoryslot2[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot2
            if item.inventoryslot2[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot2 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot3[4] == lookforinv) and (item.inventoryslot3[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot3
            if item.inventoryslot3[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot3 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot4[4] == lookforinv) and (item.inventoryslot4[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot4
            if item.inventoryslot4[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot4 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot5[4] == lookforinv) and (item.inventoryslot5[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot5
            if item.inventoryslot5[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot5 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot6[4] == lookforinv) and (item.inventoryslot6[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot6
            if item.inventoryslot6[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot6 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot7[4] == lookforinv) and (item.inventoryslot7[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot7
            if item.inventoryslot7[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot7 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot8[4] == lookforinv) and (item.inventoryslot8[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot8
            if item.inventoryslot8[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot8 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot9[4] == lookforinv) and (item.inventoryslot9[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot9
            if item.inventoryslot9[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot9 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        if (item.inventoryslot10[4] == lookforinv) and (item.inventoryslot10[2] == ActionInput):
            item.assignmentinvslot = item.inventoryslot10
            if item.inventoryslot10[4] == 'offhand':
                item.itemslotweapon1[0] = item.assignmentinvslot[0]
                item.itemslotweapon1[1] = item.assignmentinvslot[2]
                item.itemslotweapon1[2] = item.assignmentinvslot[3]
                item.itemslotweapon1[3] = item.assignmentinvslot[4]
                item.itemslotweapon1[4] = item.assignmentinvslot[5]
                item.itemslotweapon1[5] = item.assignmentinvslot[6]
                item.itemslotweapon1[6] = item.assignmentinvslot[7]
                item.itemslotweapon1[7] = item.assignmentinvslot[8]
                item.itemslotweapon1[8] = item.assignmentinvslot[9]
                item.itemslotweapon1[9] = item.assignmentinvslot[10]
                item.itemslotweapon1[10] = item.assignmentinvslot[11]
                item.itemslotweapon1[11] = item.assignmentinvslot[12]
                item.itemslotweapon1[12] = item.assignmentinvslot[13]
                item.itemslotweapon1[13] = item.assignmentinvslot[14]
                item.itemslotweapon1[14] = item.assignmentinvslot[15]
                item.itemslotweapon1[15] = item.assignmentinvslot[16]
                item.itemslotweapon1[16] = item.assignmentinvslot[17]
                item.itemslotweapon1[17] = item.assignmentinvslot[18]
                item.itemslotweapon1[18] = item.assignmentinvslot[19]
                item.itemslotweapon1[19] = item.assignmentinvslot[20]
                item.itemslotweapon1[20] = item.assignmentinvslot[21]
                item.inventoryslot10 = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        
    if lookforinv == "weaponoff":
        lookforinv = "weapon"
        if (item.itemslotweapon1[3] == lookforinv) and (item.itemslotweapon1[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotweapon1[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotweapon1[1]
            item.assignmentinvslot[3] = item.itemslotweapon1[2]
            item.assignmentinvslot[4] = item.itemslotweapon1[3]
            item.assignmentinvslot[5] = item.itemslotweapon1[4]
            item.assignmentinvslot[6] = item.itemslotweapon1[5]
            item.assignmentinvslot[7] = item.itemslotweapon1[6]
            item.assignmentinvslot[8] = item.itemslotweapon1[7]
            item.assignmentinvslot[9] = item.itemslotweapon1[8]
            item.assignmentinvslot[10] = item.itemslotweapon1[9]
            item.assignmentinvslot[11] = item.itemslotweapon1[10]
            item.assignmentinvslot[12] = item.itemslotweapon1[11]
            item.assignmentinvslot[13] = item.itemslotweapon1[12]
            item.assignmentinvslot[14] = item.itemslotweapon1[13]
            item.assignmentinvslot[15] = item.itemslotweapon1[14]
            item.assignmentinvslot[16] = item.itemslotweapon1[15]
            item.assignmentinvslot[17] = item.itemslotweapon1[16]
            item.assignmentinvslot[18] = item.itemslotweapon1[17]
            item.assignmentinvslot[19] = item.itemslotweapon1[18]
            item.assignmentinvslot[20] = item.itemslotweapon1[19]
            item.assignmentinvslot[21] = item.itemslotweapon1[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon1 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
        lookforinv = "offhand"
        if (item.itemslotweapon2[3] == lookforinv) and (item.itemslotweapon2[1] == ActionInput):
            item.assignmentinvslot[0] = item.itemslotweapon2[0]
            item.assignmentinvslot[1] = 1
            item.assignmentinvslot[2] = item.itemslotweapon2[1]
            item.assignmentinvslot[3] = item.itemslotweapon2[2]
            item.assignmentinvslot[4] = item.itemslotweapon2[3]
            item.assignmentinvslot[5] = item.itemslotweapon2[4]
            item.assignmentinvslot[6] = item.itemslotweapon2[5]
            item.assignmentinvslot[7] = item.itemslotweapon2[6]
            item.assignmentinvslot[8] = item.itemslotweapon2[7]
            item.assignmentinvslot[9] = item.itemslotweapon2[8]
            item.assignmentinvslot[10] = item.itemslotweapon2[9]
            item.assignmentinvslot[11] = item.itemslotweapon2[10]
            item.assignmentinvslot[12] = item.itemslotweapon2[11]
            item.assignmentinvslot[13] = item.itemslotweapon2[12]
            item.assignmentinvslot[14] = item.itemslotweapon2[13]
            item.assignmentinvslot[15] = item.itemslotweapon2[14]
            item.assignmentinvslot[16] = item.itemslotweapon2[15]
            item.assignmentinvslot[17] = item.itemslotweapon2[16]
            item.assignmentinvslot[18] = item.itemslotweapon2[17]
            item.assignmentinvslot[19] = item.itemslotweapon2[18]
            item.assignmentinvslot[20] = item.itemslotweapon2[19]
            item.assignmentinvslot[21] = item.itemslotweapon2[20]
            while item.assignmentinvslot[0] == 1:
                print("Do jakiego slotu w ekwipunku chcesz odłożyć ten przedmiot? (1-10, 0 aby anulować)")
                odp1 = int(input())
                if odp1 == 1:
                    if item.inventoryslot1[0] == 0:
                        item.inventoryslot1 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot1[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 2:
                    if item.inventoryslot2[0] == 0:
                        item.inventoryslot2 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot2[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 3:
                    if item.inventoryslot3[0] == 0:
                        item.inventoryslot3 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot3[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 4:
                    if item.inventoryslot4[0] == 0:
                        item.inventoryslot4 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot4[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 5:
                    if item.inventoryslot5[0] == 0:
                        item.inventoryslot5 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot5[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 6:
                    if item.inventoryslot6[0] == 0:
                        item.inventoryslot6 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot6[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 7:
                    if item.inventoryslot7[0] == 0:
                        item.inventoryslot7 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot7[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 8:
                    if item.inventoryslot8[0] == 0:
                        item.inventoryslot8 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot8[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 9:
                    if item.inventoryslot9[0] == 0:
                        item.inventoryslot9 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot9[0] == 1:
                        print("Wybrany slot jest już zajęty!")
                if odp1 == 10:
                    if item.inventoryslot10[0] == 0:
                        item.inventoryslot10 = item.assignmentinvslot
                        item.assignmentinvslot[0] = 0
                        item.itemslotweapon2 = [0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if item.inventoryslot10[0] == 1:
                        print("Wybrany slot jest już zajęty!")  
                if odp1 == 0:
                    print("...")
                    item.assignmentinvslot[0] = 0
                    
                                                           
                            
    return item
def lookforinvtype(ActionInput):
    if ActionInput == "ekwipunek":
        lookfornamesinv(item)
        lookforuseditems(item)
        lookforwornitems(item)
        print('')
        
def lookfornamesinv(item):
    print("Twój Ekwipunek:")
    if item.inventoryslot1[0] != 0:
        print(item.inventoryslot1[1], item.inventoryslot1[2])
    if item.inventoryslot2[0] != 0:
        print(item.inventoryslot2[1], item.inventoryslot2[2])
    if item.inventoryslot3[0] != 0:
        print(item.inventoryslot3[1], item.inventoryslot3[2])
    if item.inventoryslot4[0] != 0:
        print(item.inventoryslot4[1], item.inventoryslot4[2])
    if item.inventoryslot5[0] != 0:
        print(item.inventoryslot5[1], item.inventoryslot5[2])
    if item.inventoryslot6[0] != 0:
        print(item.inventoryslot6[1], item.inventoryslot6[2])
    if item.inventoryslot7[0] != 0:
        print(item.inventoryslot7[1], item.inventoryslot7[2])
    if item.inventoryslot8[0] != 0:
        print(item.inventoryslot8[1], item.inventoryslot8[2])
    if item.inventoryslot9[0] != 0:
        print(item.inventoryslot9[1], item.inventoryslot9[2])
    if item.inventoryslot10[0] != 0:
        print(item.inventoryslot10[1], item.inventoryslot10[2])
def lookforuseditems(item):
    print("Twój Oręż i Używane Przedmioty:")
    if item.itemslotweapon1[0] != 0:
        print(item.itemslotweapon1[1])
    if item.itemslotweapon2[0] != 0:
        print(item.itemslotweapon2[1])
    if item.itemslotactive1[0] != 0:
        print(item.itemslotactive1[1])
    if item.itemslotactive2[0] != 0:
        print(item.itemslotactive2[1])
    if item.itemslotactive3[0] != 0:
        print(item.itemslotactive3[1])
    if item.itemslotactive4[0] != 0:
        print(item.itemslotactive4[1])
    if item.itemslotactive5[0] != 0:
        print(item.itemslotactive5[1])
    if item.itemslotactive6[0] != 0:
        print(item.itemslotactive6[1])
def lookforwornitems(item):
    print("Twoja Zbroja i Akcesoria:")
    if item.itemslothead[0] != 0:
        print(item.itemslothead[1])
    if item.itemslotchest[0] != 0:
        print(item.itemslotchest[1])
    if item.itemslotarms[0] != 0:
        print(item.itemslotarms[1])
    if item.itemslothands[0] != 0:
        print(item.itemslothands[1])
    if item.itemslotlegs[0] != 0:
        print(item.itemslotlegs[1])
    if item.itemslotfoot[0] != 0:
        print(item.itemslotfoot[1])
    if item.itemslotacc1[0] != 0:
        print(item.itemslotacc1[1])
    if item.itemslotacc2[0] != 0:
        print(item.itemslotacc2[1])
    if item.itemslotacc3[0] != 0:
        print(item.itemslotacc3[1])
def DebugAdditem(item):
    while True:
        debugassign = [0,0,"","","","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        try:
            print("indeks 0 (istnienie) =")
            debugassign[0] = 1
            print("indeks 1 (ilość) =")
            debugassign[1] = int(input())
            print("indeks 2 (nazwa) =")
            debugassign[2] = str(input())
            print("indeks 3 (opis) =")
            debugassign[3] = str(input())
            print("indeks 4 (typ) =")
            debugassign[4] = str(input())
            print("indeks 5 (podtyp) =")
            debugassign[5] = str(input())
            print("indeks 6 (+hp) =")
            debugassign[6] = 0
            print("indeks 7 (+mp) =")
            debugassign[7] = 0
            print("indeks 8 (maxhp) =")
            debugassign[8] = 0
            print("indeks 9 (maxmp) =")
            debugassign[9] = 0
            print("indeks 10 (+exp) =")
            debugassign[10] = 0
            print("indeks 11 (str) =")
            debugassign[11] = 0
            print("indeks 12 (dex) =")
            debugassign[12] = 0
            print("indeks 13 (int) =")
            debugassign[13] = 0
            print("indeks 14 (end) =")
            debugassign[14] = 0
            print("indeks 15 (luck) =")
            debugassign[15] = 0
            print("indeks 16 (dmg broni) =")
            debugassign[16] = 0
            print("indeks 17 (ID) =")
            debugassign[17] = 0
            print("indeks 18 (obrona przed obr. kłutymi) =")
            debugassign[18] = 0
            print("indeks 19 (obrona przed obr. ciętymi) =")
            debugassign[19] = 0
            print("indeks 20 (obrona przed obr. obuchowymi) =")
            debugassign[20] = 0
            print("indeks 21 (typy obrażeń) =")
            debugassign[21] = 0
            break
        except ValueError:
            print("Coś ci się pomyliło!")
    print("Podaj slot w ekwipunku dla przedmiotu (1-10)")
    debugslotchoice = int(input())
    if debugslotchoice == 1:
        item.inventoryslot1 = debugassign
    if debugslotchoice == 2:
        item.inventoryslot2 = debugassign
    if debugslotchoice == 3:
        item.inventoryslot3 = debugassign
    if debugslotchoice == 4:
        item.inventoryslot4 = debugassign
    if debugslotchoice == 5:
        item.inventoryslot5 = debugassign
    if debugslotchoice == 6:
        item.inventoryslot6 = debugassign
    if debugslotchoice == 7:
        item.inventoryslot7 = debugassign
    if debugslotchoice == 8:
        item.inventoryslot8 = debugassign
    if debugslotchoice == 9:
        item.inventoryslot9 = debugassign
    if debugslotchoice == 10:
        item.inventoryslot10 = debugassign
    return item
    
    
#####EKWIPUNEK#####

#####WYDARZENIA#####
def EventHandler(LocMoveset,item,player,ActionInput,Loc7Moveset):
    if LocMoveset[5] == 1:
        print("Między kamyczkami na dnie widzisz mieniącą się złotą monetę")
        print("Czy chciałbyś ją podnieść? (Tak/Nie)")
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput == "tak":
                item.gold+=1
                print("Podniosłeś złotą monetę")
                print("Dodano: +1 Korona")
                ActionInput = ""
                LocMoveset[5] = 0
                Loc5Moveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print("Postanawaiasz zostawić monetę w spokoju.")
                break
    if LocMoveset[5] == 2:
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput in MovementNorth:
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "tak":
                print("...Mmmm... Cóż za soczysty zapach...")
                time.sleep(3)
                print("Giniesz krótko po tym gdy próbowałeś pocałować ogra.")
                print("Nawet taki zwierzoczłowiek ma jakieś podstawy moralne...")
                time.sleep(3)
                player.HP = 0
                LocMoveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print('Dobry wybór Kmiotku.')
                print("Możesz spokojnie odejść...")
                LocMoveset[5] = 0
                break
    if LocMoveset[5] == 3:
        while ActionInput != "tak" or ActionInput != "nie":
            ActionInput = input().lower()
            if ActionInput in MovementEast:
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "tak":
                print('...Powoli wsadzasz palec w żar...')
                time.sleep(2)
                print('Dziwnym przypadkiem po chwilowym bólu tracisz czucie w palcu...')
                time.sleep(2)
                print('Totalnie przypadkowo twój palec zostaje w ognisku.')
                time.sleep(2)
                strata = random.randint(1,3)
                player.HP -= strata
                print("Straciłeś",strata,"HP!")
                LocMoveset[5] = 0
                return LocMoveset, item, player, ActionInput, MovementAction, Loc5Moveset
            if ActionInput == "nie":
                print('Dobry wybór Kmiotku.')
                print("Możesz spokojnie odejść...")
                LocMoveset[5] = 0
                break
#####WYDARZENIA#####

#####GŁÓWNY MODUŁ#####
akcja=['North','South','East','West','n','s','w','e','Zjedz','Użyj','Opis','Atakuj','Zagadaj']
MovementAction=['north','n','south','s','east','e','west','w']
MovementNorth=['north','n']
MovementSouth=['south','s']
MovementEast=['east','e']
MovementWest=['west','w']
OtherAction=['zjedz','użyj','opis','atakuj','zagadaj', 'ubierz', 'dobądź', 'zdejmij', 'schowaj', 'ekwipunek', 'weź']
ItemAction=['zjedz','użyj','opis','ubierz','dobądź','zdejmij','schowaj','ekwipunek']
DebugAction=['debug','additem']
LocMoveset=[0,0,0,0,0,0]
Loc1Moveset=[2,0,0,0,0,0] #W kolejności North(0)/South(1)/East(2)/West(3)/Wróg w Lokacji(4)/Wydarzenie(5)
Loc2Moveset=[3,0,0,0,0,0]
Loc3Moveset=[0,2,4,9,0,0] #Skrzyżowanie
Loc4Moveset=[5,0,7,3,0,0] #0 = "Tam nie pójdziesz'
Loc5Moveset=[0,4,0,0,0,0] #Strumyk
#Loc6Moveset=[0,0,0,0] #Alternatywna wersja strumyka
Loc7Moveset=[0,8,0,4,0,1]
Loc8Moveset=[7,0,0,0,0,0] #Obóz ogrów w zagajniku
Loc9Moveset=[10,0,3,11,0,0]
Loc10Moveset=[12,9,0,0,0,0]
Loc11Moveset=[0,0,9,0,0,0] #Ognisko w Zagajniku
Loc12Moveset=[14,10,0,0,0,0] #Południowa brama Crosset
#Loc13Moveset=[0,0,0,0] #alternatywna wersja bramy
Loc14Moveset=[19,12,16,15,0,0] #skrzyzowanie crosset
Loc15Moveset=[20,0,14,0,0,0] #ulica pszenna crosset
Loc16Moveset=[17,0,21,14,0,0] #ulica targowa crosset
Loc17Moveset=[0,16,0,0,1,0] #zaułek
#Loc18Moveset=[0,0,0,0] #alternatywny zaułek
Loc19Moveset=[0,14,0,0,0,0] #wieża straznicza crosset
Loc20Moveset=[0,15,0,0,0,0] #piekarnia crosset
Loc21Moveset=[0,0,0,16,0,0] #kuźnia crosset


def ActInput(ActionInput):
    ActionInput = input().lower()
    return ActionInput
def LocMovesetCheck(Lokacja):
    if Lokacja == 1:
        LocMoveset=Loc1Moveset
    if Lokacja == 2:
        LocMoveset=Loc2Moveset
    if Lokacja == 3:
        LocMoveset=Loc3Moveset
    if Lokacja == 4:
        LocMoveset=Loc4Moveset
    if Lokacja == 5:
        LocMoveset=Loc5Moveset
    if Lokacja == 6:
        LocMoveset=Loc6Moveset
    if Lokacja == 7:
        LocMoveset=Loc7Moveset
    if Lokacja == 8:
        LocMoveset=Loc8Moveset
    if Lokacja == 9:
        LocMoveset=Loc9Moveset
    if Lokacja == 10:
        LocMoveset=Loc10Moveset
    if Lokacja == 11:
        LocMoveset=Loc11Moveset
    if Lokacja == 12:
        LocMoveset=Loc12Moveset
    if Lokacja == 13:
        LocMoveset=Loc13Moveset
    if Lokacja == 14:
        LocMoveset=Loc14Moveset
    if Lokacja == 15:
        LocMoveset=Loc15Moveset
    if Lokacja == 16:
        LocMoveset=Loc16Moveset
    if Lokacja == 17:
        LocMoveset=Loc17Moveset
    if Lokacja == 18:
        LocMoveset=Loc18Moveset
    if Lokacja == 19:
        LocMoveset=Loc19Moveset
    if Lokacja == 20:
        LocMoveset=Loc20Moveset
    if Lokacja == 21:
        LocMoveset=Loc21Moveset
    return LocMoveset
    

def ActionCheck(ActionInput,Lokacja,LocMoveset): #nie testowane, powiedzmy że działa
    #print(MovementAction)
    if ActionInput in MovementAction:
        if ActionInput in MovementNorth:
            #print(LocMoveset)
            #print(ActionInput)
            if LocMoveset[0] != 0:
                Lokacja=LocMoveset[0]
                #print(Lokacja)
                #return ActionInput, Lokacja, LocMoveset 
            if LocMoveset[0] == 0:
                print("Tam nie pójdziesz")
                #return ActionInput, Lokacja, LocMoveset
        if ActionInput in MovementSouth:
            if LocMoveset[1] != 0:
                Lokacja=LocMoveset[1]
            if LocMoveset[1] == 0:
                print("Tam nie pójdziesz")
        if ActionInput in MovementEast:
            if LocMoveset[2] != 0:
                Lokacja=LocMoveset[2]
            if LocMoveset[2] == 0:
                print("Tam nie pójdziesz")
        if ActionInput in MovementWest:
            if LocMoveset[3] != 0:
                Lokacja=LocMoveset[3]
            if LocMoveset[3] == 0:
                print("Tam nie pójdziesz")
    if ActionInput in OtherAction:
        if ActionInput in ItemAction:
            print("przeniesione")
    if ActionInput in DebugAction:
        if ActionInput == 'debug':
            print("Jakieś dane tu się będą pokazywać")
        if ActionInput == 'additem':
            DebugAdditem(item)
     #NIŻEJ ZMIENIŁEM or NA and   
    if (ActionInput not in MovementAction) and (ActionInput not in OtherAction) and (ActionInput not in DebugAction) and (ActionInput != "questy"):
        print("???")
    return ActionInput, Lokacja, LocMoveset

#def LocDescCheck(Lokacja):
def LocDescCheck(Lokacja, DaneWszystkichQuestów):
    if Lokacja == 1:
        loc1()
    if Lokacja == 2:
        loc2()
    if Lokacja == 3:
        loc3()
    if Lokacja == 4:
        loc4()
    if Lokacja == 5:
        loc5()
    if Lokacja == 6:
        loc6()
    if Lokacja == 7:
        loc7()
    if Lokacja == 8:
        loc8()
    if Lokacja == 9:
        loc9()
    if Lokacja == 10:
        loc10()
    if Lokacja == 11:
        loc11()
    if Lokacja == 12 and DaneWszystkichQuestów[1][0] == 0:
        DaneWszystkichQuestów[1][0] = 1
        loc13()
        print()
        print('Otrzymano zadanie: Miejscowy Bohater')
        print()
    if Lokacja == 12 and DaneWszystkichQuestów[1][0] == 1 or DaneWszystkichQuestów[1][0] == 3:
        loc12()
    #if Lokacja == 13:
        #loc13()
    if Lokacja == 14:
        loc14()
    if Lokacja == 15:
        loc15()
    if Lokacja == 16:
        loc16()
    if Lokacja == 17:
        loc17()
    if Lokacja == 18:
        loc18()
    if Lokacja == 19:
        loc19()
    if Lokacja == 20:
        loc20()
    if Lokacja == 21:
        loc21()
    return None #nic nie zwraca, tylko generuje opis 
#####GŁÓWNY MODUŁ#####

#####LICZNIK TUR#####
def TurnCounter(Turn):
    Turn = Turn + 1
    return Turn
#####LICZNIK TUR#####
    
clear = "\n" * 100
def clear():
    print(clear)

ActionInput = ""

lookforinv = ''
item = Inventory(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
player = PlayerStats(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
entity = EnemyStats("",0,0,0,0,0)
defineinventory(item)
#Staty = PlayerStats("edgy", 100, 20, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#Staty.PlayerName()
#print(Staty.StatDisplay())
start = 0
Turn = 0
if start == 0:
    print("###############################################################")
    print()
    print("               Mikołaj, Tomek i Gruby prezentują...")
    time.sleep(1)
    print()
    print("                            ZAGAJNIK")
    print()
    time.sleep(1)
    print("###############################################################")
    print()
    print("Nowa Gra   -   Kontynuuj   -   Wczytaj   -   Opcje   -   Wyjdź")
    print()
    print()
while start == 0:
    StartInput = input().lower()
    if StartInput == "nowa gra":
        Lokacja = 1
        start = 1
        xyz = 1
        xxx = ["zbrojny","1","zwiadowca","2","łotr","3"]
        while xyz == 1:
            print("Wybierz swoją klasę...")
            print("Zbrojny (1), zwiadowca (2), łotr (3)...")
            StartInput = input().lower()
            ClassChoice(player,item,StartInput)
            if StartInput in xxx:
                xyz = 0
    if StartInput == "kontynuuj":
        print("Czy na pewno chcesz kontunuować swoje cierpienie?")
    if StartInput == "wczytaj":
        print("Jak zrobisz zapisywanie to pogadamy!")
    if StartInput == "opcje":
        print("Masz dwie opcje: gułag albo śmierć!")
    if StartInput == "wyjdź":
        break
    
    

Lokacja = 1
DaneWszystkichQuestów=Questy()
#print(DaneWszystkichQuestów)
#print()
while Lokacja != 0 and start == 1: #lokacja 0 to GAME OVER
    #LocDescCheck(Lokacja)
    LocDescCheck(Lokacja,DaneWszystkichQuestów)
    LocMoveset=LocMovesetCheck(Lokacja)
    if LocMoveset[4] == 1:
        #ObrażeniaWychodzące(ObrażeniaCięte, ObrażeniaKłute, ObrażeniaObuchowe, player)
        entity = EnemyStats("",1,0,0,0,0)
        entity.ID = 1
        EnemySpawn(entity)
        playerOutputDMG = 3
        LocMoveset[4] = 0
        Loc17Moveset[4] = 0
        FirstBlood(entity,player,playerOutputDMG,Trucizna,Trucizna1)
    if LocMoveset[4] != 0 or LocMoveset[5] != 0:
        EventHandler(LocMoveset,item,player,ActionInput,MovementAction,Loc7Moveset)
        if player.HP <= 0:
            Lokacja = 0
        if ActionInput not in MovementAction:
            ActionInput = input().lower()
    if LocMoveset[5] == 0 and LocMoveset[4] == 0:
        ActionInput = input().lower()
    
    #to zmieniłem i TO JEST KLUCZOWE:
    (ActionInput,Lokacja,LocMoveset)=ActionCheck(ActionInput,Lokacja,LocMoveset)
    if ActionInput == 'zjedz':
        print("Co chciałbyś zjeść?")
        ActionInput = input().lower()
        lookforinv="food"

    if ActionInput == 'użyj':
        print("Co chciałbyś użyć?")
        ActionInput = input().lower()
        lookforinv="consumable"

    if ActionInput == 'opis':
        print("O którym przedmiocie chcesz wiedzieć więcej?")
        ActionInput = input().lower()
        lookforinv="desc"

    if ActionInput == 'ubierz':
        print("Co chciałbyś ubrać na siebię?")
        ActionInput = input().lower()
        lookforinv="armor"

    if ActionInput == 'dobądź':
        print("Jaką broń chciałbyś dobyć?")
        ActionInput = input().lower()
        lookforinv="weapon"

    if ActionInput == 'zdejmij':
        print("Co chciałbyś zdjąć z siebie?")
        ActionInput = input().lower()
        lookforinv="armoroff"

    if ActionInput == 'schowaj':
        print("Jaką broń chciałbyś schować?")
        ActionInput = input().lower()
        lookforinv="weaponoff"

    if ActionInput == 'upuść':
        print("Jaki przedmiot chciałbyś upuścić? Tej akcji nie można cofnąć! (Wybierz przedmiot nie używany przez ciebię)")
        ActionInput = input().lower()

    if ActionInput == 'ekwipunek':
        lookforinvtype(ActionInput)
    #(lookforinv, ActionInput)=itemuse(lookforinv,ActionInput)
    lookforinventory(lookforinv,ActionInput,item)
    lookforinventory(lookforinv,ActionInput,item)
    DaneWszystkichAlkoholi=[]
    DaneWszystkichAlkoholi=Alkohole(DaneWszystkichAlkoholi)
    StopienOdurzenia=()
    StopienOdurzenia = DaneWszystkichAlkoholi[0][1]/player.str or DaneWszystkichAlkoholi[1][1]/player.str or DaneWszystkichAlkoholi[2][1]/player.str
    StopienUzależnienia = DaneWszystkichAlkoholi[0][2]/player.luck*10 or DaneWszystkichAlkoholi[1][2]/player.luck*10 or DaneWszystkichAlkoholi[2][2]/player.luck*10
    Turn=(TurnCounter(Turn))
    if ActionInput == 'questy':
        if DaneWszystkichQuestów[1][0] == 1:
            print()
            print('Nazwa: {}'.format(DaneWszystkichQuestów[1][1]))
            print('Opis: {}'.format(DaneWszystkichQuestów[1][2]))
            print('Zleceniodawca: {}'.format(DaneWszystkichQuestów[1][3]))
        print()
        if DaneWszystkichQuestów[1][0] == 0 or DaneWszystkichQuestów[1][0] == 3:
            print('Nie masz żadnych zadań!')
            print()
    #turazakończenia PROWIZORYCZNIE ustawiona 0 zero...
    #turazakończenia powinna być listą na wypadek gdyby gracz wypił kilka alkoholi
    #albo różne tury zakońćzenia dla różnych substancji
    turazakończenia=0
    (DaneWszystkichAlkoholi, player, StopienOdurzenia, StopienUzależnienia, Turn, turazakończenia)=SprawdzanieAlkoholi(DaneWszystkichAlkoholi,player,StopienOdurzenia, StopienUzależnienia,Turn, turazakończenia)
#StopienOdurzenia
#StopienUzależnienia
#turazakończenia
            
            
            
       
        
            
        

    

    
