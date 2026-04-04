names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    grid = ""
    for i, (name, country) in enumerate(zip(names, countries), start=1):
        grid += f"{i}. {name:<11}{country}\n"
    print(grid, end="")
    return grid

enumerate_names_countries()

# find the longest name in the array, plu