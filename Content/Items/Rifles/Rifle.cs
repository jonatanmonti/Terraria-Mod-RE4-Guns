using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Rifles
{
    // Rifle - Resident Evil 4 (Bolt-action rifle)
    public class Rifle : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 40,
            UseTime = 42,
            Knockback = 5.0f,
            Velocity = 13f,
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
            Rarity = ItemRarityID.Green,
            BuyPriceGold = 6,
            Width = 65,
            Height = 15,
            HoldoutX = -11f,
            MuzzleOffset = 49f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40;

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
