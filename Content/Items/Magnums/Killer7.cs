using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using RE4Weapons.Common;

namespace RE4Weapons.Content.Items.Magnums
{
    // Killer7 - Resident Evil 4 (Magnum)
    public class Killer7 : RE4Gun
    {
        private static readonly GunData data = new GunData
        {
            Damage = 80,
            UseTime = 22,
            Knockback = 6.5f,
            Velocity = 13f,
            Crit = 10,
            Spread = 0f,
            AmmoSaveChance = 0f,
            Pellets = 1,
            ExtraPierce = 1,
            Scope = false,
            AutoReuse = false,
            Burst = 1,
            ReuseDelay = 0,
            Launcher = 0,
            Rarity = ItemRarityID.LightPurple,
            BuyPriceGold = 40,
            Width = 26,
            Height = 18,
            HoldoutX = 2f,
            MuzzleOffset = 20f,
        };

        protected override GunData Data => data;
        protected override Terraria.Audio.SoundStyle Sound => SoundID.Item40 with { Pitch = -0.35f };

        public override void AddRecipes()
        {
            Recipe recipe = CreateRecipe();
            recipe.AddRecipeGroup("RE4Weapons:AdamantiteBar", 14);
            recipe.AddIngredient(ItemID.SoulofNight, 8);
            recipe.AddIngredient(ItemID.IllegalGunParts, 1);
            recipe.AddTile(TileID.MythrilAnvil);
            recipe.Register();
        }
    }
}
