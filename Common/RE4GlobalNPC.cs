using Terraria;
using Terraria.GameContent.ItemDropRules;
using Terraria.ID;
using Terraria.ModLoader;

namespace RE4Weapons.Common
{
    // The Arms Dealer plays the RE4 Merchant: more guns unlock as bosses go down. Some enemies drop rare guns.
    public class RE4GlobalNPC : GlobalNPC
    {
        public override void ModifyShop(NPCShop shop)
        {
            if (shop.NpcType == NPCID.ArmsDealer)
            {
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Handguns.Handgun>());
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Handguns.Punisher>(), Condition.DownedEyeOfCthulhu);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Shotguns.Shotgun>(), Condition.DownedEyeOfCthulhu);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Handguns.Red9>(), Condition.DownedEowOrBoc);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Handguns.Blacktail>(), Condition.DownedSkeletron);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Rifles.Rifle>(), Condition.DownedSkeletron);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.MachinePistols.TMP>(), Condition.DownedSkeletron);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Shotguns.RiotGun>(), Condition.Hardmode);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Handguns.Matilda>(), Condition.Hardmode);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Magnums.BrokenButterfly>(), Condition.DownedMechBossAny);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Special.MineThrower>(), Condition.DownedMechBossAny);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Rifles.RifleSemiAuto>(), Condition.DownedMechBossAny);
                shop.Add(ModContent.ItemType<global::RE4Weapons.Content.Items.Special.RocketLauncher>(), Condition.DownedMechBossAll);
            }
        }

        public override void ModifyNPCLoot(NPC npc, NPCLoot npcLoot)
        {
            if (npc.type == NPCID.TacticalSkeleton)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::RE4Weapons.Content.Items.Magnums.Killer7>(), 12));
            if (npc.type == NPCID.SkeletonCommando)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::RE4Weapons.Content.Items.Special.RocketLauncher>(), 10));
            if (npc.type == NPCID.PirateDeadeye)
                npcLoot.Add(ItemDropRule.Common(ModContent.ItemType<global::RE4Weapons.Content.Items.Shotguns.Striker>(), 20));
        }
    }
}
