import sqlite3

import main

conn = sqlite3.connect('galaxy.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS planet")
c.execute("DROP TABLE IF EXISTS species")

c.execute("""CREATE TABLE planet (
            planet_id integer,
            planet_size integer,
            primary_biome text,
            distance_from_star real,
            habitable integer
            )""")

c.execute("""CREATE TABLE species (
            id integer,
            planet_id integer,
            morphology text,
            limb_count integer,
            height real,
            weight real,
            sapience_index int
            )""")

insert_with_param_planet = """INSERT INTO planet
            (planet_id, planet_size, primary_biome, distance_from_star, habitable)
            VALUES (?, ?, ?, ?, ?);"""

insert_with_param_species = """INSERT INTO species
            (id, planet_id, morphology, limb_count, height, weight, sapience_index)
            VALUES (?, ?, ?, ?, ?, ?, ?);"""

for i in main.planet_list:
    data_tuple = (i.planet_id, i.size, i.primary_biome, i.distance_from_star, i.habitable)
    c.execute(insert_with_param_planet, data_tuple)

for i in main.species_list:
    data_tuple = (
        i.species_id, i.species_planet_id, i.morphology_general, i.morphology_limbs, i.height, i.weight,
        i.sapience_index)
    c.execute(insert_with_param_species, data_tuple)

c.execute(
    """SELECT species.id,species.morphology,species.limb_count,species.height,species.weight,species.sapience_index
        FROM species
        INNER JOIN planet
        ON species.planet_id = planet.planet_id""")

print(c.fetchall())

conn.commit()

conn.close()
