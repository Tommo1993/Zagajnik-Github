def ObrażeniaKłute(Player):
	ObrażeniaInput1 = 0.60*player.weapondamage
	ObrażeniaOutput1 = ObrażeniaInput1*(0.10*player.dex)

def ObrażeniaCięte(Player):
	ObrażeniaInput2 = 0.40*player.weapondamage
	ObrażeniaOutput2 = ObrażeniaInput2*(0.10*player.dex)

def ObrażeniaObuchowe(Player):
	ObrażeniaInput3 = 0.75*player.weapondamage
	ObrażeniaOutput3 = ObrażeniaInput3*(0.10*player.str)
	
def ObrażeniaWychodzące(ObrażeniaCięte, ObrażeniaKłute, ObrażeniaObuchowe, Player):
	if item.itemslotweapon1[16] in range(1,20):
		playerOutputDMG = ObrażeniaOutput1
	if item.itemslotweapon1[16] in range(21,40):
		playerOutputDMG = ObrażeniaOutput2
	if item.itemslotweapon1[16] in range(41,60):
		playerOutputDMG = ObrażeniaOutput3
	return playerOutputDMG

	
	
#Obrażenia*typ* - Rodzaj zadawanych obrażeń zawartych w definicji (def)
#Kłute i Cięte skalują się ze zręcznością Kłute bardziej natomiast z drugiej strony obrażenia bazowe bronii posiadających ten typ są niższe.
#Obuchowe skalują się z siłą, skalują się najlepiej ze wszystkich typów, natomiast obrażenia bazowe są najniższe ze wszystkich.
#ObrażeniaInput*cyfra* - surowe obrażenia surowe przemnożone przez dopowiedni mnożnik.
#ObrażeniaOutput*cyfra* - Obrażenia niesurowe (XD) surowe obliczone wraz z atrybutem przy odpowiednim mnożnikiem (dex, str)
#ObrażeniaWychodzące- faktyczne obrażenia zadawane przez gracza, program sprawdza jakie obrażenia zadaje broń na podstawie jej ID czyli
#playerOutputDMG - Wartość obrażeń wychodzących

	