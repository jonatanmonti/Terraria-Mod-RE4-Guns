using Microsoft.Xna.Framework;
using Terraria;
using Terraria.Audio;
using Terraria.DataStructures;
using Terraria.ID;
using Terraria.ModLoader;

namespace RE4Weapons.Common
{
    /// <summary>Stats for one gun. Each weapon class fills one of these.</summary>
    public class GunData
    {
        public int Damage;
        public int UseTime;
        public float Knockback;
        public float Velocity;
        public int Crit;
        public float Spread;          // max random spread, in degrees
        public float AmmoSaveChance;  // 0..1 chance to not consume ammo (1 = infinite ammo)
        public int Pellets = 1;       // >1 = shotgun
        public int ExtraPierce;       // extra enemies each bullet passes through
        public bool Scope;            // right click zoom like the Rifle Scope
        public bool AutoReuse;
        public int Burst = 1;         // >1 = shots per trigger pull (Matilda)
        public int ReuseDelay;        // pause after a burst
        public int Launcher;          // vanilla launcher whose rocket projectiles this weapon uses (0 = bullets)
        public int Rarity;
        public int BuyPriceGold;
        public int Width;
        public int Height;
        public float HoldoutX;
        public float MuzzleOffset;
    }

    /// <summary>
    /// Shared behaviour for every RE4 gun: ranged damage, uses vanilla bullets (or rockets for launchers),
    /// spread, ammo saving, shotgun pellets, piercing and burst fire.
    /// </summary>
    public abstract class RE4Gun : ModItem
    {
        protected abstract GunData Data { get; }
        protected abstract SoundStyle Sound { get; }

        public override void SetStaticDefaults()
        {
            Item.ResearchUnlockCount = 1; // Journey mode
            if (Data.Launcher > 0)
                AmmoID.Sets.SpecificLauncherAmmoProjectileFallback[Type] = Data.Launcher;
        }

        public override void SetDefaults()
        {
            GunData d = Data;
            Item.width = d.Width;
            Item.height = d.Height;

            Item.DamageType = DamageClass.Ranged;
            Item.damage = d.Damage;
            Item.knockBack = d.Knockback;
            Item.crit = d.Crit;
            Item.noMelee = true;

            Item.useStyle = ItemUseStyleID.Shoot;
            Item.useTime = d.UseTime;
            Item.useAnimation = d.UseTime * d.Burst;
            Item.reuseDelay = d.ReuseDelay;
            Item.autoReuse = d.AutoReuse;
            Item.UseSound = d.Burst > 1 ? null : Sound; // burst guns play the sound on every shot

            Item.shootSpeed = d.Velocity;
            if (d.Launcher > 0)
            {
                Item.shoot = ProjectileID.RocketI;
                Item.useAmmo = AmmoID.Rocket;
            }
            else
            {
                // Standard gun setup: the real projectile comes from the ammo.
                Item.shoot = ProjectileID.PurificationPowder;
                Item.useAmmo = AmmoID.Bullet;
            }

            Item.rare = d.Rarity;
            Item.value = Item.buyPrice(gold: d.BuyPriceGold);
        }

        public override Vector2? HoldoutOffset() => new Vector2(Data.HoldoutX, 0f);

        public override bool CanConsumeAmmo(Item ammo, Player player)
            => Main.rand.NextFloat() >= Data.AmmoSaveChance;

        public override void HoldItem(Player player)
        {
            if (Data.Scope)
                player.scope = true;
        }

        public override void ModifyShootStats(Player player, ref Vector2 position, ref Vector2 velocity, ref int type, ref int damage, ref float knockback)
        {
            // Spawn the bullet at the muzzle instead of the player's hand.
            Vector2 muzzle = Vector2.Normalize(velocity) * Data.MuzzleOffset;
            if (Collision.CanHit(position, 0, 0, position + muzzle, 0, 0))
                position += muzzle;

            if (Data.Pellets <= 1 && Data.Spread > 0f)
                velocity = velocity.RotatedByRandom(MathHelper.ToRadians(Data.Spread));
        }

        public override bool Shoot(Player player, EntitySource_ItemUse_WithAmmo source, Vector2 position, Vector2 velocity, int type, int damage, float knockback)
        {
            GunData d = Data;
            if (d.Burst > 1)
                SoundEngine.PlaySound(Sound, player.position);

            if (d.Pellets > 1)
            {
                for (int i = 0; i < d.Pellets; i++)
                {
                    Vector2 v = velocity.RotatedByRandom(MathHelper.ToRadians(d.Spread)) * Main.rand.NextFloat(0.85f, 1.1f);
                    Projectile.NewProjectile(source, position, v, type, damage, knockback, player.whoAmI);
                }
                return false;
            }

            if (d.ExtraPierce > 0)
            {
                int p = Projectile.NewProjectile(source, position, velocity, type, damage, knockback, player.whoAmI);
                Projectile proj = Main.projectile[p];
                if (proj.penetrate > 0)
                    proj.penetrate += d.ExtraPierce;
                proj.usesLocalNPCImmunity = true;
                proj.localNPCHitCooldown = -1; // each enemy is hit once per bullet
                return false;
            }

            return true;
        }
    }
}
