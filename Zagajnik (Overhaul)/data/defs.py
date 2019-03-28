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
    def calcstats(player):
        player.MaxHP = player.MaxHPnocalc + player.end
        player.MaxMP = player.MaxMPnocalc + player.int
        player.basedamage = player.basedamage + player.str
        player.weapondamage = player.basedamage + item.WeaponDamage
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

class EnemyStats:
    def __init__(entity, name, ID, HP, MP, attackdmg, EXPreward):
	entity.name = name
	entity.ID = ID
	entity.HP = HP
	entity.MP = MP
	entity.attackdmg
	entity.EXPreward
        




