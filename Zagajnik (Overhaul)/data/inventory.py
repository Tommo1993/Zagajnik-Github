

def inventory(ekwipunek, ActionInput, itemlist):
    lista_do_wyswietlenia = (
    "Hełm:   ", "Napierśnik:   ", "Nogawice:   ", "Rękawice:   ", "Slot 1:   ", "Slot 2:   ", "Slot 3:   ",
    "Slot 4:   ", "Slot 5:   ")
    if ActionInput.lower() == "ekwipunek":
        for inventory_position in range(9):
            if ekwipunek[inventory_position] == "puste":
                print(lista_do_wyswietlenia[inventory_position], ekwipunek[inventory_position])
            else:
                print(lista_do_wyswietlenia[inventory_position],
                      ekwipunek[inventory_position]["name"])  # tu będą wpisywane statystyki przedmiotu#
    if ActionInput.lower()[0:6] == "ubierz":
        key = ActionInput.lower()[
              7:len(ActionInput.lower())]  #### KLUCZ DO ODNALEZIENIA ITEMU NA LIŚCIE ITEMÓW itemlist
        if key in itemlist.keys() and itemlist[key]["doIhave"] == True:
            for item_position in range(4, 9):
                if ekwipunek[item_position] == itemlist[key] and itemlist[key]["type"] in ["helmet", "chestplate",
                                                                                           "legs", "gloves"]:
                    ekwipunek[item_position] = "puste"
            if itemlist[key]["type"] == "helmet":
                ekwipunek[0] = itemlist[key]
                return ekwipunek
            elif itemlist[key]["type"] == "legs":
                ekwipunek[2] = itemlist[key]
                return ekwipunek
            elif itemlist[key]["type"] == "chestplate":
                ekwipunek[1] = itemlist[key]
                return ekwipunek
            elif itemlist[key]["type"] == "gloves":
                ekwipunek[3] = itemlist[key]
                return ekwipunek
        elif key in itemlist.keys() and itemlist[key]["doIhave"] == False:
            print("Nie masz tego przedmiotu!")
        else:
            print("Wybrany przedmiot nie istnieje")
    if ActionInput.lower()[0:7] == "zdejmij":
        if "puste" not in ekwipunek[5:9]:
            print("Nie masz miejsca na przechowanie zdjętego przedmiotu!")
            return ekwipunek
        key = ActionInput.lower()[8:len(ActionInput.lower())]
        if key in itemlist.keys() and itemlist[key]["doIhave"] == True:
            if itemlist[key]["type"] == "helmet" and ekwipunek[0] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[0] = "puste"
                        return ekwipunek
            elif itemlist[key]["type"] == "chestplate" and ekwipunek[1] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[1] = "puste"
                        return ekwipunek
            elif itemlist[key]["type"] == "legs" and ekwipunek[2] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[2] = "puste"
                        return ekwipunek
            elif itemlist[key]["type"] == "gloves" and ekwipunek[3] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[3] = "puste"
                        return ekwipunek
            else:
                print("Tego przedmiotu nie możesz zdjąć!")
    if ActionInput.lower()[0:6] == "wyrzuć":
        key = ActionInput.lower()[7:len(ActionInput.lower())]
        if key in itemlist.keys():
            if itemlist[key] not in ekwipunek[4:9]:
                if itemlist[key] in ekwipunek[0:4]:
                    print("Najpierw zdejmij z siebie przedmiot, który chcesz wyrzucić!")
                    return ekwipunek
                else:
                    print("Nie masz przedmiotu, który chcesz wyrzucić!")
                    return ekwipunek
            for item_position in range(4, 9):
                if ekwipunek[item_position] == itemlist[key]:
                    ekwipunek[item_position] = "puste"
                    itemlist[key]["doIhave"] = False
                    return ekwipunek
        else:
            print("Wybrany przedmiot nie istnieje!")
            return ekwipunek