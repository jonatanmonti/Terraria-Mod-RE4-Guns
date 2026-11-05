using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Rifles
{
    // Rifle (semi-auto) - Resident Evil 4 (Semi-automatic rifle)
    public class RifleSemiAuto : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 62,
            UseTime = 22,
            Knockback = 5.0f,
            Velocity = 15f,
            Crit = 15,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 1,
            Scope = true,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Pink,
            BuyPriceGold = 28,
            Width = 60,
            Height = 19,
            HoldoutX = -10f,
            MuzzleOffset = 45f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

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
