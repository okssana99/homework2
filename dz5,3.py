# Adult upper clothing sizes
adult_upper_sizes = {
    "Russia": {"XS": (90, 42), "S": (95, 44), "M": (99, 46), "L": (104, 48), "XL": (109, 50), "XXL": (114, 52), "XXXL": (119, 54)},
    "Europe": {"XS": (66, 89), "S": (70, 92), "M": (74, 95), "L": (78, 98), "XL": (82, 101), "XXL": (87, 104)},
    "UK": {"XS": (36, 81), "S": (40, 84), "M": (44, 87), "L": (48, 90), "XL": (52, 93)},
    "USA": {"XS": (6, 36), "S": (8, 38), "M": (10, 40), "L": (12, 42), "XL": (14, 44), "XXL": (16, 46), "XXXL": (18, 48), "XXXXL": (20, 50)},
}

# Women's underwear sizes
women_underwear_sizes = {
    "Russia": {"XXS": 42, "XS": 44, "S": 46, "M": 48, "L": 50},
    "Europe": {"XXS": 36, "XS": 38, "S": 40, "M": 42, "L": 44, "XL": 46, "XXL": 48},
    "USA": {"XXS": 0, "XS": 2, "S": 4, "M": 6, "L": 8, "XL": 10, "XXL": 12, "XXXL": 14},
}

# Children's clothing sizes
children_sizes = {
    "86": 3,
    "92": 6,
    "98": 9,
    "104": 12,
    "110": 14,
    "116": 16,
    "122": 18,
    "128": 20,
}

def translate_size(size, system):
    """
    Translates clothing size from one system to another.

    :param size: Size in the original system.
    :param system: Target size system.
    :return: Size in the target system or None if size is not found.
    """
    if size in women_underwear_sizes:
        size_in_different_systems = women_underwear_sizes[size]
        if system in size_in_different_systems:
            return size_in_different_systems[system]
    return None

size = "S"
target_system = "EU"
translated_size = translate_size(size, target_system)
if translated_size is not None:
    print(f"Size {size} in {target_system} system is {translated_size}")
else:
    print("Size not found.")
