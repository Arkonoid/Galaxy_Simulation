# Imports
import random
import plotting
from IPython.display import display
import pandas as pd

# Changes settings in pandas to display the entire dataframe instead of the collapsed version
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Set up the random number generator function
def random_generator(min_value, max_value):
    random_number = random.randrange(min_value, max_value + 1)
    return random_number


# List for the planet codes, so they can be weighted differently depending on distance to star
planet_codes_weighted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def planet_codes(code):
    match code:
        case 0:
            return "Barren"
        case 1:
            return "Temperate"
        case 2:
            return "Forest"
        case 3:
            return "Archipelago"
        case 4:
            return "Ocean"
        case 5:
            return "Craig"
        case 6:
            return "Lava"
        case 7:
            return "Jungle"
        case 8:
            return "Tundra"
        case 9:
            return "Arctic"
        case 10:
            return "Desert"
        case 11:
            return "Toxic"
        case _:
            return "UNDEFINED"


# Other various lists with values that can be used with the weighted choices
morphology_general_list = ["Primate", "Cetacea", "Arthropod"]
morphology_limbs_list = [0, 2, 4, 6, 8, 10, 12]
species_height_list = [3, 2, 1, 0]


# Create 'Galaxy' class
class Galaxy:
    def __init__(self, number_of_stars):
        self.number_of_stars = number_of_stars
        pass


# Generate the number of stars
galaxy_star_count = random_generator(1000000000, 2000000000)

# Generate the galaxy
galaxy1 = Galaxy(galaxy_star_count)


# Create 'Planet' class
class Planet:
    def __init__(self, planet_id, size, primary_biome, distance_from_star, habitable):
        self.planet_id = planet_id
        self.size = size
        self.primary_biome = primary_biome
        self.distance_from_star = distance_from_star
        self.habitable = habitable
        pass


# Generate number of planets based on stars
planet_count = round(galaxy_star_count * 0.000001)

# Create a list for the planets to go into
planet_list = []

# Empty DataFrame for the newly created elements to be added into
df_planet = pd.DataFrame()

# Generate the properties of each planet
for i in range(planet_count):
    temp_id = i
    temp_size = random_generator(1, 10)
    temp_distance_from_star = round((random_generator(30, 200) * 0.01), 2)

    # Generates different kinds of planets based on their distance from the star
    if temp_distance_from_star <= 0.6:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.2, 0, 0, 0, 0, 0.2, 0.5, 0, 0, 0, 0, 0.1))[0])
    elif temp_distance_from_star <= 0.8:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.2, 0, 0, 0, 0, 0.2, 0.1, 0, 0, 0, 0.2, 0.3))[0])
    elif temp_distance_from_star <= 0.9:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.2, 0.1, 0.1, 0, 0, 0.1, 0, 0.1, 0, 0, 0.3, 0.1))[0])
    elif temp_distance_from_star <= 1.0:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0, 0.1, 0, 0, 0.1, 0))[0])
    elif temp_distance_from_star <= 1.1:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.2, 0.1, 0.2, 0.1, 0.1, 0, 0, 0.1, 0.1, 0, 0.1, 0))[0])
    elif temp_distance_from_star <= 1.2:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.3, 0, 0.1, 0.1, 0.1, 0, 0, 0, 0.3, 0.1, 0, 0))[0])
    elif temp_distance_from_star <= 1.2:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.3, 0, 0.1, 0.1, 0.1, 0, 0, 0, 0.3, 0.1, 0, 0))[0])
    elif temp_distance_from_star <= 1.4:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.5, 0, 0, 0, 0, 0.1, 0, 0, 0.1, 0.3, 0, 0))[0])
    elif temp_distance_from_star > 1.4:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0))[0])

    # Decides whether a fringe planet will be able to support life
    habitability_factor = round(random_generator(0, 100) * 0.01, 2)

    # Habitability is set to true by default
    temp_habitable = True

    # Barren planets will always be uninhabitable
    if temp_primary_biome == "Barren":
        temp_habitable = False
    # Extreme climate worlds have a 1/20 chance to be habitable
    elif temp_primary_biome == "Lava" or temp_primary_biome == "Toxic" or temp_primary_biome == "Arctic":
        if habitability_factor < 0.95:
            temp_habitable = False
    # Boarder worlds have a 1/5 chance to be habitable
    elif temp_primary_biome == "Craig" or temp_primary_biome == "Desert":
        if habitability_factor < 0.8:
            temp_habitable = False
    else:
        temp_habitable = True

    # Creates the planet based on the generated properties
    planet = Planet(temp_id, temp_size, temp_primary_biome, temp_distance_from_star, temp_habitable)
    # Add the newly created planet to the list
    planet_list.append(planet)

    # Create the DF with the properties
    my_df_temp = {
        'PLANET ID': [temp_id],
        'PLANET SIZE': [temp_size],
        'PRIMARY BIOME': [temp_primary_biome],
        'DISTANCE FROM STAR': [temp_distance_from_star],
        'HABITABLE': [temp_habitable]
    }

    # Merge the new DF with the existing one to effectively *add it to the list*
    df_temp = pd.DataFrame(my_df_temp)
    df_planet = pd.concat([df_planet, df_temp])


# Create 'Species' class
class Species:
    def __init__(self, species_id, species_planet_id, morphology_general, morphology_limbs, height, weight,
                 sapience_index):
        self.species_id = species_id
        self.species_planet_id = species_planet_id
        self.morphology_general = morphology_general
        self.morphology_limbs = morphology_limbs
        self.height = height
        self.weight = weight
        self.sapience_index = sapience_index


# Create a list for the species to go into
species_list = []
counter = 0

# Empty DataFrame for Species
df_species = pd.DataFrame()

# Cycle through all planets to find ones that are habitable and generate the species for them
for i in range(len(planet_list)):
    if planet_list[i].habitable:
        temp_species_id = counter
        temp_species_planet_id = i

        # This checks the planet's biome to make certain morphologies more common for them
        if planet_list[i].primary_biome == "Temperate":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.45, 0.1, 0.45))[0]
        elif planet_list[i].primary_biome == "Forest":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.5, 0.05, 0.45))[0]
        elif planet_list[i].primary_biome == "Archipelago":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.3, 0.6, 0.1))[0]
        elif planet_list[i].primary_biome == "Ocean":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.0, 1.0, 0.0))[0]
        elif planet_list[i].primary_biome == "Craig":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.2, 0.0, 0.8))[0]
        elif planet_list[i].primary_biome == "Lava":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.0, 0.0, 1.0))[0]
        elif planet_list[i].primary_biome == "Jungle":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.4, 0.4, 0.2))[0]
        elif planet_list[i].primary_biome == "Tundra":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.7, 0.2, 0.1))[0]
        elif planet_list[i].primary_biome == "Arctic":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.1, 0.9, 0.0))[0]
        elif planet_list[i].primary_biome == "Desert":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.1, 0.0, 0.9))[0]
        elif planet_list[i].primary_biome == "Toxic":
            temp_morphology_general = random.choices(morphology_general_list, weights=(0.0, 0.1, 0.9))[0]
        temp_morphology_limbs = random.choices(morphology_limbs_list, weights=(0.02, 0.08, 0.4, 0.3, 0.1, 0.06, 0.04))

        # Checks the morphology to make certain number of limbs more common
        if temp_morphology_general == "Primate":
            temp_morphology_limbs = random.choices(morphology_limbs_list,
                                                   weights=(0.0, 0.1, 0.4, 0.4, 0.1, 0.0, 0.0))[0]
        elif temp_morphology_general == "Cetacea":
            temp_morphology_limbs = random.choices(morphology_limbs_list,
                                                   weights=(0.1, 0.3, 0.3, 0.3, 0.0, 0.0, 0.0))[0]
        elif temp_morphology_general == "Arthropod":
            temp_morphology_limbs = random.choices(morphology_limbs_list,
                                                   weights=(0.0, 0.0, 0.0, 0.2, 0.2, 0.3, 0.3))[0]

        # Checks the planet's size to make smaller planets produce larger species
        if planet_list[i].size <= 3:
            temp_species_height = random.choices(species_height_list, weights=(0.4, 0.3, 0.2, 0.1))[0] + round(
                random_generator(0, 10) * 0.1, 1)
        elif planet_list[i].size <= 7:
            temp_species_height = random.choices(species_height_list, weights=(0.2, 0.3, 0.3, 0.2))[0] + round(
                random_generator(0, 10) * 0.1, 1)
        elif planet_list[i].size <= 10:
            temp_species_height = random.choices(species_height_list, weights=(0.1, 0.1, 0.4, 0.4))[0] + round(
                random_generator(0, 10) * 0.1, 1)

        # Uses a formula to determine weight based on height
        temp_species_weight = round((temp_species_height * temp_species_height) * (random_generator(155, 165) * 0.1), 2)

        # Creates and modifies a certain value used in sapience index calculation.
        # This means certain traits can make a species more or less likely to be intelligent
        intel_multiplier = 1

        if temp_morphology_general == "Primate":
            intel_multiplier += 0.3
        if temp_morphology_general == "Cetacea":
            intel_multiplier += 0.2
        if temp_morphology_general == "Arthropod":
            intel_multiplier -= 0.2

        if temp_species_height < 0.5:
            intel_multiplier = 0.2
        elif temp_species_height <= 1:
            intel_multiplier -= 0.5
        elif temp_species_height <= 2.5:
            intel_multiplier += 0
        elif temp_species_height <= 3:
            intel_multiplier += 0.2
        elif temp_species_height <= 5:
            intel_multiplier -= 0.2

        # Generates the sapience index
        temp_sapience_index = round((random_generator(50, 70) * 0.1) * intel_multiplier)
        if temp_sapience_index > 10:
            temp_sapience_index = 10

        # Creates the new species from the generated traits
        species = Species(temp_species_id,
                          temp_species_planet_id,
                          temp_morphology_general,
                          temp_morphology_limbs,
                          temp_species_height,
                          temp_species_weight,
                          temp_sapience_index)

        # Adds the species to the list (Honestly unused now that the sqlite DB is gone)
        species_list.append(species)
        #Iterates the counter for the next species id
        counter += 1

        # Create the DF with the properties
        my_df_temp = {
            'SPECIES ID': [temp_species_id],
            'PLANET ID': [temp_species_planet_id],
            'MORPHOLOGY': [temp_morphology_general],
            'LIMB COUNT': [temp_morphology_limbs],
            'HEIGHT': [temp_species_height],
            'WEIGHT': [temp_species_weight],
            'SAPIENCE INDEX': [temp_sapience_index]
        }

        # Merge the new DF with the existing one to effectively *add it to the list*
        df_temp = pd.DataFrame(my_df_temp)
        df_species = pd.concat([df_species, df_temp])


# Save DataFrames as a CSV File
planet_csv_data = df_planet.to_csv('planet_data.csv', index=False)
print('\nCSV String: ', planet_csv_data)
species_csv_data = df_species.to_csv('species_data.csv', index=False)
print('\nCSV String: ', species_csv_data)

# Load CSV data into Pandas DataFrame
planet_data = pd.read_csv('planet_data.csv')
species_data = pd.read_csv('species_data.csv')

# Create a New DataFrame that Joins Planets and Species on Planet ID
galaxy_df = pd.merge(planet_data, species_data, on='PLANET ID')
galaxy_csv_data = galaxy_df.to_csv('galaxy_data.csv', index=False)


def display_planets():
    display(planet_data)


def display_species():
    display(species_data)


# DEBUG TEST CODE
# for i in species_list:
#     print("PLANET DETAILS")
#     print("---------------------------")
#     print(f"Planet ID: {planet_list[i.species_planet_id].planet_id}")
#     print(f"Distance from Star: {planet_list[i.species_planet_id].distance_from_star}AU")
#     print(f"Planet Type: {planet_list[i.species_planet_id].primary_biome}")
#     print(f"Planet Size: {planet_list[i.species_planet_id].size}")
#     print("SPECIES DETAILS")
#     print("---------------------------")
#     print(f"Species ID: {i.species_id}")
#     print(f"Species Morphology: {i.morphology_general}")
#     print(f"Limb Count: {i.morphology_limbs}")
#     print(f"Height: {i.height}")
#     print(f"Weight: {i.weight}")
#     print(f"Sapience Index: {i.sapience_index}")
#     print("===========================")

# User Interface


# Main program loop
end_program = False
print("Welcome to the Galaxy Simulator v0.5!")
print("\nA new galaxy has already been generated for you, and been filled with randomly generated "
      "planets and species. Select the options below to see some of the data on this new galaxy!\n")
while not end_program:
    print("============================================")
    print("What would you like to do?")
    print("1) Display Raw DataFrame for Planets")
    print("2) Display Raw DataFrame for Species")
    print("3) View Height and Weight Correlation for species")
    print("4) View Height and Planet Size Correlation for species")
    print("5) View Morphology and Sapience Index Comparison")
    print("Enter anything else to exit\n")

    selection = int(input('Selection: '))
    match selection:
        case 1:
            display_planets()
        case 2:
            display_species()
        case 3:
            plotting.weight_chart_display()
        case 4:
            plotting.size_chart_display()
        case 5:
            plotting.sapience_chart_display()
        case _:
            end_program = True
