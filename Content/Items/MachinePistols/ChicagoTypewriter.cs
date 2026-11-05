using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.MachinePistols
{
    // Chicago Typewriter - Resident Evil 4 (Submachine gun)
    public class ChicagoTypewriter : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 40,
            UseTime = 5,
            Knockback = 2.0f,
            Velocity = 12f,
            Crit = 4,
            Spread = 4f,
            AmmoSaveChance = 1f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Yellow,
            BuyPriceGold = 80,
            Width = 50,
            Height = 20,
            HoldoutX = -7f,
            MuzzleOffset = 38f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.ChlorophyteBar, 15);
            recipe.AddIngredient(ItemID.Ectoplasm, 6);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}
