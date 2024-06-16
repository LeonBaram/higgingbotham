from oauth2client.service_account import ServiceAccountCredentials
import gspread
import toml
import re
from collections import defaultdict
from itertools import chain


def parse_fraction(fraction):
    if m := re.fullmatch("(.+) ?/ ?(.+)", fraction):
        return m.group(1, 2)
    else:
        return None


filename = "higgingbotham.toml"

data = None

with open(filename) as file:
    data = toml.loads(file.read())

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "crucial-bonito-382823-5333eb85d775.json", scopes)  # type: ignore

file = gspread.authorize(credentials)
sheet = file.open("Higgingbotham").sheet1

cells = defaultdict(list)

cells["f13"].append(data["character name"])
cells["i157"].append(data["character title"])
cells["f15"].append(data["player name"])

cells["al15"].append(data["level"])
cells["u15"].append(data["race"])
cells["u13"].append(data["class"])
cells["aa13"].append(data["background"])
cells["aa15"].append(data["alignment"])
cells["h18"].append(data["inspiration"])
cells["v28"].append(data["conditions"])
cells["h22"].append(data["proficiency bonus"])

cells["w20"].append(data["initiative"])
cells["s20"].append(data["armor class"])
cells["c54"].append(data["passive perception"])
sheet.insert_note("c54",
                  f"passive investigation: {data['passive investigation']}")

# Carry Capacity
cells["f91"].append(data["carry capacity"])

# Observant Feat
cells["o55"].append("observant" in data["features"])

# Death Saves
death_save_successes = data["death saves"]["successes"]
cells["z33:ab33"].extend((death_save_successes >= 1,
                          death_save_successes >= 2,
                          death_save_successes >= 3))

death_save_failures = data["death saves"]["failures"]
cells["z34:ab34"].extend((death_save_failures >= 1,
                          death_save_failures >= 2,
                          death_save_failures >= 3))

# Hit Points
current_hp, max_hp = parse_fraction(data["hit points"]["hp"])
cells["s25"].append(current_hp)
cells["v24"].append(max_hp)

# Temporary Hit Points
cells["s29"].append(data["hit points"]["temp hp"])

# Hit Dice
current_hit_dice, max_hit_dice = parse_fraction(data["hit points"]["hit dice"])
cells["s34"].append(current_hit_dice)
cells["t33"].append(max_hit_dice)

# Attacks
for entry in data["attacks"]:
    cells["s40:s44"].append(entry["item"])
    cells["z40:z44"].append(entry["stats"]["attack"])
    cells["ac40:ac44"].append(entry["stats"]["damage"])

# Stats
# Ability Scores, Modifiers, Saves
cells["c23"].append(data["stats"]["strength"]["score"])
cells["c21"].append(data["stats"]["strength"]["modifier"])
cells["j25"].append(data["stats"]["strength"]["save"])
cells["i25"].append("proficient" in data["stats"]["strength"])

cells["c28"].append(data["stats"]["dexterity"]["score"])
cells["c26"].append(data["stats"]["dexterity"]["modifier"])
cells["j26"].append(data["stats"]["dexterity"]["save"])
cells["i26"].append("proficient" in data["stats"]["dexterity"])

cells["c33"].append(data["stats"]["constitution"]["score"])
cells["c31"].append(data["stats"]["constitution"]["modifier"])
cells["j27"].append(data["stats"]["constitution"]["save"])
cells["i27"].append("proficient" in data["stats"]["constitution"])

cells["c38"].append(data["stats"]["intelligence"]["score"])
cells["c36"].append(data["stats"]["intelligence"]["modifier"])
cells["j28"].append(data["stats"]["intelligence"]["save"])
cells["i28"].append("proficient" in data["stats"]["intelligence"])

cells["c43"].append(data["stats"]["wisdom"]["score"])
cells["c41"].append(data["stats"]["wisdom"]["modifier"])
cells["j29"].append(data["stats"]["wisdom"]["save"])
cells["i29"].append("proficient" in data["stats"]["wisdom"])

cells["c48"].append(data["stats"]["charisma"]["score"])
cells["c46"].append(data["stats"]["charisma"]["modifier"])
cells["j30"].append(data["stats"]["charisma"]["save"])
cells["i30"].append("proficient" in data["stats"]["charisma"])

# Skills
for skill in data["skills"].values():
    cells["j34:j51"].append(skill[0])
    cells["i34:i51"].append("proficient" in skill)
    cells["h34:h51"].append("expertise" in skill)

# Language & Tool Proficiencies
cells["r54:r65"].extend(data["proficiencies"]["languages"])
cells["r54:r65"].extend(data["proficiencies"]["tools"])

# Weapon & Armor Proficiencies
cells["ai39:ai51"].extend(data["proficiencies"]["weapons"])
cells["ai39:ai51"].extend(data["proficiencies"]["armor"])

# Spellcasting
spell = data["spell"]
cells["ai100"].append(spell["stats"]["attack"])
cells["ab100"].append(spell["stats"]["save"])
cells["i99"].append(spell["stats"]["class"])
cells["i101"].append(spell["stats"]["spells_known"])

# Spell Slots
if "lvl1" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl1"])
    cells["ag104:aj104"].extend((current, _max))

if "lvl2" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl2"])
    cells["g114:j114"].extend((_max, current))

if "lvl3" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl3"])
    cells["ag114:aj114"].extend((current, _max))

if "lvl4" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl4"])
    cells["g124:j124"].extend((_max, current))

if "lvl5" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl5"])
    cells["ag124:aj124"].extend((current, _max))

if "lvl6" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl6"])
    cells["g134:j134"].extend((_max, current))

if "lvl7" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl7"])
    cells["ag134:aj134"].extend((current, _max))

if "lvl8" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl8"])
    cells["g144:j144"].extend((_max, current))

if "lvl9" in spell["slots"]:
    current, _max = parse_fraction(spell["slots"]["lvl9"])
    cells["ag144:aj144"].extend((current, _max))

# Spell List
if "lvl0" in spell["list"]:
    cells["e106:e111"].extend(spell["list"]["lvl0"][:6])
    cells["n103:n111"].extend(spell["list"]["lvl0"][6:])

if "lvl1" in spell["list"]:
    cells["x103:x111"].extend(spell["list"]["lvl1"][:9])
    cells["ag106:ag111"].extend(spell["list"]["lvl1"][9:])

if "lvl2" in spell["list"]:
    cells["e116:e121"].extend(spell["list"]["lvl2"][:6])
    cells["n113:n121"].extend(spell["list"]["lvl2"][6:])

if "lvl3" in spell["list"]:
    cells["x113:x121"].extend(spell["list"]["lvl3"][:9])
    cells["ag116:ag121"].extend(spell["list"]["lvl3"][9:])

if "lvl4" in spell["list"]:
    cells["e126:e131"].extend(spell["list"]["lvl4"][:6])
    cells["n123:n131"].extend(spell["list"]["lvl4"][6:])

if "lvl5" in spell["list"]:
    cells["x123:x131"].extend(spell["list"]["lvl5"][:9])
    cells["ag126:ag131"].extend(spell["list"]["lvl5"][9:])

if "lvl6" in spell["list"]:
    cells["e136:e141"].extend(spell["list"]["lvl6"][:6])
    cells["n133:n141"].extend(spell["list"]["lvl6"][6:])

if "lvl7" in spell["list"]:
    cells["x133:x141"].extend(spell["list"]["lvl7"][:9])
    cells["ag136:ag141"].extend(spell["list"]["lvl7"][9:])

if "lvl8" in spell["list"]:
    cells["e146:e151"].extend(spell["list"]["lvl8"][:6])
    cells["n143:n151"].extend(spell["list"]["lvl8"][6:])

if "lvl9" in spell["list"]:
    cells["x143:x151"].extend(spell["list"]["lvl9"][:9])
    cells["ag146:ag151"].extend(spell["list"]["lvl9"][9:])

# Money
cells["e70"].append(data["money"]["copper"])
cells["e73"].append(data["money"]["silver"])
cells["e76"].append(data["money"]["gold"])
cells["e79"].append(data["money"]["platinum"])
cells["e82"].append(data["money"]["electrum"])

# Inventory
worn_items = data["inventory"]["wearing"].items()
backpack_items = data["inventory"]["backpack"].items()

remaining_equipment = []

total_weight = 0

for index, (name, properties) in enumerate(chain(worn_items, backpack_items)):
    quantity = properties["q"]
    weight = properties["w"]
    total_weight += int(weight)
    if index < 24:
        cells["l71:l94"].append(name)
        cells["k71:k94"].append(quantity)
        cells["v71:v94"].append(weight)
    elif index < 48:
        cells["ab71:ab94"].append(name)
        cells["aa71:aa94"].append(quantity)
        cells["am71:am94"].append(weight)
    else:
        remaining_equipment.append(f"{quantity} {name} ({weight} lbs)")

if remaining_equipment:
    sheet.insert_note("k95", "\n".join(remaining_equipment))

cells["e92"].append(f"{total_weight}lbs")

# Features
features = list(data["features"].keys())
cells["z54:z65"].extend(features[:12])
cells["ah54:ah65"].extend(features[12:24])
if len(features) > 24:
    sheet.insert_note("z66", "\n".join(features[24:]))

# Appearance
appearance = data["appearance"]
cells["u156"].append(appearance["age"])
cells["z156"].append(appearance["height"])
cells["af156"].append(appearance["weight"])
cells["ak156"].append(appearance["height"])
cells["u158"].append(appearance["gender"])
cells["z158"].append(appearance["eyes"])
cells["af158"].append(appearance["hair"])
cells["ak158"].append(appearance["skin"])

# Traits
personality_traits = data["traits"]["personality traits"]
cells["af20:af22"].extend(personality_traits[:3])
if len(personality_traits) > 3:
    sheet.insert_note("ae23", "\n".join(personality_traits[3:]))

ideals = data["traits"]["ideals"]
cells["af24:af26"].extend(ideals[:3])
if len(ideals) > 3:
    sheet.insert_note("ae27", "\n".join(ideals[3:]))

bonds = data["traits"]["bonds"]
cells["af28:af30"].extend(bonds[:3])
if len(bonds) > 3:
    sheet.insert_note("ae31", "\n".join(bonds[3:]))

flaws = data["traits"]["flaws"]
cells["af32:af34"].extend(flaws[:3])
if len(flaws) > 3:
    sheet.insert_note("ae35", "\n".join(flaws[3:]))

sheet.batch_update([{"range": key, "values": [vals]}
                   for key, vals in cells.items()])
