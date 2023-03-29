# Imports
import random


# Setup generator functions
def random_generator(min_value, max_value):
    random_number = random.randrange(min_value, max_value + 1)
    return random_number


#Create 'Galaxy' class (shape, number of stars)
# generate number of stars (75,000,000,000 - 125,000,000,000)

#Create 'Planet' class (size, distance to star, primary biome)
# generate number of planets based on stars

# Create 'Species' class (id, morphology general, morphology limbs, height, weight, sapience index)

# output a csv file for the planets and the species separately

# use pandas sql to read the two csv files

# join the two tables

# Create 'Galaxy' class
class Galaxy:
    def __init__(self, size, shape, number_of_stars):
        self.size = size
        self.shape = shape
        self.number_of_stars = number_of_stars
        pass


# Setup lists for the galaxy properties
galaxy_size_options = ["Small", "Medium", "Large"]
galaxy_shape_options = ["Spiral", "Toroid", "Ring", "Spoked"]
galaxy_stars_options = [[1000000, 1000000000], [1000000000, 1000000000000], [1000000000000, 100000000000000]]

# Generate galaxy size
galaxy_size = random_generator(0, 2)

# Generate galaxy shape
galaxy_shape = random_generator(0, 3)

# Generate galaxy star count (based on size)
galaxy_star_count = random_generator(galaxy_stars_options[galaxy_size][0], galaxy_stars_options[galaxy_size][1])

# Create a new 'Galaxy' Object using the generated properties
galaxy1 = Galaxy(galaxy_size_options[galaxy_size], galaxy_shape_options[galaxy_shape], galaxy_star_count)

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
class Planet:
    def __init__(self, size, primary_biome, distance_from_star):
        self.size = size
        self.primary_biome = primary_biome
        self.distance_from_star = distance_from_star
        pass

planet_number = galaxy_star_count/1000
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
