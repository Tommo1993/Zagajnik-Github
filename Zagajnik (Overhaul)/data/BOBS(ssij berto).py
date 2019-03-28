
import random
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
    #def calcstats(player):
        #player.MaxHP = player.MaxHPnocalc + player.end
       #player.MaxMP = player.MaxMPnocalc + player.int
        #player.basedamage = player.basedamage + player.str
        #player.weapondamage = player.basedamage + item.WeaponDamage
    def addstats(player):
        if str(input()) == "str":
            player.str = player.str + 1
        if str(input()) == "dex":
            player.dex = player.dex + 1
        if str(input()) == "int":
            player.int = player.int + 1
        if str(input()) == "end":
            player.end = player.end + 1
        if str(input()) == "luck":
            player.luck = player.luck + 1
    def PlayerName(player):
        return 'Twoje imie to {}'.format(player.name)
    def StatDisplay(player):
        return '{} HP, {} MP, {} EXP'.format(player.HP, player.MP, player.EXP)
    def StatDisplay2(player):
        return '{} str, {} dex, {} int, {} end, {} luck'.format(player.str, player.dex, player.int, player.end, player.luck)
#Staty = PlayerStats("Dovahkiin", 100, 20, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#print(Staty.PlayerName())
#print(Staty.StatDisplay())
#print(Staty.StatDisplay2())
class classdefs:
    def Zbrojny(player):
        player.HP = 20
        player.MP = 5
        player.MaxHP = 20
        player.MaxMP = 5
        player.str = 3
        player.dex = 2
        player.int = 1
        player.end = 2
        player.luck = 1
        player.pclass = 1
    def Zwiadowca(player):
        player.HP = 15
        player.MP = 10
        player.MaxHP =15
        player.MaxMP = 10
        player.str = 2
        player.dex = 3
        player.int = 1
        player.end = 1
        player.luck = 1
        player.pclass = 2
    def Adept(player):
        player.HP = 10
        player.MP = 20
        player.MaxHP = 10
        player.MaxMP = 20
        player.str = 1
        player.dex = 2
        player.int = 3
        player.end = 1
        player.luck = 1
        player.pclass = 3			
class EnemyStats:
    def __init__(entity, name, ID, HP, MP, attackdmg, EXPreward):
        entity.name = name
        entity.ID = ID
        entity.HP = HP
        entity.MP = MP
        entity.attackdmg
        entity.EXPreward
def EnemySpawn(entity): #(w systemie): def Łyżeczka Dżemu(ID):
                        #                  ID=1 , itd. 
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





def Występowanie_Przeciwnika(Lokacja,entity):
    #if Lokacja in range(Lokacje przeciwników)
        if entity.ID in range(1,17):
            print (entity.name)
            print ("HP wynosi") + entity.HP
            print ("MP wynosi") + entity.MP
            print()
            print()
            print()
def FirstBlood(entity,player):
    if entity.attackdmg > playerOutputDMG:
        Atak
    if entity.attackdmg < playerOutputDMG:
        WybórPrzeciwnika
    if entity.attackdmg == playerOutputDMG:
        LosAtaku=random.randint(0,2)
        if LosAtaku==1:
            Wybór
        if LosAtaku ==2:
            WybórPrzeciwnika

def Wybór():
    print("Chcesz użyć ATAK, MAGIA, czy UCIECZKA")
    wybór=str(input())
    if wybór == "ATAK":
        Atak
    if wybór == "MAGIA":
        Magia
    #if wybór=="UCIECZKA": (Zamrożony pomysł)
                
def Magia (player,entity):
    print("Co chciałbyś wybrać?")
    print ("(Aby użyć coś innego wpisz WRÓĆ.)")
    Magicstr = str(input())
    Magiclist=["Kula ognia","Wysysanie Życia","Mroźny Podmuch","Berserker","Wstząs","Otrucie"]
    print (Magiclist)
    ManaUse=1
    def KulaOgnia():
        player.MP -= 3
        entity.HP -= 5
        ManaUse=0
        return player, entity, ManaUse
    def WysysanieŻycia():
        player.MP -= 5
        entity.HP -= 2
        player.HP += 2
        ManaUse=0
        return player, entity, ManaUse
    def MroźnyPodmuch():
        player.MP -= 5
        entity.HP -= 4
        ManaUse=0
        return player, entity, ManaUse
    def Berserker():
        player.HP -= 2
        player.MP -= 5
        entity.HP -= 9
        ManaUse=0
        return player, entity, ManaUse
    def Wstrząs():
        player.MP -= 6
        entity.HP -= 4
        entity.MP -= 3
        ManaUse=0
        return player, entity, ManaUse
    def Otrucie():
        player.MP -= 7
        entity.HP -= 3
        ManaUse=0
        return player, entity, ManaUse
    if Magicstr == Magiclist[0]:
        KulaOgnia
    if Magicstr == Magiclist[1]:
        WysysanieŻycia
    if Magicstr == Magiclist[2]:
        MroźnyPodmuch
    if Magicstr == Magiclist[3]:
        Berserker
    if Magicstr == Magiclist[4]:
        Wstrzrąs
    if Magicstr == Magiclist[5]:
        Otrucie
    if Magicstr=="WRÓĆ":
        Wybór
    if Magicstr not in Magiclist and Magicstr != "WRÓĆ":
        print("Chyba coś pomyliłeś.")
        #miejsce celowo pozostawione puste
def MagiaWroga(player,entity):
    # chodzi o to żeby losowało, które
        def KulaOgnia():
            entity.MP -= 3
            player.HP -= 5
            Wybór
            return player,entity
        def WysysanieŻycia():
            entity.MP -= 5
            player.HP -= 2
            entity.HP += 2
            Wybór
            return player,entity
        def MroźnyPodmuch():
            entity.MP -= 5
            player.HP -= 4
            Wybór
            return player,entity
        def Berserker():
            entity.HP -= 2
            entity.MP -= 5
            player.HP -= 9
            Wybór
            return player,entity
        def Wstrząs():
            entity.MP -= 6
            player.HP -= 4
            player.MP -= 3
            Wybór
            return player,entity
        def Otrucie():
            entity.MP -= 7
            player.HP -= 3
            Wybór
            return player, entity
        if Magicstr == Magiclist[0]:
            KulaOgnia
        if Magicstr == Magiclist[1]:
            WysysanieŻycia
        if Magicstr == Magiclist[2]:
            MroźnyPodmuch
        if Magicstr == Magiclist[3]:
            Berserker
        if Magicstr == Magiclist[4]:
            Wstrzrąs
        if Magicstr == Magiclist[5]:
            Otrucie

def DeathStats (player,entity):
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
        AtakPrzeciwnika
    if player.HP<0:
        player.HP=0
    if  player.MP<0:
        player.MP=0
    if player.HP==0:
        print("U n00b")
        Lokacja=0 # śmierdź się zrobi później
    if player.MP==0 and ManaUse==1:
        print("Nie masz many!")
        Wybór
        

def Atak (player,entity):
    Los=random.randint(0,9)
    if Los==1 or Los==2:
        print("DoStaŁ, ALe PrawIE Go NIe ZarYSOwalIŚmY.")
        entity.HP -= 0.2* playerOutputDMG
        WybórPrzeciwnika
    if Los ==3:
        print("Machłeś się i ledwo żeś go trafił.")
        entity.HP-=0.4* playerOutputDMG
        WybórPrzeciwnika
    if Los ==4:
        print("No,no,no... Całkiem, całkiem. ")
        entity.HP-=0.6*playerOutputDMG
        WybórPrzeciwnika
    if Los ==5:
        print("Ała to musiało boleć.")
        entity.HP-=0.8* playerOutputDMG
        WybórPrzeciwnika
    if Los ==6:
        print("Ach jak przyjemnie poczuć czyjąś krew.")
        entity.HP-=playerOutputDMG
        WybórPrzeciwnika
    if Los ==7:
        print("ZDEWASTOWAŁEŚ swojego wroga. Popamięta sobie na zawsze.")
        entity.HP-=1.2*playerOutputDMG
        WybórPrzeciwnika
    if Los==8 or Los==9:
        LosChybienia==random.randint(0,8)
        if LosChybienia==1:
            print("Wróg uskoczył i uderzył cię od boku.")
            player.HP-=2
            WybórPrzeciwnika
        if LosChybienia==8:
            print("Oponent zrobił serię przewrotów ninja po czym uderzył się o parapet.")
            entity.HP-=1
            WybórPrzeciwnika
        if LosChybienia==2:
            print("Ciosy wyprowadza się z nadgarstka, a nie od łokcia.")
            WybórPrzeciwnika
        if LosChybienia==3:
            print("Słońce oślepiło cię swoim jasnym blaskiem i nie zaatakowałeś.")
            WyborPrzeciwnika
        if LosChybienia==4:
            print("Masz kryzys egzystencjalny.")
            WybórPrzeciwnika
        if LosChybienia==5:
            print("Zamiast atakować przeciwnika zacząłeś go obrażać.")
            WybórPrzeciwnika
        if LosChybienia==6:
            print("Przeciwnik uszedł z pola walki ale pojawił się następny łudząco podobny")
            print("do poprzedniego.")
            WybórPrzeciwnika
        if LosChybienia==7:
            print("Począłeś dyplomatyczną konwersację z przeciwnikiem, lecz on nie podzielał ")
            print("twoich pacyfistycznych intencji.")
            WybórPrzeciwnika
def WybórPrzeciwnika(player,entity):
    LosDecWalkiPrzeciwnika=random.randint(0,2)
    if LosDecWalkiPrzeciwnika==1:
        if entity.MP not in range(0,3): #######################
            MagiaWroga
    if LosDecWalkiPrzeciwnika==2:
        AtakPrzeciwnika
def AtakPrzeciwnika(player, entity):
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
        player.HP-=0.2*entity.attackdamage
        Wybór
    if Los2==2:
        print("I to ma być cios?!")
        player.HP-=0.4*entity.attackdamage
        Wybór
    if Los2==3:
        print("Jakoś to zniosę. Bywało gorzej.")
        player.HP-=0.6*entity.attackdamage
        Wybór
    if Los2==4:
        print("Silny skurczybyk jak stu chłopa.")
        player.HP-=0.8*entity.attackdamage
        Wybór
    if Los2==5:
        print("Twój przeciwnik wie jak zrobić, żeby bolało.")
        player.HP-=entity.attackdamage
        Wybór
    if Los2==6:
        print("Brak" + LosOrganów +  "hmmm... To chyba dobrze.")
        player.HP-=1.2*entity.attackdamage
        Wybór
    if Los2==7 or Los2==8:
        LosChybienia2=random.randint(0,7)
        if LosChybienia2==1:
            print("Sprzedałeś przeciwnikiowi psztyczka w nos i wytrąciłeś")
            print("go z równowagi.")
            Wybór
        if LosChybienia2==2:
            print("Przeciwnika zaswędziało coś w nosie i musiał odkichnąć.")
            Wybór
        if LosChybienia2==3:
            print("Oponent zobaczył króliczka, a wiesz że ma do nich słabość.")
            Wybór
        if LosChybienia2==4:
            print("Twój wróg umiejętnością się nie popisał.")
            Wybór
        if LosChybienia2==5:
            print("Niemcy proszę pana.")
            Wybór
        if LosChybienia2==6:
            print("Twój antagonista poślizgnął się na kawałku słomy z twojej zbroi.")
            Wybór
        if LosChybienia2==7:
            print("")
            Wybór


    # Mam pomyśł z otruciem. Chodzi o to żeby w funkcji walki zmieniać otrucie ciągle o 1 w górę i gdy osiągnie 3 to się zeruje. .
        
        

        

        

        

        

        


        

        
        
    


    


    


    


    
