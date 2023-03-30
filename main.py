# Imports
import random


# Setup generator functions
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


# Create 'Galaxy' class
class Galaxy:
    def __init__(self, number_of_stars):
        self.number_of_stars = number_of_stars
        pass


# Generate the number of stars
galaxy_star_count = random_generator(75000000000, 125000000000)

# Generate the galaxy
galaxy1 = Galaxy(galaxy_star_count)


# Create 'Planet' class
class Planet:
    def __init__(self, planet_id, size, primary_biome, distance_from_star):
        self.planet_id = planet_id
        self.size = size
        self.primary_biome = primary_biome
        self.distance_from_star = distance_from_star
        pass


# Generate number of planets based on stars
planet_count = round(galaxy_star_count * 0.000001)

# Create a list for the planets to go into
planet_list = []

# Generate the properties of each planet
for i in range(planet_count):
    temp_id = i
    temp_size = random_generator(1, 10)
    temp_distance_from_star = round((random_generator(0, 1) + random_generator(30, 100) * 0.01), 2)

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
            random.choices(planet_codes_weighted_list, weights=(0.4, 0, 0, 0, 0, 0.1, 0, 0, 0.1, 0.4, 0, 0))[0])
    elif temp_distance_from_star > 1.4:
        temp_primary_biome = planet_codes(
            random.choices(planet_codes_weighted_list, weights=(0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0))[0])

    planet = Planet(temp_id, temp_size, temp_primary_biome, temp_distance_from_star)

    # Add the newly created planet to the list
    planet_list.append(planet)

# for i in range(planet_count):
#     print(planet_list[i].planet_id)
#     print(planet_list[i].size)
#     print(planet_list[i].primary_biome)
#     print(planet_list[i].distance_from_star)
#     print("-------------------")

# Create 'Species' class (id, morphology general, morphology limbs, height, weight, sapience index)

# output a csv file for the planets and the species separately

# use pandas sql to read the two csv files

# join the two tables

# print(galaxy1.size)
# print(galaxy1.shape)
# print("{:,}".format(galaxy1.number_of_stars))

# Create 'Star' class
# star_list = []
# star_class_list = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
# for i in range(1000000):
#     star_class = random.choices(star_class_list, weights=(0.00003, 0.0013, 0.006, 0.03, 0.076, 0.121, 0.7645))
#     star_list.append(star_class[0])


# Generate 'Planet' class


planet_number = galaxy_star_count / 1000
print(planet_number)

habitable_planet_count = planet_number * 0.001
print(habitable_planet_count)


#   Generate number of planets based on stars

#   Generate distance of planets
#   Generate size off planets
#   Generate type of planet

# Generate 'Species' class
class Species:
    def __init__(self, id, morphology_general, morphology_limbs, height, weight, sapience_index):
        self.id = id
        self.morphology_general = morphology_general
        self.morphology_limbs = morphology_limbs
        self.height = height
        self.weight = weight
        self.sapience_index = sapience_index

#   Generate species based on planet type
#   Generate species traits
