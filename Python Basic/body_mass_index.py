def body_mass_index(weight, height):
    weight_kg = round(weight / 2.2046, 2)
    return float(weight_kg / (((height[0] * 0.3048) + (height[1] * 0.0254)) ** 2))

print(body_mass_index(176.37, [5, 8]))