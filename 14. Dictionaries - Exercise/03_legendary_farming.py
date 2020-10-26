def get_key_material(material, quantity):
    key_materials[material] += quantity
    return key_materials


def get_junk_material(material, quantity):
    if material not in junk:
        junk[material] = 0
    junk[material] += quantity
    return junk


def print_result(key_materials, junk):
    sorted_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
    for material, quantity in sorted_key_materials.items():
        print(f"{material}: {quantity}")

    sorted_junk_materials = dict(sorted(junk.items()))
    for material, quantity in sorted_junk_materials.items():
        print(f"{material}: {quantity}")


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
winner_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}
is_item_obtained = False

while True:
    materials = input().lower().split()

    for i in range(1, len(materials), 2):
        material = materials[i]
        quantity = int(materials[i - 1])

        if material in key_materials:
            get_key_material(material, quantity)

            if key_materials[material] >= 250:
                print(f"{winner_items[material]} obtained!")
                key_materials[material] -= 250
                is_item_obtained = True
                break

        else:
            get_junk_material(material, quantity)

    if is_item_obtained:
        print_result(key_materials, junk)
        break

