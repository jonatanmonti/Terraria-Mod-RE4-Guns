using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Handguns
{
    // Handgun - Resident Evil 4 (Handgun)
    public class Handgun : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 11,
            UseTime = 15,
            Knockback = 2.0f,
            Velocity = 9f,
            Crit = 4,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.White,
            BuyPriceGold = 1,
            Width = 20,
            Height = 16,
            HoldoutX = 2f,
            MuzzleOffset = 15f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup(RecipeGroupID.IronBar, 10);
            recipe.AddRecipeGroup(RecipeGroupID.Wood, 5);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
