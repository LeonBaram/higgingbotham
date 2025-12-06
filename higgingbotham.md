# Herbert Higgingbotham, PhD

_Professor Herbert Higgingbotham, PhD, head of anthropology at the Dunwall College of Liberal Arts_

Lore Bard '14'`:lvl`\
54-year-old Anthropologist; 'Lawful Good'`:alignment`

## Conditions

**Planar Alignment (Frontier 0):**

- only regain spell slots lvl1/lvl2/lvl3
- portable holes / bags of holding reset
- betrayer's tear is only a +1 focus (-2 on spell attacks and save DC)
    - '-2'`:BETRAYER_PENALTY=-2`
- earrings of protection disabled
- on each long rest, pass a CON save or max hp reduced by X, where X is a roll of your hit dice - current reduction of 0 hp

**proficiency bonus:** '+5'`:+prof`

## Stats

| stat  | score      | mod         | save              |
| ----- | ---------- | ----------- | ----------------- |
| STR   | '8'`:STR`  | '-1'`:str`  | '-1'`:=str`       |
| DEX\* | '16'`:DEX` | '+3'`:+dex` | '+8'`:+=dex+prof` |
| CON   | '14'`:CON` | '+2'`:+con` | '+2'`:+=con`      |
| INT   | '16'`:INT` | '+3'`:+int` | '+3'`:+=int`      |
| WIS   | '14'`:WIS` | '+2'`:+wis` | '+2'`:+=wis`      |
| CHA\* | '18'`:CHA` | '+4'`:+cha` | '+9'`:+=cha+prof` |

\*proficient save

## Combat

initiative: '+5'`:+=dex+prof//2`\
speed: 30\
armor class: '17'`:=14+dex` (Bardic Leathers)

''`:=reset(longrest)`\
hp: 14 / 100\
hit dice: 14d8 / '14d8'`:=fmt(lvl, "d8")`

temp hp: 0

**attacks:**

- rapier: '+8'`:+=dex+prof` to hit; damage: '1d8+3'`:=fmt('1d8+',dex)` piercing
- dagger: '+8'`:+=dex+prof` to hit; damage: '1d4+3'`:=fmt('1d4+',dex)` piercing (thrown)
    - range 60/240
- **Debt Collector (+2 revolver):**
    - to hit: '+10'`:+=dex+prof+2`
    - damage: '1d10+5'`:=fmt('1d10+',dex+2)` piercing
    - ammo: 156 bullets; 49 silver bullets(+1 ammo, +1d4 radiant)
    - range 60/240; reload 6; misfire 1
    - fragment count: 0; people killed without money: 0/3
    - engraving: D̵̓͒E̸͝͝B̸̛̏T̷̿̅S̶̛̎ ̶̌́G̵͝O BEYOND ̶̾̐W̴͝͝E̸̐͘ALTH

**Debt Collector: Money Drain**\
on a hit, target loses an amount of coins such that their "dollar" value is equal to the damage of the hit. The gun "makes change" in their pockets if necessary. The lost coins are transferred to your coin pouch (or equivalent). If the target has no material wealth (money, gems, etc), the gun deals an additional 3d10 force damage, and if the creature dies as a result, you receive a fragment of their soul.

## Resources

''`:=reset(longrest,shortrest)`\
**Bardic Inspiration:** 4d10 / '4d10'`:=fmt(cha,'d10')`

''`:=reset(longrest)`\
treacherous leech (cutting words on their save): 5 / '5'`:=prof`

> Upon doning the hat
> Those of the same ɹ̷̀͊ǝ̷͊͝s̷̾͝o̵̓̇u̴̿̀ɐ̷͌́u̵͝ɔǝ sᴉƃuɐʇnɹǝ as the original host
> Finds that their words cut deeper then ever before

''`:=reset(longrest)`\
betrayers last tear (whispers of doubt: disadvantage on initiative to '4'`:=cha` creatures): 1 / 1\
betrayers last tear (lingering malice: summon focus to myself): 1 / 1

spell-storing tattoos:

- 1x lvl3 absorb elements (fire)
- 1x lvl3 absorb elements (1 per element)
- 1x lvl1 gift of alacritty

''`:=reset(longrest)`\
free cast Fortune's Favor: 1 / 1

''`:=reset(longrest,shortrest)`\
use reaction to attempt to prevent misfire: 0 / 1

## Spells

''`:=reset(longrest)`

betrayers last tear bonus (to spell attack and save DC): '+3'`:+betrayer_bonus`\
(reduced to +1 by **planar alignment**)

spell attack bonus: '+10'`:+=cha + prof + betrayer_bonus + BETRAYER_PENALTY`\
spell save DC: '18'`:=8 + cha + prof + betrayer_bonus + BETRAYER_PENALTY`

**spell slots:**\
(levels 4-7 disabled due to **planar alignment**)

| lvl 1 | lvl 2 | lvl 3            | lvl 4 | lvl 5 | lvl 6 | lvl 7 |
| ----- | ----- | ---------------- | ----- | ----- | ----- | ----- |
| 4/4   | 3/3   | 2/2 (formerly 3) | 0/3   | 0/2   | 0/1   | 0/1   |

**spells:**

- cantrips:
    - vicious mockery (V)
    - friends (SM) <C>
    - minor illusion (SM)
    - mage hand (VS)
- lvl1:
    - silvery barbs (V)
    - command (V)
    - bane (VSM) <C>
    - unseen servant (VSM)
- lvl2:
    - calm emotions (VS) <C>
    - suggestion (VM)
    - silence (VS) <C>
    - shatter (VSM)
    - heat metal (VSM) <C>
    - mirror image (VS)
- lvl3:
    - dispel magic (VS)
    - counterspell (S)
- lvl4:
    - charm monster (VS)
    - dimension door (V)
    - greater invisibility (VS) <C>
    - death ward (VS)
- lvl5:
    - raise dead (VSM - diamond 500gp x 1)
    - modify memory (VS) <C>
    - holy weapon (VS) <C>
    - hold monster (VSM) <C>
    - greater restoration (VSM - diamond dust worth at least 100gp, which the spell consumes)
    - sunbeam (VSM) <C>
- lvl6:
    - mass suggestion (VM)
- lvl7:
    - etherealness (VS)
    - simulacrum (VSM - snow or ice in quantities sufficient to make a life-size copy of the duplicated creature; some hair, fingernail clippings, or other piece of that creature's body placed inside the snow or ice; and powdered ruby worth 1500gp, sprinkled over the duplicate and consumed by the spell)
    - regenerate (VSM)
    - teleport (V)

## Skills

expertise bonus: '+10'`:+expertise=prof*2`\
jack of all trades: '+2'`:+jack=prof//2`

**Note:** Advantage on survival checks

| skill           | bonus                   |
| --------------- | ----------------------- |
| athletics       | '+1'`:+=str+jack`       |
| acrobatics      | '+5'`:+=dex+jack`       |
| sleight of hand | '+5'`:+=dex+jack`       |
| stealth         | '+5'`:+=dex+jack`       |
| arcana          | '+13'`:+=int+expertise` |
| history         | '+8'`:+=int+prof`       |
| investigation   | '+13'`:+=int+expertise` |
| nature          | '+8'`:+=int+prof`       |
| religion        | '+8'`:+=int+prof`       |
| animal handling | '+4'`:+=wis+jack`       |
| insight         | '+12'`:+=wis+expertise` |
| medicine        | '+4'`:+=wis+jack`       |
| perception      | '+12'`:+=wis+expertise` |
| survival        | '+4'`:+=wis+jack`       |
| deception       | '+6'`:+=cha+jack`       |
| intimidation    | '+6'`:+=cha+jack`       |
| performance     | '+9'`:+=cha+prof`       |
| persuasion      | '+9'`:+=cha+prof`       |

bonus from **Observant** feat: '+5'`:+observant_feat=5`\
**passive perception:** '27'`:=10+wis+expertise + observant_feat`\
**passive investigation:** '28'`:=10+int+expertise + observant_feat`

languages known: shalben common, graveltalk, elvish, arcanum
armor proficiencies: light armor
weapon proficiencies: simple weapons, firearms, longsword, rapier, shortsword
tool proficiencies: singing stone (musical instrument), tinker's tools, archaeologist's tools

## Inventory

**money:** 506gp / 3,000 marks

**max weight (lb):** '120'`:=STR*15`\
**current weight (lb):** '100'`:=total_weight()`

```lua calcmd
inventory = [[
            compass of the vast golden serpent (MAGIC) (ATTUNED)
    2lb     betrayer's last tear (+3 SPELLCASTING FOCUS) (MAGIC) (ATTUNED)
            earring of protection (+1 to saves and AC) (MAGIC)
            hat ("The Treacherous Leech") (MAGIC) (ATTUNED)
            James's Dual Holsters (MAGIC)
            round eyeglasses (left lens broken)
    1lb     traveler's clothes
    1lb     singing rock (bardic focus)
    1lb     coin pouch
    1lb     ammo pouch
    3lb     Debt Collector (+2 revolver)
    2lb     rapier
    1lb     dagger
    10lb    Bardic Leathers (+2 studded leather - AC=14+dex) (MAGIC)
    13lb    studded leather armor (AC=12+dex)
            The Map (magic map from Anteverse B-1)
    5lb     backpack
    7lb     bedroll
    10lb    hemp rope (50 feet)
            ink bottle (1 ounce)
            ink pen
            sealing wax
5x          sheet of paper
5x  1lb     map/scroll case
    5lb     leather-bound diary
            vial of perfume
            soap
3x  2lb     oil lanterns
    1lb     oil lamp
2x  1lb     oil flask (capacity 1 pint)
    1lb     tinderbox
    1lb     torch
    1lb     mess kit
5x  2lb     day's worth of rations
    5lb     waterskin (capacity 4 pints)
            sapphire (worth 200gp)
            amethyst (100gp)
]]

left_at_home=[[
1lb mithril half-plate
37x small pieces of coal
calcified fragment
stun baton
]]
```

## Features

### Observant

- Increase your Intelligence or Wisdom by 1, to a maximum of 20.
- If you can see a creature's mouth while it is speaking a language you understand, you can interpret what it's saying by reading its lips.
- You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores.

### Warcaster

- You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.
- You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.
- When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature.

### Sharpshooter

- Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.
- Your ranged weapon attacks ignore half cover and three-quarters cover.
- Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage.

### Firearm Specialist

- if you misfire, you can use a reaction to roll a d20. if you roll higher than the misfire score, there is no misfire.
- when you attack with a one-handed weapon, if you're holding a loaded, light firearm, you can use a bonus action to attack with it

### Token of the Gloom

- "if you choose to succeed, you shall"

### Class Features

- song of rest (d10) (+1d10 hp when hit-dice healing on short rests)
- cutting words
    - when a creature you can see in 60ft of you makes an attack roll / ability check / damage roll, you can use your reaction to spend a **bardic inspiration**, roll it, and subtract it from the result. the creature is immune if it can't hear you, or is immune to charm.
- countercharm
    - as an action, you can start a performance until the end of your next turn. creatures in 30ft (_that can hear you_) of you gain advantage on saves against frighten / charm. ends early if you are incapacitated.

### Modified Simulacrum

- can create more than 1 simulacrum
- each additional simulacrum has 1hp
- each additional simulacrum cannot cast spells
- each additional simulacrum inherits some limited subset of my mental capabilities
- current count is 1 main, 10 additional

### Betrayer's Last Tear - Whispers of Doubt

When You roll initiative you can use your reaction to give a number of creatures equal to your Cha Modifier that you can see within 60 feet of you, disadvantage on their initiative roll Once you use this feature, you can't do so again until you finish a long rest.

### Betrayer's Last Tear - Lingering Malice

Once per Long rest you may spend ten minutes communing with the Red to summon the focus onto your person regardless of attunement.

### James's Dual Holsters (not currently active)

Spending an hour bonding a firearm to the holster will allow a duplicate firearm to appear in the other holster. Dual wielding said firearms allows for the wearer to make an extra attack if they do not have extra attack. the second firearm made with the holster has the same qualities as the bonded weapon.

### Compass of the Vast Golden Serpent

- can only be opened by attuned subject
- points to location of Gilded Leviathan
- advantage on Survival checks
- \+2 to Charisma score
- can cast Fortune's Favor on self once per long rest
- **Curse of Greed:** whenever you encounter gold that does not have an obvious owner, make a DC 15 Charisma save or you must attempt to obtain it

### Anthropologist

- after observing humanoids interacting with one another for at least 1 day, I can learn a small amount of important words/expressions/gestures -- enough for simple/basic communication

## Character Traits

personality traits:

- I have Stage 4 British.
- I'm a stickler when it comes to observing proper etiquette and local customs.
- When I arrive at a new settlement for the first time, I must learn all its customs.

ideals:

- Discovery. I want to be the first person to discover a lost culture.
- Protection. I must do everything possible to save a society facing extinction.

bonds:

- I want to learn about krag culture.
- I want to become more renowned than my rival, Victoria Handforth.

flaws: I believe that I'm intellectually superior to people from other cultures, and have much to teach them.

## Appearance

blue eyes, dark brown hair\
tan skin; round eyeglasses\
6ft tall, 140lb body weight

## Utility/Helper Functions

```lua calcmd
-- stringifies and concatenates all the arguments
function fmt(...)
    out=''
    for _, arg in ipairs(table.pack(...)) do
        s = tostring(arg)
        if s == nil then
            s = ''
        end
        out=out..s
    end
    return out
end

-- calculate current total inventory weight based on item weights / quantities
function total_weight()
    local total = 0
    for submatch in string.gmatch(inventory, '([%d.]+)lb') do
        local w = tonumber(submatch)
        if w ~= nil then
            total = total + w
        end
    end
    for submatch in string.gmatch(inventory, '(%d+x%s+[%d.]+lb)') do
        local _, _, quantity, weight = string.find(submatch, '(%d+)x%s+([%d.]+)lb')
        local q, w = tonumber(quantity), tonumber(weight)
        if q == nil then
            q = 1
        end
        if w ~= nil then
            total = total + (q * w)
        end
    end
    return total
end

-- print "RESET" if any of the given reset conditions are true
function reset(...)
    for _, condition in ipairs(table.pack(...)) do
        if condition then
            return "RESET"
        end
    end
    return ""
end
```
