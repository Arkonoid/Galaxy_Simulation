import sqlite3
import main

conn = sqlite3.connect('galaxy.db')

c = conn.cursor()

# Gets rid of the species table if it already exists so the program works past the first run
c.execute("""DROP TABLE IF EXISTS species""")

c.execute("""CREATE TABLE species (
            id integer,
            planet_id integer,
            morphology text,
            limb_count integer,
            height real,
            weight real,
            sapience_index int
            )""")

insert_with_param = """INSERT INTO species
            (id, planet_id, morphology, limb_count, height, weight, sapience_index)
            VALUES (?, ?, ?, ?, ?, ?, ?);"""

for i in main.species_list:
    data_tuple = (i.species_id, i.species_planet_id, i.morphology_general, i.morphology_limbs, i.height, i.weight, i.sapience_index)
    c.execute(insert_with_param, data_tuple)

c.execute("SELECT * FROM species")
print(c.fetchall())

conn.commit()

conn.close()