using Terraria;
using Terraria.ID;
using Terraria.Localization;
using Terraria.ModLoader;

namespace RE4Weapons.Common
{
    /// <summary>"Any X Bar" groups so both ore variants of a world can craft the guns.</summary>
    public class RE4RecipeGroups : ModSystem
    {
        public override void AddRecipeGroups()
        {
            Register("SilverBar", ItemID.SilverBar, ItemID.TungstenBar);
            Register("EvilBar", ItemID.DemoniteBar, ItemID.CrimtaneBar);
            Register("CobaltBar", ItemID.CobaltBar, ItemID.PalladiumBar);
            Register("MythrilBar", ItemID.MythrilBar, ItemID.OrichalcumBar);
            Register("AdamantiteBar", ItemID.AdamantiteBar, ItemID.TitaniumBar);
        }

        private static void Register(string key, params int[] items)
        {
            LocalizedText name = Language.GetOrRegister($"Mods.RE4Weapons.RecipeGroups.{key}");
            RecipeGroup group = new RecipeGroup(() => name.Value, items);
            RecipeGroup.RegisterGroup($"RE4Weapons:{key}", group);
        }
    }
}
