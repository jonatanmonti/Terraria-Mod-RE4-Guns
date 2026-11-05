using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Handguns
{
    // Red9 - Resident Evil 4 (Handgun)
    public class Red9 : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 24,
            UseTime = 20,
            Knockback = 3.5f,
            Velocity = 11f,
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
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 34,
            Height = 20,
            HoldoutX = -2f,
            MuzzleOffset = 26f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:EvilBar", 12);
            recipe.AddRecipeGroup(RecipeGroupID.IronBar, 6);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
