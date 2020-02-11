
# linia 12 otwieranie eq
# linia 19 ubieranie armora
# linia 43 zdejmowanie armora
# linia 75 wyrzucanie itemów
# linia 93 wybieranie używanej broni
# linia 107 przedmioty jadalne
# linia 130 eliksiry
def inventory(ekwipunek, ActionInput, itemlist, player):
    lista_do_wyswietlenia = (
    "Hełm:   ", "Napierśnik:   ", "Nogawice:   ", "Rękawice:   ", "Slot 1:   ", "Slot 2:   ", "Slot 3:   ",
    "Slot 4:   ", "Slot 5:   ", "Amulet:   ", "Korony:   ")
    if ActionInput.lower() == "ekwipunek":
        for inventory_position in range(0, 11):
            if ekwipunek[inventory_position] == "puste":
                print(lista_do_wyswietlenia[inventory_position], ekwipunek[inventory_position])
            elif type(ekwipunek[inventory_position]) == int:
                print(lista_do_wyswietlenia[inventory_position], ekwipunek[inventory_position])
            else:
                print(lista_do_wyswietlenia[inventory_position],
                      ekwipunek[inventory_position]["name"]) # tu będą wpisywane statystyki przedmiotu#
    if ActionInput.lower()[0:6] == "ubierz":
        key = ActionInput.lower()[
              7:len(ActionInput.lower())]  #### KLUCZ DO ODNALEZIENIA ITEMU NA LIŚCIE ITEMÓW itemlist
        if key not in itemlist.keys():
            print("Wybrany przedmiot nie istnieje!")
            return ekwipunek
        if  key in itemlist.keys() and itemlist[key]["type"] not in ["helmet", "chestplate", "legs", "gloves", "amulet"]:
            print("Nie możesz założyć", key.title(), "!")
            return ekwipunek
        if key in itemlist.keys() and itemlist[key] in ekwipunek[4:9]:
            for item_position in range(4, 9):
                if ekwipunek[item_position] == itemlist[key] and itemlist[key]["type"] in ["helmet", "chestplate",
                                                                                           "legs", "gloves", "amulet"]:
                    ekwipunek[item_position] = "puste"
            if itemlist[key]["type"] == "helmet":
                ekwipunek[0] = itemlist[key]
                print("Założono", key.title())
                return ekwipunek
            elif itemlist[key]["type"] == "legs":
                ekwipunek[2] = itemlist[key]
                print("Założono", key.title())
                return ekwipunek
            elif itemlist[key]["type"] == "chestplate":
                ekwipunek[1] = itemlist[key]
                print("Założono", key.title())
                return ekwipunek
            elif itemlist[key]["type"] == "gloves":
                ekwipunek[3] = itemlist[key]
                print("Założono", key.title())
                return ekwipunek
            elif itemlist[key]["type"] == "amulet":
                ekwipunek[9] = itemlist[key]
                print("Założono", key.title())
                return ekwipunek

        elif key in itemlist.keys() and itemlist[key] in ekwipunek[4:9] and itemlist[key]["type"] not in ["helmet", "chestplate", "legs", "gloves"]:
            print("Nie możesz założyć", itemlist[key])
            return ekwipunek, itemlist
        elif key in itemlist.keys() and itemlist[key] not in ekwipunek[4:9]:
            print("Nie masz tego przedmiotu!")
            return ekwipunek
        else:
            print("Wybrany przedmiot nie istnieje")
            return ekwipunek
    if ActionInput.lower()[0:7] == "zdejmij":
        if "puste" not in ekwipunek[4:9]:
            print("Nie masz miejsca na przechowanie zdjętego przedmiotu!")
            return ekwipunek
        key = ActionInput.lower()[8:len(ActionInput.lower())]
        if key not in itemlist.keys():
            print("Wybrany przedmiot nie istnieje")
            return ekwipunek
        if key in itemlist.keys() and itemlist[key] in ekwipunek[0:4] or ekwipunek[9] == itemlist[key]:
            if itemlist[key]["type"] == "helmet" and ekwipunek[0] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[0] = itemlist["puste"]
                        print("Zdjęto", key.title())
                        return ekwipunek, itemlist
            elif itemlist[key]["type"] == "chestplate" and ekwipunek[1] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[1] = itemlist["puste"]
                        print("Zdjęto", key.title())
                        return ekwipunek
            elif itemlist[key]["type"] == "legs" and ekwipunek[2] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[2] = itemlist["puste"]
                        print("Zdjęto", key.title())
                        return ekwipunek
            elif itemlist[key]["type"] == "gloves" and ekwipunek[3] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[3] = itemlist["puste"]
                        print("Zdjęto", key.title())
                        return ekwipunek
            elif itemlist[key]["type"] == "amulet" and ekwipunek[9] == itemlist[key]:
                for free_space in range(4, 9):
                    if ekwipunek[free_space] == "puste":
                        ekwipunek[free_space] = itemlist[key]
                        ekwipunek[9] = itemlist["brak_amuletu"]
                        print("Zdjęto", key.title())
                        return ekwipunek, itemlist


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
                    print("Wyrzucono", key.title())
                    return ekwipunek, itemlist
        else:
            print("Wybrany przedmiot nie istnieje!")
            return ekwipunek
    if ActionInput.lower()[0:6] == "dobądź":
        key = ActionInput.lower()[7:len(ActionInput.lower())]
        if  key in itemlist.keys() and itemlist[key] in ekwipunek[4:9] and itemlist[key]["type"] == "weapon":
            weapon = itemlist[key]
            return weapon
        elif key in itemlist.keys() and itemlist[key]["type"] != "weapon":
            print("Nie możesz dobyć ", key.title(), "!")
            return ekwipunek
        elif key not in itemlist.keys():
            print("Wybrany przedmiot nie istnieje")
            return ekwipunek
        elif key in itemlist.keys() and itemlist[key] not in ekwipunek[4:9]:
            print("Nie posiadasz wybranego przedmiotu")
            return ekwipunek
    if ActionInput.lower()[0:5] == "zjedz":
        key = ActionInput.lower()[6:len(ActionInput.lower())]
        if key not in itemlist.keys():
            print("Wybrany przedmiot nie istnieje")
            return ekwipunek
        elif key in itemlist.keys() and itemlist[key]["type"] == "food":
            if itemlist[key] in ekwipunek[4:9]:
                player.HP = player.HP + itemlist[key]["dodawane_HP"]
                player.MP = player.MP + itemlist[key]["dodawane_MP"]
                for food_position in range(4, 9):
                    if ekwipunek[food_position] == itemlist[key]:
                        ekwipunek[food_position] = "puste"
                        print("Zjedzono", key.title())
                        return ekwipunek, player.HP, player.MP, itemlist
            if itemlist[key] not in ekwipunek[4:9]:
                print("Nie posiadasz tego przedmiotu!")
                return ekwipunek
        elif key in itemlist.keys() and itemlist[key]["type"] != "food":
            print("Nie możesz zjeść", key)
    if ActionInput.lower()[0:5] == "wypij":
        key = ActionInput.lower()[6:len(ActionInput.lower())]
        if key not in itemlist.keys():
            print("Wybrany przedmiot nie istnieje")
            return ekwipunek
        if key in itemlist.keys() and itemlist[key] not in ekwipunek[4:9]:
            print("Nie posiadasz przedmiotu, który chcesz wypić!")
            return ekwipunek
        if key in itemlist.keys() and itemlist[key] in ekwipunek[4:9] and itemlist[key]["type"] != "elixir":
            print("Nie możesz wypić", key.title())
        if key in itemlist.keys() and itemlist[key] in ekwipunek[4:9] and itemlist[key]["type"] == "elixir":
            player.HP = player.HP + itemlist[key]["dodawane_HP"]
            player.MP = player.MP + itemlist[key]["dodawane_MP"]
            for elixir_position in range(4, 9):
                if ekwipunek[elixir_position] == itemlist[key]:
                    ekwipunek[elixir_position] = "puste"
                    print("Wypito", itemlist[key]["name"].title())
                    return ekwipunek