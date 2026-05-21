from itertools import product

def unique_combinations(*sequences):
    for combo in product(*sequences):
        yield combo

colors = ["red", "blue"]
sizes = ["S", "M"]
materials = ["cotton", "polyester"]

for combo in unique_combinations(colors, sizes, materials):
    print(combo)