using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.MachinePistols
{
    // TMP - Resident Evil 4 (Submachine gun)
    public class TMP : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 9,
            UseTime = 5,
            Knockback = 1.0f,
            Velocity = 9f,
            Crit = 0,
            Spread = 8f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Orange,
            BuyPriceGold = 10,
            Width = 27,
            Height = 22,
            HoldoutX = 2f,
            MuzzleOffset = 20f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item11;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddIngredient(ItemID.MeteoriteBar, 12);
            recipe.AddIngredient(ItemID.HellstoneBar, 6);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
