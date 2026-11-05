using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Handguns
{
    // Matilda - Resident Evil 4 (Machine pistol)
    public class Matilda : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 16,
            UseTime = 4,
            Knockback = 1.5f,
            Velocity = 10f,
            Crit = 2,
            Spread = 3f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 0,
            Scope = false,
            AutoReuse = true,
            Burst = 3,
            ReuseDelay = 14,
            Launcher = 0,
            Rarity = ItemRarityID.LightRed,
            BuyPriceGold = 18,
            Width = 33,
            Height = 22,
            HoldoutX = -2f,
            MuzzleOffset = 25f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item41;

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:CobaltBar", 12);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.Anvils);
            recipe.Register();
        }
    }
}
