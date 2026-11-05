import math, random, os
from PIL import Image, ImageDraw
from roster import ROSTER
from stats import STATS, TYPE_EN, CAT_EN
import font
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = f'{OUT}/workshop'; os.makedirs(WS, exist_ok=True)
sprite = {c: f().render() for c, _, _, _, f in ROSTER}
def lerp(a, b, t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

def scene(W, H, seed=1, top=(30,18,22), bot=(150,70,40), moon=None):
    """Dusk over a rural village: banded sky, moon, hills, houses and church silhouettes, dirt road."""
    random.seed(seed)
    img = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(img)
    for y in range(H):
        t = min(1, int(y / H * 12) / 12 * 1.2)
        d.line([(0, y), (W, y)], fill=lerp(top, bot, t))
    if moon: d.ellipse([moon[0]-9, moon[1]-9, moon[0]+9, moon[1]+9], fill=(236, 214, 170))
    for layer, col, base, amp in ((0, (58, 34, 34), 0.60, 12), (1, (40, 26, 26), 0.70, 8)):
        ph = random.random() * 10
        for x in range(W):
            h = int(H*base + math.sin(x/23+ph)*amp*0.6 + math.sin(x/9+ph*2)*amp*0.25)
            d.line([(x, h), (x, H)], fill=col)
    gy = H - 14; hc = (24, 16, 16)
    x = random.randint(0, 20)
    while x < W:
        w = random.randint(14, 24); h = random.randint(8, 14)
        d.rectangle([x, gy-h, x+w, gy], fill=hc)
        d.polygon([(x-2, gy-h), (x+w//2, gy-h-6), (x+w+2, gy-h)], fill=hc)
        if random.random() < 0.5: d.rectangle([x+4, gy-h+3, x+6, gy-h+5], fill=(230, 160, 60))
        if random.random() < 0.15:
            d.rectangle([x+w+4, gy-30, x+w+10, gy], fill=hc); d.line([(x+w+7, gy-38), (x+w+7, gy-30)], fill=hc)
            d.line([(x+w+5, gy-35), (x+w+9, gy-35)], fill=hc); x += 10
        x += w + random.randint(10, 40)
    for x in range(W):
        d.line([(x, gy), (x, H)], fill=(96, 70, 46)); d.point((x, gy), fill=(120, 96, 60))
    for _ in range(W*2):
        d.point((random.randint(0, W-1), random.randint(gy+2, H-1)), fill=random.choice([(80, 58, 38), (120, 90, 60), (70, 66, 60)]))
    return img

def panel(img, x0, y0, x1, y1):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle([x0, y0, x1, y1], fill=(30, 22, 20, 210), outline=(10, 6, 6, 255))
    d.rectangle([x0+1, y0+1, x1-1, y1-1], outline=(150, 40, 34, 255))
    img.alpha_composite(ov)

def up(img, s): return img.resize((img.width*s, img.height*s), Image.NEAREST)
RED = (210, 40, 34); SH = (30, 6, 6)

ic = scene(80, 80, seed=3)
d = ImageDraw.Draw(ic)
font.text(ic, (80 - font.width('RE4', 3)) // 2, 5, 'RE4', RED, 3, shadow=SH)
g = sprite['Red9']; ic.alpha_composite(g, ((80 - g.width) // 2, 31))
font.text(ic, (80 - font.width('GUNS', 2)) // 2, 57, 'GUNS', (240, 230, 220), 2, shadow=SH)
d.rectangle([0, 0, 79, 79], outline=(14, 8, 8)); d.rectangle([1, 1, 78, 78], outline=(150, 40, 34))
ic.save(f'{OUT}/icon.png'); up(ic, 6).save(f'{OUT}/icon_workshop.png')

cv = scene(480, 270, seed=7, moon=(452, 92))
font.text(cv, (480 - font.width('RE4 WEAPONS', 5)) // 2, 12, 'RE4 WEAPONS', RED, 5, shadow=SH)
sub = '18 WEAPONS FROM RESIDENT EVIL 4'
font.text(cv, (480 - font.width(sub, 2)) // 2, 56, sub, (240, 230, 220), 2, shadow=SH)
show = ['Red9', 'Striker', 'Handcannon', 'ChicagoTypewriter', 'RifleSemiAuto', 'BrokenButterfly', 'Matilda', 'RocketLauncher', 'Blacktail']
for n, k in enumerate(show):
    sp = up(sprite[k], 2); cx = 80 + (n % 3) * 160; cy = 104 + (n // 3) * 46
    cv.alpha_composite(sp, (cx - sp.width // 2, cy - sp.height // 2 + 10))
up(cv, 4).save(f'{WS}/01_cover.png')

cats = ['Handguns', 'Shotguns', 'Rifles', 'MachinePistols', 'Magnums', 'Special']
for i, c in enumerate(cats, start=2):
    im = scene(480, 270, seed=10+i); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 479, 24], fill=(110, 24, 20)); d.line([(0, 25), (479, 25)], fill=(14, 8, 8))
    font.text(im, 8, 5, CAT_EN[c].upper(), (255, 255, 255), 2, shadow=SH)
    font.text(im, 480 - font.width('RE4 WEAPONS', 2) - 8, 5, 'RE4 WEAPONS', (255, 200, 120), 2, shadow=SH)
    guns = [r for r in ROSTER if r[3] == c]
    for j, (cls, disp, _, _, _) in enumerate(guns):
        col, row = j % 2, j // 2
        x0, y0 = 6 + col * 236, 31 + row * 79
        panel(im, x0, y0, x0 + 231, y0 + 75)
        st = STATS[cls]
        font.text(im, x0 + 5, y0 + 5, disp.replace('(', '').replace(')', ''), (255, 255, 255), 1, shadow=(10, 4, 4))
        font.text(im, x0 + 5, y0 + 15, f'DMG {st[2]}', (255, 200, 80), 1)
        font.text(im, x0 + 5, y0 + 24, TYPE_EN[st[1]].upper(), (240, 150, 130), 1)
        sp = up(sprite[cls], 2)
        im.alpha_composite(sp, (x0 + 226 - sp.width, y0 + 72 - sp.height))
    up(im, 4).save(f'{WS}/{i:02d}_{c.lower()}.png')

cols = 6; cw, ch = 72, 30
sh = Image.new('RGBA', (cols*cw, 3*ch), (40, 26, 24, 255))
for i, (cls, _, _, _, _) in enumerate(ROSTER):
    sp = sprite[cls]
    sh.alpha_composite(sp, ((i % cols)*cw + (cw-sp.width)//2, (i//cols)*ch + (ch-sp.height)//2))
up(sh, 3).save(f'{WS}/all_guns.png')
print('done')
