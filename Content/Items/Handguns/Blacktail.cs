using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Handguns
{
    // Blacktail - Resident Evil 4 (Handgun)
    public class Blacktail : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 20,
            UseTime = 11,
            Knockback = 2.5f,
            Velocity = 10f,
            Crit = 6,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Orange,
            BuyPriceGold = 10,
            Width = 23,
            Height = 17,
            HoldoutX = 2f,
            MuzzleOffset = 17f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

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
