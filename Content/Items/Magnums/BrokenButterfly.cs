using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Magnums
{
    // Broken Butterfly - Resident Evil 4 (Magnum)
    public class BrokenButterfly : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 85,
            UseTime = 32,
            Knockback = 7.0f,
            Velocity = 13f,
            Crit = 10,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 2,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 38,
            Height = 19,
            HoldoutX = -3f,
            MuzzleOffset = 28f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40 with { Pitch = -0.35f };

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
