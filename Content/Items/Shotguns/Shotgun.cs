using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Shotguns
{
    // Shotgun - Resident Evil 4 (Shotgun)
    public class Shotgun : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 10,
            UseTime = 45,
            Knockback = 5.0f,
            Velocity = 8f,
            Crit = 0,
            Spread = 16f,
            AmmoSaveChance = 0f,
            Pellets = 5,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 57,
            Height = 11,
            HoldoutX = -9f,
            MuzzleOffset = 43f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item36;

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
