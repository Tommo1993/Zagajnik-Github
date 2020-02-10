class PlayerStats:
    def __init__(self, name, HP, MP, MaxHP, MaxMP, XP, level, str, dex, int, end, luck, basedamage, statpoints, spentstatpoints, pclass, subclass, combatstate, pointsspentstr, pointsspentdex, pointsspentint, pointsspentend, pointsspentluck, armorhead, armortorso, armorarms, armorlegs, eqaddedstr, eqaddeddex, eqaddedint, eqaddedend, eqaddedluck, basestr, basedex, baseint, baseend, baseluck, prevmaxhp, prevmaxmp):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.MaxHP = MaxHP
        self.MaxMP = MaxMP
        self.XP = XP
        self.level = level
        self.str = str
        self.dex = dex
        self.int = int
        self.end = end
        self.luck = luck
        self.basedamage = basedamage
        self.statpoints = statpoints
        self.spentstatpoints = spentstatpoints
        self.pclass = pclass
        self.subclass = subclass
        self.combatstate = combatstate
        self.pointsspentstr = pointsspentstr
        self.pointsspentdex = pointsspentdex
        self.pointsspentint = pointsspentint
        self.pointsspentend = pointsspentend
        self.pointsspentluck = pointsspentluck
        self.armorhead = armorhead #zależne od ekwipunku
        self.armortorso = armortorso #
        self.armorarms = armorarms #
        self.armorlegs = armorlegs #
        self.eqaddedstr = eqaddedstr # 
        self.eqaddeddex = eqaddeddex #
        self.eqaddedint = eqaddedint #
        self.eqaddedend = eqaddedend #
        self.eqaddedluck = eqaddedluck #
        self.basestr = basestr
        self.basedex = basedex
        self.baseint = baseint
        self.baseend = baseend
        self.baseluck = baseluck
        self.prevmaxhp = prevmaxhp
        self.prevmaxmp = prevmaxmp
    
    def classchoice(self): #wybór startowej klasy, przedmioty mogą być dodane za pomocą tego (prawdopodobnie)
        print("Wybierz swoją początkową klasę.")
        print("Masz do wyboru zbrojnego, zwiadowcę i adepta magii.")
        print("(1/2/3)")
        while True:
            qwe = str(input())
            if qwe == "1":
                self.pclass = 1
                self.subclass = 1
                self.HP = 20  #maxhp się zwiększa wraz z siłą i wytrzymałością, podobnie jak mana; 4 (str) * 1 + 3 (end) * 2 = dodane maxhp
                self.MaxHP = 10  #
                self.MP = 5
                self.MaxMP = 0
                self.basestr = 4
                self.baseend = 3
                self.baseint = 1
                self.basedex = 3
                self.baseluck = 1
                print("Wybrałeś zbrojnego.")
                break
            if qwe == "2":
                self.pclass = 2
                self.subclass = 1
                self.HP = 15
                self.MaxHP = 10
                self.MP = 10
                self.MaxMP = 0
                self.basestr = 3
                self.baseend = 1
                self.baseint = 3
                self.basedex = 4
                self.baseluck = 2
                print("Wybrałeś zwiadowcę.")
                break
            if qwe == "3":
                self.pclass = 3
                self.subclass = 1
                self.HP = 10
                self.MaxHP = 6
                self.MP = 15
                self.MaxMP = 0
                self.basestr = 2
                self.baseend = 1
                self.baseint = 6
                self.basedex = 3
                self.baseluck = 1
                print("Wybrałeś adepta magii.")
                break
        return self
    def calcstats(self): #oblicza statystyki, by wszystko się zgadzało
        self.str = self.pointsspentstr + self.eqaddedstr + self.basestr
        self.dex = self.pointsspentdex + self.eqaddeddex + self.basedex
        self.int = self.pointsspentint + self.eqaddedint + self.baseint
        self.end = self.pointsspentend + self.eqaddedend + self.baseend
        self.luck = self.pointsspentluck + self.eqaddedluck + self.baseluck
        return self
        
    def calcmaxhp(self):
        self.MaxHP = 10+(1*self.str)+(2*self.end)
        if self.HP > self.MaxHP:
            self.HP = self.MaxHP
        if self.MaxHP < 0:
            self.MaxHP = 1
            print("Życie poniżej zera; ustawiono na 0.")
        return self
    def calcmaxmp(self):
        self.MaxMP = 0+(1*self.dex)+(2*self.int)
        if self.MP > self.MaxMP:
            self.MP = self.MaxMP
        if self.MP < 0:
            self.MP = 0
        if self.MaxMP < 0:
            self.MaxMP = 0
            print("Mana poniżej zera; ustawiono na 0.")
        return self

    def prevhpscaling(self):
        self.prevmaxhp = self.HP/self.MaxHP*100
        self.prevmaxmp = self.MP/self.MaxMP*100
        return self
        
    def hpmpscaling(self):
        if self.HP/self.MaxHP*100 != self.prevmaxhp:
            self.HP = self.MaxHP*self.prevmaxhp//100
            self.HP = int(self.HP)
        if self.MP/self.MaxMP*100 != self.prevmaxmp:
            self.MP = self.MaxMP*self.prevmaxmp//100
            self.MP= int(self.MP)
        return self
        
    def calcdamage(self):
        self.basedamage = 1+(1*self.dex)+(2*self.str)
        if self.basedamage < 0:
            self.MaxMP = 1
            print("Obrażenia poniżej zera; ustawiono na 0.")
        return self
    def calclevel(self):
        if self.XP < 0:
            print("Ta wiadomość nie powinna się pokazywać. Coś jest nie tak z twoim poziomem...")
        if self.XP == 0:
            self.level = 0
            self.statpoints = 0
        if self.XP > 0 and self.XP <= 99:
            self.level = 1
            self.statpoints = 1 - self.spentstatpoints
        if self.XP >= 100 and self.XP <= 219:
            self.level = 2
            self.statpoints = 2 - self.spentstatpoints
        if self.XP >= 220 and self.XP <= 349:
            self.level = 3
            self.statpoints = 3 - self.spentstatpoints
        if self.XP >= 350 and self.XP <= 499:
            self.level = 4
            self.statpoints = 4 - self.spentstatpoints
        if self.XP >= 500 and self.XP <= 750:
            self.level = 5
            self.statpoints = 5 - self.spentstatpoints
        return self
    def displaystats(self):
        print(self.name, "nazwa gracza")
        print(self.HP, "hp")
        print(self.MP, "mp")
        print(self.MaxHP, "maxhp")
        print(self.MaxMP, "maxmp")
        print(self.XP, "xp")
        print(self.level, "lvl")
        print(self.str, "str")
        print(self.dex, "dex")
        print(self.int, "int")
        print(self.end, "end")
        print(self.luck, "luck")
        print(self.basedamage, "basedmg")
        print(self.statpoints, "statp")
        print(self.spentstatpoints, "spentstatp")
        print(self.pclass, "pclass")
        print(self.subclass, "subclass")
        print(self.combatstate, "combatstate")