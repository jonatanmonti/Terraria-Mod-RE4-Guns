using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Shotguns
{
    // Riot Gun - Resident Evil 4 (Shotgun)
    public class RiotGun : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 18,
            UseTime = 40,
            Knockback = 5.5f,
            Velocity = 9f,
            Crit = 0,
            Spread = 12f,
            AmmoSaveChance = 0f,
            Pellets = 6,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 49,
            Height = 15,
            HoldoutX = -6f,
            MuzzleOffset = 37f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item36;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:CobaltBar", 12);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
