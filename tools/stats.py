P,MAG,SG,B,S,MP,SMG,MT,RL,K = 'Handgun','Magnum','Shotgun','Bolt','Semi','MachinePistol','SMG','MineThrower','Rocket','Knife'
# class: (tier, type, dmg, useTime, kb, vel, crit, spread, ammoSave, pellets, pierce, scope, auto, sound, burst, reuseDelay)
STATS = {
 'Handgun':          (1,P,  11,15,2.0, 9,  4, 0,  0,  1,0,False,False,'pistol', 1, 0),
 'Punisher':         (2,P,  13,16,2.5,10,  4, 0,  0,  1,2,False,False,'pistol', 1, 0),
 'Red9':             (3,P,  24,20,3.5,11,  6, 0,  0,  1,0,False,False,'pistol', 1, 0),
 'Blacktail':        (4,P,  20,11,2.5,10,  6, 0,  0,  1,0,False,False,'pistol', 1, 0),
 'Matilda':          (5,MP, 16, 4,1.5,10,  2, 3,  0,  1,0,False,True, 'pistol', 3,14),
 'Shotgun':          (3,SG, 10,45,5.0, 8,  0,16,  0,  5,0,False,False,'shotgun',1, 0),
 'RiotGun':          (5,SG, 18,40,5.5, 9,  0,12,  0,  6,0,False,False,'shotgun',1, 0),
 'Striker':          (7,SG, 24,22,5.0, 9,  0,13,  0,  6,0,False,True, 'shotgun',1, 0),
 'Rifle':            (3,B,  40,42,5.0,13, 15, 0,  0,  1,1,True, False,'sniper', 1, 0),
 'RifleSemiAuto':    (6,S,  62,22,5.0,15, 15, 0,  0,  1,1,True, False,'sniper', 1, 0),
 'TMP':              (4,SMG, 9, 5,1.0, 9,  0, 8,  0,  1,0,False,True, 'smg',    1, 0),
 'ChicagoTypewriter':(9,SMG,40, 5,2.0,12,  4, 4,  1,  1,0,False,True, 'smg',    1, 0),
 'BrokenButterfly':  (6,MAG,85,32,7.0,13, 10, 0,  0,  1,2,False,False,'magnum', 1, 0),
 'Killer7':          (7,MAG,80,22,6.5,13, 10, 0,  0,  1,1,False,False,'magnum', 1, 0),
 'Handcannon':       (9,MAG,240,40,10,15, 15, 0,  0,  1,4,False,False,'magnum', 1, 0),
 'MineThrower':      (6,MT, 45,35,4.0, 8,  0, 0,  0,  1,0,False,False,'grenade',1, 0),
 'RocketLauncher':   (8,RL,120,50,8.0,10,  0, 0,  0,  1,0,False,False,'rocket', 1, 0),
 'Knife':            (1,K,  10,14,3.0, 0,  4, 0,  0,  1,0,False,True, 'swing',  1, 0),
}
# tier -> (ingredients, tile, rarity, buy gold)  (same tiers as WW2Guns, plus tier 9 post-Plantera)
TIERS = {
 1: ([('G:IronBar',10),('V:Wood',5)], 'TileID.Anvils', 'ItemRarityID.White', 1),
 2: ([('C:SilverBar',12),('V:Wood',8)], 'TileID.Anvils', 'ItemRarityID.Blue', 3),
 3: ([('C:EvilBar',12),('G:IronBar',6)], 'TileID.Anvils', 'ItemRarityID.Green', 6),
 4: ([('I:MeteoriteBar',12),('I:HellstoneBar',6)], 'TileID.Anvils', 'ItemRarityID.Orange', 10),
 5: ([('C:CobaltBar',12),('I:IllegalGunParts',1)], 'TileID.Anvils', 'ItemRarityID.LightRed', 18),
 6: ([('C:MythrilBar',12),('I:SoulofNight',6)], 'TileID.MythrilAnvil', 'ItemRarityID.Pink', 28),
 7: ([('C:AdamantiteBar',14),('I:SoulofNight',8),('I:IllegalGunParts',1)], 'TileID.MythrilAnvil', 'ItemRarityID.LightPurple', 40),
 8: ([('I:HallowedBar',15),('I:SoulofMight',10)], 'TileID.MythrilAnvil', 'ItemRarityID.Lime', 60),
 9: ([('I:ChlorophyteBar',15),('I:Ectoplasm',6)], 'TileID.MythrilAnvil', 'ItemRarityID.Yellow', 80),
}
KNIFE_RECIPE = ([('G:IronBar',6)], 'TileID.Anvils')
SOUNDS = {
 'pistol': 'SoundID.Item41', 'smg': 'SoundID.Item11', 'sniper': 'SoundID.Item40', 'shotgun': 'SoundID.Item36',
 'magnum': 'SoundID.Item40 with { Pitch = -0.35f }', 'grenade': 'SoundID.Item61', 'rocket': 'SoundID.Item11 with { Pitch = -0.5f }',
 'swing': 'SoundID.Item1',
}
# Rocket-ammo weapons borrow the projectiles of a vanilla launcher
LAUNCHER = {'MineThrower': 'ItemID.ProximityMineLauncher', 'RocketLauncher': 'ItemID.RocketLauncher'}
SHOP = {  # Arms Dealer, like the RE4 Merchant
 'Handgun': None,
 'Punisher': 'Condition.DownedEyeOfCthulhu', 'Shotgun': 'Condition.DownedEyeOfCthulhu',
 'Red9': 'Condition.DownedEowOrBoc',
 'Blacktail': 'Condition.DownedSkeletron', 'Rifle': 'Condition.DownedSkeletron', 'TMP': 'Condition.DownedSkeletron',
 'RiotGun': 'Condition.Hardmode', 'Matilda': 'Condition.Hardmode',
 'BrokenButterfly': 'Condition.DownedMechBossAny', 'MineThrower': 'Condition.DownedMechBossAny', 'RifleSemiAuto': 'Condition.DownedMechBossAny',
 'RocketLauncher': 'Condition.DownedMechBossAll',
}
DROPS = [  # (npc, item, chance denominator)
 ('NPCID.TacticalSkeleton','Killer7',12),
 ('NPCID.SkeletonCommando','RocketLauncher',10),
 ('NPCID.PirateDeadeye','Striker',20),
]
TYPE_ES = {P:'Pistola',MAG:'Mágnum',SG:'Escopeta',B:'Rifle de cerrojo',S:'Rifle semiautomático',MP:'Pistola automática',
           SMG:'Subfusil',MT:'Lanzaminas',RL:'Lanzacohetes',K:'Cuchillo'}
TYPE_EN = {P:'Handgun',MAG:'Magnum',SG:'Shotgun',B:'Bolt-action rifle',S:'Semi-automatic rifle',MP:'Machine pistol',
           SMG:'Submachine gun',MT:'Mine launcher',RL:'Rocket launcher',K:'Knife'}
CAT_EN = {'Handguns':'Handguns','Shotguns':'Shotguns','Rifles':'Rifles','MachinePistols':'Machine guns','Magnums':'Magnums','Special':'Special'}
CAT_ES = {'Handguns':'Pistolas','Shotguns':'Escopetas','Rifles':'Rifles','MachinePistols':'Ametralladoras','Magnums':'Mágnums','Special':'Especiales'}
