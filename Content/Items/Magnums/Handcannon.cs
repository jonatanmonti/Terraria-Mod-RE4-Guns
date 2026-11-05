using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Magnums
{
    // Handcannon - Resident Evil 4 (Magnum)
    public class Handcannon : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 240,
            UseTime = 40,
            Knockback = 10f,
            Velocity = 15f,
            Crit = 15,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 4,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Yellow,
            BuyPriceGold = 80,
            Width = 45,
            Height = 20,
            HoldoutX = -5f,
            MuzzleOffset = 34f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40 with { Pitch = -0.35f };

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
