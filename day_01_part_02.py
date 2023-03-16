def calculate_fuel_for_module(mass):
    fuel = mass // 3 - 2
    return fuel + calculate_fuel_for_module(fuel) if fuel > 0 else 0
def calculate_total_fuel(modules_mass):
    return sum(calculate_fuel_for_module(mass) for mass in modules_mass)
