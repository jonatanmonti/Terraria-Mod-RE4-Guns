using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Special
{
    // Rocket Launcher - Resident Evil 4 (Rocket launcher)
    public class RocketLauncher : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 120,
            UseTime = 50,
            Knockback = 8.0f,
            Velocity = 10f,
            Crit = 0,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = ItemID.RocketLauncher,
            Rarity = ItemRarityID.Lime,
            BuyPriceGold = 60,
            Width = 51,
            Height = 18,
            HoldoutX = -7f,
            MuzzleOffset = 38f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11 with { Pitch = -0.5f };

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.HallowedBar, 15);
            recipe.AddIngredient(ItemID.SoulofMight, 10);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}
