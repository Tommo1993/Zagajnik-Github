# ochrona, sila, zrecznosc, wytrzymalosc, inteligencja, szczescie

def items():

    # Puste definiuje brak zbroi i odnosi się jedynie do armora i amuletów:
    puste = {"name": "puste", "type": "any", "ochrona": 0, "dodawana_siła": 0, "odejmowana_zręczność": 0, "dodawana_wytrzymałość": 0, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "dodawane_max_HP": 0, "dodawane_max_MP": 0}

    # Uzbrojenie:
    hands = {"name": "Pięści", "type": "weapon"}
        #buzdygan
        #miecz

    # Elementy armora:
    helmet1 = {"name": "Zniszczony szyszak", "type": "helmet", "ochrona": 1, "dodawana_siła": 1, "odejmowana_zręczność": -1, "dodawana_wytrzymałość": 2, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 5}
    helmet2 = {"name": "Pikelhauba", "type": "helmet", "ochrona": 2, "dodawana_siła": 2, "odejmowana_zręczność": -2, "dodawana_wytrzymałość": 3, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 15}
    chestplate1 = {"name": "Zniszczona przeszywanica", "type": "chestplate", "ochrona": 4, "dodawana_siła": 5, "odejmowana_zręczność": -3, "dodawana_wytrzymałość": 2, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 15}
    chestplate2 = {"name": "Zbroja płytowa", "type": "chestplate", "ochrona": 8, "dodawana_siła": 9, "odejmowana_zręczność": -10, "dodawana_wytrzymałość": 9, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 60}
    legs1 = {"name": "Skórzane spodnie", "type": "legs", "ochrona": 3, "dodawana_siła": 2, "odejmowana_zręczność": -2, "dodawana_wytrzymałość": 3, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 15}
    legs2 = {"name": "Nagolenniki", "type": "legs", "ochrona": 4, "dodawana_siła": 3, "odejmowana_zręczność": -5, "dodawana_wytrzymałość": 5, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 25}
    gloves1 = {"name": "Skórzane rękawice", "type": "gloves", "ochrona": 1, "dodawana_siła": 1, "odejmowana_zręczność": -4, "dodawana_wytrzymałość": 2, "dodawana_inteligencja": 0, "dodawane_szczęście": 0, "cena": 3}

    # jadalne
    apple = {"name": "Jabłko", "type": "food", "dodawane_HP": 2, "dodawane_MP": 1, "cena": 2}

    # eliksiry
    mana_elixir = {"name": "Eliksir many", "type": "elixir", "dodawane_HP": 0, "dodawane_MP": 2, "cena": 15}
    health_elixir = {"name": "Eliksir życia", "type": "elixir", "dodawane_HP": 4, "dodawane_MP": 0, "cena": 15}
    big_health_elixir = {"name": "Potężny eliksir życia", "type": "elixir", "dodawane_HP": 8, "dodawane_MP": 0, "cena": 22}
    big_mana_elixir = {"name": "Potężny eliksir many", "type": "elixir", "dodawane_HP": 0, "dodawane_MP": 5, "cena": 22}

    # amulety
    puste_amulet = {"name": "puste", "type": "amulet", "dodawana_siła": 0, "dodawana_zręczność": 0, "dodawana_wytrzymałość": 0, "dodawana_inteligencja": 0, "dodawane_szczęście": 0}
    amulet1 = {"name": "Naszyjnik z kości", "type": "amulet", "dodawana_siła": 1, "dodawana_zręczność": 0, "dodawana_wytrzymałość": 3, "dodawana_inteligencja": 1, "dodawane_szczęście": 1, "cena": 10}
    amulet2 = {"name": "Królicza łapka", "type": "amulet", "dodawana_siła": 0, "dodawana_zręczność": 2, "dodawana_wytrzymałość": 0, "dodawana_inteligencja": 5, "dodawane_szczęście": 6, "cena": 30}

    # lista wszystkich przedmiotów w grze, itemy wywołuje się za pomocą itemlist["nazwa_itemu"]:
    itemlist = {"zniszczony szyszak": helmet1, "pikelhauba": helmet2, "zniszczona przeszywanica": chestplate1, "zbroja płytowa": chestplate2,
            "skórzane spodnie": legs1, "nagolenniki": legs2, "skórzane rękawice": gloves1, "brak broni": hands, "puste": puste, "jabłko": apple,
                "eliksir many": mana_elixir, "potężny eliksir many": big_mana_elixir, "eliksir życia": health_elixir, "potężny eliksir życia": big_health_elixir, "brak_amuletu": puste_amulet,
                "naszyjnik z kości": amulet1, "królicza łapka": amulet2}
    return itemlist