import os, shutil
from roster import ROSTER
from stats import *
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items_dir = f'{OUT}/Content/Items'
shutil.rmtree(items_dir, ignore_errors=True)
CAT = {c[0]: c[3] for c in ROSTER}

def ing(code, n):
    k, v = code.split(':')
    if k in ('G', 'V'): return f'recipe.AddRecipeGroup(RecipeGroupID.{v}, {n});'
    if k == 'C': return f'recipe.AddRecipeGroup("RE4Weapons:{v}", {n});'
    return f'recipe.AddIngredient(ItemID.{v}, {n});'

def f(x): return f'{x}f'

HEAD = '''using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.{cat}
{{
    // {name} - Resident Evil 4 ({typ})
'''

loc_en, loc_es = [], []
for cls, name, name_es, cat, fn in ROSTER:
    img = fn().render()
    d = f'{items_dir}/{cat}'; os.makedirs(d, exist_ok=True)
    img.save(f'{d}/{cls}.png')
    tier,typ,dmg,ut,kb,vel,crit,spread,save,pellets,pierce,scope,auto,snd,burst,delay = STATS[cls]
    ings, tile, rare, gold = TIERS[tier]
    w, h = img.size
    head = HEAD.format(cat=cat, name=name, typ=TYPE_EN[typ])
    if typ == K:
        kings, ktile = KNIFE_RECIPE
        recipe = '\n            '.join(ing(c, n) for c, n in kings)
        code = head + f'''    public class {cls} : ModItem
    {{
        public override void SetStaticDefaults()
        {{
            Item.ResearchUnlockCount = 1;
        }}

        public override void SetDefaults()
        {{
            Item.width = {w};
            Item.height = {h};
            Item.DamageType = DamageClass.Melee;
            Item.damage = {dmg};
            Item.knockBack = {f(kb)};
            Item.crit = {crit};
            Item.useStyle = ItemUseStyleID.Swing;
            Item.useTime = {ut};
            Item.useAnimation = {ut};
            Item.autoReuse = {str(auto).lower()};
            Item.UseSound = {SOUNDS[snd]};
            Item.rare = {rare};
            Item.value = Item.buyPrice(gold: {gold});
        }}

        public override void AddRecipes()
        {{
            Recipe recipe = CreateRecipe();
            {recipe}
            recipe.AddTile({ktile});
            recipe.Register();
        }}
    }}
}}
'''
    else:
        hold = 2 if w < 32 else -round((w - 28) * 0.3)
        muzzle = max(12, round(w * 0.75))
        recipe = '\n            '.join(ing(c, n) for c, n in ings)
        code = head + f'''    public class {cls} : RE4Gun
    {{
        private static readonly GunData data = new GunData
        {{
            Damage = {dmg},
            UseTime = {ut},
            Knockback = {f(kb)},
            Velocity = {f(vel)},
            Crit = {crit},
            Spread = {f(spread)},
            AmmoSaveChance = {f(save)},
            Pellets = {pellets},
            ExtraPierce = {pierce},
            Scope = {str(scope).lower()},
            AutoReuse = {str(auto).lower()},
            Burst = {burst},
            ReuseDelay = {delay},
            Launcher = {LAUNCHER.get(cls, '0')},
            Rarity = {rare},
            BuyPriceGold = {gold},
            Width = {w},
            Height = {h},
            HoldoutX = {f(hold)},
            MuzzleOffset = {f(muzzle)},
        }};

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => {SOUNDS[snd]};

        public override void AddRecipes()
        {{
            Recipe recipe = CreateRecipe();
            {recipe}
            recipe.AddTile({tile});
            recipe.Register();
        }}
    }}
}}
'''
    open(f'{d}/{cls}.cs', 'w', encoding='utf-8').write(code)
    extra_en, extra_es = [], []
    if save >= 1: extra_en.append('Infinite ammo'); extra_es.append('Munición infinita')
    elif save: extra_en.append(f'{int(save*100)}% chance not to consume ammo'); extra_es.append(f'{int(save*100)}% de probabilidad de no gastar munición')
    if burst > 1: extra_en.append(f'Fires {burst}-round bursts'); extra_es.append(f'Dispara ráfagas de {burst} balas')
    if pellets > 1: extra_en.append(f'Fires {pellets} pellets'); extra_es.append(f'Dispara {pellets} perdigones')
    if pierce: extra_en.append(f'Bullets pierce {pierce} extra enemies'); extra_es.append(f'Las balas atraviesan {pierce} enemigo(s) extra')
    if scope: extra_en.append('Right click to zoom out'); extra_es.append('Clic derecho para hacer zoom')
    if typ == MT: extra_en.append('Fires sticky proximity mines'); extra_es.append('Dispara minas de proximidad')
    if typ == K: ammo_en, ammo_es = [], []
    elif cls in LAUNCHER: ammo_en, ammo_es = ['Uses rockets'], ['Usa cohetes']
    else: ammo_en, ammo_es = ['Uses bullets'], ['Usa balas']
    tt_en = '\\n'.join([f'Resident Evil 4 - {TYPE_EN[typ]}'] + extra_en + ammo_en)
    tt_es = '\\n'.join([f'Resident Evil 4 - {TYPE_ES[typ]}'] + extra_es + ammo_es)
    loc_en.append(f'\t\t{cls}: {{\n\t\t\tDisplayName: "{name}"\n\t\t\tTooltip: "{tt_en}"\n\t\t}}\n')
    loc_es.append(f'\t\t{cls}: {{\n\t\t\tDisplayName: "{name_es}"\n\t\t\tTooltip: "{tt_es}"\n\t\t}}\n')

os.makedirs(f'{OUT}/Localization', exist_ok=True)
groups_en = {'SilverBar':'Any Silver Bar','EvilBar':'Any Demonite or Crimtane Bar','CobaltBar':'Any Cobalt Bar','MythrilBar':'Any Mythril Bar','AdamantiteBar':'Any Adamantite Bar'}
groups_es = {'SilverBar':'Cualquier lingote de plata','EvilBar':'Cualquier lingote de demonita o carmesí','CobaltBar':'Cualquier lingote de cobalto','MythrilBar':'Cualquier lingote de mithril','AdamantiteBar':'Cualquier lingote de adamantita'}
for lang, items, groups in (('en-US', loc_en, groups_en), ('es-ES', loc_es, groups_es)):
    g = ''.join(f'\t\t{k}: {v}\n' for k, v in groups.items())
    open(f'{OUT}/Localization/{lang}_Mods.RE4Weapons.hjson', 'w', encoding='utf-8').write(
        'Mods: {\n\tRE4Weapons: {\n\t\tItems: {\n' + ''.join('\t' + l.replace('\n\t', '\n\t\t') for l in items) +
        '\t\t}\n\n\t\tRecipeGroups: {\n' + g.replace('\t\t', '\t\t\t') + '\t\t}\n\t}\n}\n')

def ref(k): return f'ModContent.ItemType<global::RE4Weapons.Content.Items.{CAT[k]}.{k}>()'
shop = '\n'.join(f'                shop.Add({ref(k)}{", " + v if v else ""});' for k, v in SHOP.items())
drops = '\n'.join(f'            if (npc.type == {n})\n                npcLoot.Add(ItemDropRule.Common({ref(k)}, {c}));' for n, k, c in DROPS)
open(f'{OUT}/Common/RE4GlobalNPC.cs', 'w', encoding='utf-8').write(f'''using Terraria;
using Terraria.GameContent.ItemDropRules;
using Terraria.ID;
using Terraria.ModLoader;

namespace RE4Weapons.Common
{{
    // The Arms Dealer plays the RE4 Merchant: more guns unlock as bosses go down. Some enemies drop rare guns.
    public class RE4GlobalNPC : GlobalNPC
    {{
        public override void ModifyShop(NPCShop shop)
        {{
            if (shop.NpcType == NPCID.ArmsDealer)
            {{
{shop}
            }}
        }}

        public override void ModifyNPCLoot(NPC npc, NPCLoot npcLoot)
        {{
{drops}
        }}
    }}
}}
''')
print('generated', len(ROSTER))
