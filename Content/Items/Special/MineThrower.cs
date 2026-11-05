using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Special
{
    // Mine Thrower - Resident Evil 4 (Mine launcher)
    public class MineThrower : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 45,
            UseTime = 35,
            Knockback = 4.0f,
            Velocity = 8f,
            Crit = 0,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = ItemID.ProximityMineLauncher,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 54,
            Height = 16,
            HoldoutX = -8f,
            MuzzleOffset = 40f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item61;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:MythrilBar", 12);
            recipe.AddIngredient(ItemID.SoulofNight, 6);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}
