

def wykaz_itemow():
    from data.itemdefs import items
    itemlist = items()


    wykaz_itemow = open("wykaz_itemow.txt", mode="w")
    for x in itemlist.keys():
        y = x +"   "+str(itemlist[x])+"\n"*3
        wykaz_itemow.write(y)
    return None
