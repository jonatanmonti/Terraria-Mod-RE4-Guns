"""Pixel drawings of every RE4 weapon (same engine and style as WW2Guns)."""
from pix import G

# ---------- shared parts ----------
def tguard(g, x, y, m='black'):
    g.R(x, y, x, y+2, m); g.R(x, y+2, x+4, y+2, m); g.D(x+4, y+1, m)
    g.D(x+2, y, m, 'd'); g.D(x+2, y+1, m, 'd')

def rifle_stock(g, xw, m, top=8, butt=15, wb=12, pg=False):
    g.P([(0, top-1), (xw, top), (xw, wb), (xw-5, wb), (0, butt)], m)
    g.R(0, top-1, 0, butt, 'black', 'd')
    if pg:
        g.P([(xw-5, wb), (xw, wb), (xw-1, wb+5), (xw-5, wb+5)], m)

def pgrip(g, x, y, m='black', h=6, w=4, slant=1):
    g.P([(x, y), (x+w, y), (x+w-slant, y+h), (x-slant, y+h)], m)

def bolt_handle(g, x, y):
    g.D(x, y, 'metal'); g.D(x+1, y+1, 'metal'); g.R(x+1, y+2, x+2, y+2, 'steel')

def scope(g, x0, x1, y=3):
    g.R(x0, y, x1, y+1, 'black')
    g.R(x0-2, y-1, x0-1, y+2, 'black'); g.R(x1+1, y-1, x1+3, y+2, 'black')
    g.D(x1+3, y, 'steel', 'h')
    g.D(x0+3, y+2, 'black'); g.D(x1-3, y+2, 'black')

def auto_pistol(slen=16, sh=3, grip='black', gw=5, gh=8, gx=2, slide='black', frame='black', slant=2):
    g = G()
    y = 4
    g.R(0, y, slen, y+sh, slide)
    g.R(1, y+sh+1, slen-3, y+sh+1, frame)
    gy = y+sh+1
    g.P([(gx, gy), (gx+gw, gy), (gx+gw-slant, gy+gh), (gx-slant, gy+gh)], grip)
    g.R(gx-slant, gy+gh, gx+gw-slant, gy+gh, frame, 'd')
    tguard(g, gx+gw, gy+1, frame)
    g.D(slen-1, y-1, slide, 'd')        # front sight
    g.D(1, y-1, slide, 'd')             # rear sight
    g.D(-1, y, frame, 'd')              # hammer
    return g

# ---------- handguns ----------
def handgun():
    g = auto_pistol(slen=16, sh=3, grip='black', gw=5, gh=8, gx=2)
    g.R(7, 4, 10, 4, 'black', 'h')                       # ejection port shine
    for y in (10, 12, 14): g.D(2, y, 'black', 'd')       # grip checkering
    return g

def punisher():
    g = auto_pistol(slen=16, sh=3, grip='black', gw=5, gh=8, gx=2, slide='metal')
    for x in (1, 2, 3): g.R(x, 5, x, 7, 'metal', 'd')    # slide serrations
    g.R(9, 8, 12, 8, 'black', 'h')                       # light rail
    return g

def blacktail():
    g = auto_pistol(slen=18, sh=3, grip='black', gw=5, gh=9, gx=3)
    g.R(4, 7, 15, 7, 'steel')                            # silver stripe along the slide
    g.R(0, 5, 1, 6, 'black', 'd')
    g.D(19, 6, 'black', 'd')
    return g

def red9():
    g = G()
    g.R(14, 5, 31, 6, 'black'); g.R(14, 4, 31, 4, 'black', 'l')   # long thin barrel
    g.D(31, 3, 'black', 'd')
    g.R(4, 3, 14, 8, 'black')                                     # receiver
    g.R(5, 2, 11, 2, 'black', 'l')
    g.D(3, 2, 'black', 'd'); g.D(2, 1, 'black', 'd')              # ring hammer
    g.R(14, 9, 18, 13, 'black')                                   # box magazine ahead of the trigger
    g.R(15, 10, 17, 12, 'black', 'd')
    tguard(g, 9, 9)
    g.P([(4, 9), (8, 9), (6, 18), (0, 18)], 'wood')               # broomhandle grip
    for y in (11, 13, 15): g.L(2, y+1, 6, y, 'wood', 'd')
    g.D(4, 12, 'red', 'h'); g.R(3, 13, 4, 13, 'red'); g.D(4, 14, 'red'); g.D(3, 15, 'red')  # the red 9
    g.R(0, 18, 6, 18, 'black', 'd')
    return g

def matilda():
    g = G()
    g.R(8, 4, 26, 7, 'black')                     # slide
    g.R(27, 5, 30, 6, 'black'); g.R(28, 4, 30, 4, 'black', 'd')   # muzzle brake
    g.D(28, 5, 'black', 'x')
    g.R(9, 8, 22, 8, 'black')
    g.P([(9, 9), (14, 9), (12, 17), (7, 17)], 'black')            # grip
    g.R(7, 18, 11, 22, 'black'); g.R(8, 19, 10, 21, 'black', 'd')  # extended mag
    tguard(g, 14, 9)
    g.R(19, 9, 21, 9, 'black'); g.R(20, 10, 21, 14, 'metal')      # folding foregrip
    g.L(8, 5, 0, 6, 'metal'); g.L(8, 9, 0, 10, 'metal')           # wire shoulder stock
    g.R(0, 5, 0, 11, 'black', 'd')
    g.D(23, 3, 'black', 'd'); g.D(9, 3, 'black', 'd')
    return g

# ---------- magnums ----------
def revolver(blen=34, m='black', grip='wood', cyl=(7, 2, 14, 9), lug=True, comp=False):
    g = G()
    x0, y0, x1, y1 = cyl
    g.R(x1+1, 4, blen, 6, m)                     # barrel
    g.R(x1+1, 3, blen, 3, m, 'l')                # top rib
    if lug:
        g.R(x1+3, 7, blen, 7, m, 'd')            # full under-lug
    g.D(blen, 2, m, 'd')                         # front sight
    g.R(x1+1, 7, x1+2, 8, m)                     # crane
    g.R(x0, y0, x1, y1, m)                       # cylinder
    for c in ((x0, y0), (x1, y0), (x0, y1), (x1, y1)): g.X(*c, *c)
    for x in range(x0+1, x1, 2):
        g.R(x, y0+1, x, y1-1, m, 'h'); g.R(x+1, y0+1, x+1, y1-1, m, 'd')
    g.R(3, 4, x0-1, 8, m)                        # frame
    g.D(2, 2, m, 'd'); g.D(3, 3, m)              # hammer
    g.P([(2, 9), (7, 9), (5, 17), (-1, 17)], grip)
    g.C(1, 17, 1, grip)
    tguard(g, 7, 10, m)
    if comp:
        g.R(blen-3, 2, blen+1, 7, m)
        for x in (blen-2, blen): g.D(x, 3, m, 'x')
    return g

def broken_butterfly():
    g = revolver(blen=34, m='black', grip='wood')
    for x in range(17, 34, 3): g.D(x, 2, 'black', 'd')   # vented rib
    for y in (11, 13, 15): g.D(3, y, 'wood', 'd')
    return g

def killer7():
    g = auto_pistol(slen=20, sh=4, grip='black', gw=6, gh=9, gx=2, slide='steel', frame='steel')
    g.R(6, 4, 11, 4, 'steel', 'h')
    for x in (1, 2, 3): g.R(x, 5, x, 7, 'steel', 'd')
    g.R(21, 5, 22, 7, 'black')                 # bushing / barrel
    return g

def handcannon():
    g = revolver(blen=40, m='steel', grip='black', cyl=(7, 1, 15, 10), comp=True)
    for y in (11, 13, 15): g.L(1, y+1, 4, y, 'black', 'd')   # finger grooves
    return g

# ---------- shotguns ----------
def shotgun():
    g = G()
    rifle_stock(g, 16, 'wood', top=8, butt=15, wb=12)
    g.R(16, 7, 28, 11, 'black')                  # receiver
    g.R(29, 8, 54, 8, 'black', 'l'); g.R(29, 9, 54, 9, 'black')   # barrel
    g.R(29, 10, 48, 10, 'black')                 # magazine tube
    g.R(32, 10, 42, 12, 'wood')                  # pump
    for x in (34, 36, 38, 40): g.D(x, 11, 'wood', 'd')
    g.D(53, 7, 'steel', 'h')                     # bead sight
    tguard(g, 18, 12)
    return g

def riot_gun():
    g = G()
    g.P([(0, 7), (13, 8), (13, 11), (8, 11), (0, 14)], 'black')   # synthetic stock
    g.R(0, 7, 0, 14, 'black', 'd')
    g.R(13, 7, 26, 11, 'black')
    g.R(27, 8, 46, 9, 'black'); g.R(27, 10, 42, 10, 'black')
    g.R(29, 10, 38, 12, 'black'); for_x = range(30, 38, 2)
    for x in for_x: g.D(x, 11, 'black', 'd')
    pgrip(g, 13, 12, 'black', h=6, w=4, slant=1)
    tguard(g, 17, 12)
    g.R(17, 6, 23, 6, 'black', 'l')              # ghost ring rail
    g.D(45, 7, 'black', 'd')
    g.R(20, 9, 22, 9, 'steel')
    return g

def striker():
    g = G()
    g.R(0, 5, 0, 12, 'black', 'd')               # folding stock
    g.L(1, 6, 12, 7, 'metal'); g.L(1, 11, 12, 10, 'metal')
    g.R(12, 6, 21, 10, 'black')                  # receiver
    g.C(26, 9, 5, 'black'); g.C(26, 9, 2, 'black', 'd')   # rotary drum
    for (x, y) in ((26, 5), (30, 9), (26, 13), (22, 9)): g.D(x, y, 'metal')
    g.R(31, 7, 43, 8, 'black')                   # barrel
    g.R(31, 6, 40, 6, 'metal')                   # shroud
    for x in range(32, 40, 2): g.D(x, 6, 'black', 'd')
    g.R(37, 9, 38, 14, 'black')                  # front handle
    pgrip(g, 13, 11, 'black', h=7, w=4, slant=1)
    tguard(g, 17, 11)
    return g

# ---------- rifles ----------
def rifle():
    g = G()
    rifle_stock(g, 17, 'dwood', top=8, butt=15, wb=12)
    g.R(17, 8, 29, 10, 'black')                  # receiver
    g.R(29, 9, 62, 9, 'black'); g.R(29, 10, 50, 10, 'black')   # barrel
    g.R(17, 10, 52, 12, 'dwood')                 # stock forend
    g.D(61, 8, 'black', 'd')
    bolt_handle(g, 26, 11)
    tguard(g, 18, 13)
    g.R(24, 13, 27, 13, 'black')
    scope(g, 17, 31, 4)
    return g

def rifle_semi():
    g = G()
    g.P([(0, 6), (14, 7), (14, 12), (0, 14)], 'black')   # thumbhole stock
    g.X(6, 9, 9, 10)
    g.R(0, 6, 0, 14, 'black', 'd')
    g.R(2, 7, 8, 7, 'black', 'l')                # cheek rest
    g.R(14, 7, 30, 11, 'black')                  # receiver
    g.R(31, 8, 56, 9, 'black')                   # barrel
    g.R(31, 8, 45, 11, 'black')                  # handguard
    for x in range(33, 44, 3): g.D(x, 10, 'black', 'x')
    g.R(55, 7, 57, 10, 'black')                  # flash hider
    scope(g, 17, 32, 3)
    g.R(23, 12, 26, 17, 'black')                 # magazine
    pgrip(g, 15, 12, 'black', h=6, w=4, slant=1)
    tguard(g, 19, 12)
    return g

# ---------- machine pistols ----------
def tmp():
    g = G()
    g.R(4, 5, 22, 9, 'black')                    # receiver
    g.R(6, 4, 15, 4, 'black', 'l')               # top rail
    g.R(23, 6, 28, 7, 'black'); g.D(27, 5, 'black', 'd')
    g.D(8, 3, 'steel'); g.D(9, 3, 'steel')       # cocking handle
    g.P([(6, 10), (11, 10), (10, 18), (5, 18)], 'black')   # grip with mag
    g.R(6, 19, 9, 22, 'black'); g.R(7, 20, 8, 21, 'black', 'd')
    tguard(g, 11, 10)
    g.R(18, 10, 20, 15, 'black')                 # front vertical grip
    for y in (11, 13): g.D(19, y, 'black', 'd')
    return g

def chicago():
    g = G()
    rifle_stock(g, 14, 'wood', top=8, butt=15, wb=12)
    g.R(14, 7, 30, 11, 'black')
    g.R(31, 8, 46, 9, 'black')
    for x in range(32, 40, 2): g.R(x, 7, x, 10, 'black', 'd')   # finned barrel
    g.R(44, 7, 47, 10, 'black')                  # compensator
    pgrip(g, 15, 12, 'wood', h=6, w=4, slant=1)
    g.C(25, 17, 5, 'black'); g.C(25, 17, 2, 'black', 'd')       # 100-round drum
    g.D(25, 13, 'steel'); g.D(25, 21, 'steel')
    g.P([(36, 10), (40, 10), (40, 16), (36, 16)], 'wood')      # vertical foregrip
    g.R(20, 5, 21, 6, 'black')
    g.R(22, 8, 26, 8, 'brass')                   # brass bolt shine
    tguard(g, 19, 12)
    return g

# ---------- special ----------
def mine_thrower():
    g = G()
    rifle_stock(g, 12, 'olive', top=8, butt=15, wb=12)
    g.R(12, 7, 21, 11, 'black')                  # receiver
    g.R(22, 5, 32, 13, 'olive')                  # revolving cylinder
    for x in (24, 27, 30): g.R(x, 6, x, 12, 'olive', 'd')
    g.R(33, 7, 46, 10, 'black')                  # wide barrel
    g.R(46, 6, 49, 11, 'black')                  # muzzle
    g.R(50, 8, 51, 9, 'red')                     # dart tip
    g.R(14, 5, 19, 6, 'black')                   # sight
    pgrip(g, 13, 12, 'black', h=6, w=4, slant=1)
    tguard(g, 17, 12)
    return g

def rocket_launcher():
    g = G()
    g.R(0, 6, 48, 10, 'olive')                   # launch tube
    g.R(0, 5, 3, 11, 'black'); g.R(45, 5, 48, 11, 'black')   # end caps
    g.R(31, 6, 31, 10, 'brass')                  # stripe
    g.R(11, 3, 12, 5, 'black'); g.R(35, 3, 36, 5, 'black')  # flip-up sights
    g.R(16, 11, 26, 12, 'olive')                 # trigger housing
    pgrip(g, 18, 13, 'black', h=5, w=3, slant=1)
    g.R(5, 11, 8, 11, 'black')                   # sling stud
    return g

def knife():
    g = G(40, 40)
    g.P([(9, 11), (19, 2), (22, 1), (21, 4), (11, 13)], 'steel')   # blade
    g.L(12, 10, 19, 3, 'steel', 'h')                                # edge shine
    g.L(6, 9, 12, 15, 'black'); g.L(7, 9, 13, 15, 'black')          # cross guard
    g.P([(1, 18), (6, 13), (8, 15), (3, 20)], 'black')              # handle
    for i in range(3): g.D(3+i*2, 17-i*2, 'black', 'd')
    g.D(0, 20, 'metal'); g.D(1, 20, 'metal'); g.D(1, 21, 'metal')  # pommel
    return g
