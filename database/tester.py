import sqlite3

data = [('GUA', 'MIA', 'Guatemala City')]

con = sqlite3.connect("./database/flying_chip.db")
cur = con.cursor()

cur.executemany("""
INSERT INTO cheapest_flights (origin_code, destination_code, city_from) VALUES
            (?,?,?)""", data)

con.commit()



