def Questy():
    DaneQuesta=[0,"","","","",0,0] #Slot 0- Aktywność questa Slot 1- Nazwa Slot 2- Opis Slot 3- Zleceniodawca Slot 4- Nagroda przedmiot Slot 5- ilość exp Slot 6- nagroda pieniądze
    return DaneQuesta
    
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
    OtrzymanyEXP = DaneQuesta[5]
    OtrzymanyGOLD = DaneQuesta[6]
    OtrzymanyPRZEDMIOT = DaneQuesta[4]

def SzukanieMiejscaNaPrzedmiot(item):
    SprawdzenieMiejsca = []
    
    if 0 in item.inventoryslot1[0]:
        item.inventoryslot1 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot1[0]:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(1)
        return SprawdzenieMiejsca
        
    if 0 in item.inventoryslot2[0]:
        item.inventoryslot2 == OtrzymanyPRZEDMIOT      
    if 1 in SprawdzenieMiejsca[0]:
        if 1 in item.inventoryslot2[0]:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(2)
            return SprawdzenieMiejsca
            
    if 0 in item.inventoryslot3[0]:
        item.inventoryslot3 == OtrzymanyPRZEDMIOT            
    if 2 in SprawdzenieMiejsca[0]:
        if 1 in item.inventoryslot3[0]:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(3)
            return SprawdzenieMiejsca
            
    if 0 in item.inventoryslot4[0]:
        item.inventoryslot4 == OtrzymanyPRZEDMIOT
    if 3 in SprawdzenieMiejsca[0]:        
        if 1 in item.inventoryslot4[0]:
            if SprawdzenieMiejsca in locals():
                del SprawdzenieMiejsca
                SprawdzenieMiejsca=[]
            SprawdzenieMiejsca.append(4)
            return SprawdzenieMiejsca
    
    if 0 in item.inventoryslot5[0]:
        item.inventoryslot5 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot5[0]:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(5)
        return SprawdzenieMiejsca
        
    if 0 in item.inventoryslot6[0]:
        item.inventoryslot6 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot6[0]:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(6)
        return SprawdzenieMiejsca
        
    if 0 in item.inventoryslot7[0]:
        item.inventoryslot7 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot7[0]:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(7)
        return SprawdzenieMiejsca
    
    if 0 in item.inventoryslot8[0]:
        item.inventoryslot8 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot8[0]:
        if SprawdzenieMiejsca in locals():
            del SprawdzenieMiejsca
            SprawdzenieMiejsca=[]
        SprawdzenieMiejsca.append(8)
        return SprawdzenieMiejsca
    
    if 0 in item.inventoryslot10[0]:
        item.inventoryslot10 == OtrzymanyPRZEDMIOT
    if 1 in item.inventoryslot10[0]:
        print('Brak miejsca w ekwipunku!')