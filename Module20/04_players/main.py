players = {

    ("Ivan", "Volkin"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}
other_variant = []
for key, value in players.items():
    other_variant.append(key + value)
print(other_variant)
