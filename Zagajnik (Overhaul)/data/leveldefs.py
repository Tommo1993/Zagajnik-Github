def Lvl1():
    if player.EXP >= 10 and player.level == 0:
        player.level = 1
        player.MaxHP = player.MaxHP + 2
        player.MaxMP = player.MaxMP + 1
		player.statpoint = player.statpoint + 1