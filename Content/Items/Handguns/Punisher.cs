using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Handguns
{
    // Punisher - Resident Evil 4 (Handgun)
    public class Punisher : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 13,
            UseTime = 16,
            Knockback = 2.5f,
            Velocity = 10f,
            Crit = 4,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 2,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Blue,
            BuyPriceGold = 3,
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
            recipe.AddRecipeGroup("RE4Weapons:SilverBar", 12);
            recipe.AddRecipeGroup(RecipeGroupID.Wood, 8);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
