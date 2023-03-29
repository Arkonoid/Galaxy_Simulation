# Imports
import random


# Setup generator functions
def random_generator(min_value, max_value):
    random_number = random.randrange(min_value, max_value + 1)
    return random_number


test_number = random_generator(0, 5)


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
star_list = []
star_class_list = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
for i in range(1000000):
    star_class = random.choices(star_class_list, weights=(0.00003, 0.0013, 0.006, 0.03, 0.076, 0.121, 0.7645))
    star_list.append(star_class[0])

print(f"System's star is a {star_list}")

# Generate 'Planet' class
class Planet:
    def __init__(self, size, shape, number_of_stars):
        self.size = size
        self.shape = shape
        self.number_of_stars = number_of_stars
        pass


#   Generate number of planets based on stars
#   Generate distance of planets
#   Generate size off planets
#   Generate type of planet

# Generate 'Species' class
class Species:
    pass

#   Generate species based on planet type
#   Generate species traits
