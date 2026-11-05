using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Shotguns
{
    // Striker - Resident Evil 4 (Shotgun)
    public class Striker : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 24,
            UseTime = 22,
            Knockback = 5.0f,
            Velocity = 9f,
            Crit = 0,
            Spread = 13f,
            AmmoSaveChance = 0f,
            Pellets = 6,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 46,
            Height = 17,
            HoldoutX = -5f,
            MuzzleOffset = 34f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item36;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:AdamantiteBar", 14);
            recipe.AddIngredient(ItemID.SoulofNight, 8);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}
