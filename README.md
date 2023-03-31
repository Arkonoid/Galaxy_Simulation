# Galaxy_Simulation
A galaxy simulation program that generates synthetic data based on a fake galaxy.

So it's finally here...

Not the greatest work I've done, and it definitally doesn't live up to its maximum potential, even with all the properties I've given it so far.
It is, however, easily able to be expanded upon, and that's definitely something I'm going to do later on.
Honestly, it's much more exciting reading through the comments in there and learning how it generates data!

### The Project Requirements
### --------------------------

1: Generates a whole bunch of synthetic data, then converts it all to CSV files, which are then read back in to be manipulated by the other half of the program.

2: Merges two DataFrames to create one that it can perform certain operations on. Additionally, the method in which it adds new elements to the DataFrames requires
a concatenation each time.

3: Uses three seaborn visualizations with the data.

4: An *attempt* at creating a Data Dictionary for the project. (The link in the Google Classroom for the project requirements that had the example was taken down,
so I just had to do some reasearch and do what I think it's supposed to look like)

5: Lots of helpful comments throughout the program!

### The Data Dictionary
| Field Name | Data Type | Constraint | Description |
| ---------- | --------- | ---------- | ----------- |
| Galaxy | Class | Must have number_of_stars | Class that is used to generate stars at start-up. Currently only has one property.
| number_of_stars | integer | Between 1,000,000,000 and 2,000,000,000 | Property of the Galaxy Class. Generated once at start-up. Used to determine the number of stars in the galaxy |
| Planet | Class | Must have planet_id, size, primary_biome, distance_from_star, and habitable | Class used to generate the various planets in the galaxy. |
| planet_id | integer | Must not be negative, must be unique | Property that uniquely identifies a planet. Also used to join two dataframes. |
| size | integer | Must be between 1 and 10 | Property that determines a planet's size reletive to others. Randomly generated at start-up. |
| primary_biome | string | Must be one of the 12 biomes, or Undefined | Property that determines the planet's primary biome type. Determined by distance from the star. |
| distance_from_star | float | Must be between 0.30 and 2.00 | Property that determines in AU, the planet's distance from the local star. Randomly generated at start-up |
| habitable | boolean | Must be True or False | Property that determines if a planet is habitable and will therefore generate a species. Determined by the primary biome and a seperate variable called habitability_factor for fringe planets. |
| Species | Class | Must have species_id, species_planet_id, morphology_general, morphology_limbs, height, weight, and sapience_index | Class used to generate various species objects on habitable planets. |
| species_id | integer | Must not be negative, must be unique | Property that uniquely identifies a species. |
| species_planet_id | integer | Must not be negative, must be unique, must line up with planet_id | Property that determines the id of the planet the species was generated for. Lines up with planet_id for a table join. |
| morpology_general | string | Must be one of the 3 possible choices for morphology | Property that defines a species general appearence. Is influenced by planet_biome
| morphology_limbs | integer | Must be 0, 2, 4, 6, 8, 10, or 12 | Property that defines the number of limbs a species has. Is influenced by morphology_general |
| height | float | Must be between 0.0 and 5.0 | Measures a species' height in meters. Influenced by planet size. |
| weight | float | Must be positive | Measures a species' weight in kg. Influenced by height. |
| sapience_index | float | Must be between 0.0 and 10.0 | Determines a species general intellegence. Influenced by morphology_general and height. |
