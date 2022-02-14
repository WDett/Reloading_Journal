import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()


def initialize_sqlite():

    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table'")
    result = cur.fetchone()
    if result[0] == 1:
        con.commit()

    else:
        cur.execute('''CREATE TABLE loads 
            (
            "LOAD_ID"	TEXT NOT NULL UNIQUE,
            "LOAD_NAME"	TEXT,
            "CARTRIDGE"	TEXT,
            "CARTRIDGE_OAL"	TEXT,
            "VELOCITY"	TEXT,
            "BRASS_BRAND"	TEXT,
            "BRASS_FIRINGS"	TEXT,
            "BRASS_LENGTH"	TEXT,
            "BRASS_TUMBLED"	TEXT,
            "BRASS_ANNEALED"	TEXT,
            "BRASS_TRIMMED"	TEXT,
            "BRASS_CHAMFER"	TEXT,
            "BRASS_DE_BUR"	TEXT,
            "CARTRIDGE_CRIMP_STYLE"	TEXT,
            "CARTRIDGE_CRIMP_MEASUREMENT"	TEXT,
            "PRIMER_BRAND"	TEXT,
            "PRIMER_MODEL"	TEXT,
            "POWDER_BRAND"	TEXT,
            "POWDER_MODEL"	TEXT,
            "POWDER_GRAINS"	TEXT,
            "PROJECTILE_BRAND"	TEXT,
            "PROJECTILE_MODEL"	TEXT,
            "PROJECTILE_GRAINS"	TEXT,
            "NOTES"	TEXT,
            PRIMARY KEY("LOAD_ID")
        )''')
        con.commit()


def get_load_by_id(load_id):
    con.cursor()
    cur.execute(f'SELECT * FROM loads WHERE LOAD_ID = "{load_id}"')
    result = cur.fetchone()
    load_data = []
    for item in result:
        load_data = load_data + [item]
    return load_data


def get_unique_cartridges():
    con.cursor()
    cur.execute("SELECT DISTINCT CARTRIDGE FROM loads")
    result = cur.fetchall()
    list_cartridges = []
    for item in result:
        list_cartridges = list_cartridges + [f"{item[0]}"]
    return list_cartridges


def get_recipes_by_cartridges(selected_cartridge):
    con.cursor()
    cur.execute(f"SELECT * FROM loads WHERE CARTRIDGE = '{selected_cartridge}'")
    result = cur.fetchall()
    list_loads = []
    print(result)
    for item in result:
        list_loads = list_loads + [f"{item[1]}"]
    return list_loads, result


def save_load(load_list):
    con.cursor()
    cur.execute(f'INSERT OR REPLACE INTO loads ("LOAD_ID", "LOAD_NAME", "CARTRIDGE", "CARTRIDGE_OAL", "VELOCITY", '
                f'"BRASS_BRAND", "BRASS_FIRINGS", "BRASS_LENGTH", "BRASS_TUMBLED", "BRASS_ANNEALED", "BRASS_TRIMMED", '
                f'"BRASS_CHAMFER", "BRASS_DE_BUR", "CARTRIDGE_CRIMP_STYLE", "CARTRIDGE_CRIMP_MEASUREMENT", '
                f'"PRIMER_BRAND", "PRIMER_MODEL", "POWDER_BRAND", "POWDER_MODEL", "POWDER_GRAINS", "PROJECTILE_BRAND", '
                f'"PROJECTILE_MODEL", "PROJECTILE_GRAINS", "NOTES") VALUES ("{load_list[0]}", "{load_list[1]}", '
                f'"{load_list[2]}", "{load_list[3]}", "{load_list[4]}", "{load_list[5]}", "{load_list[6]}", '
                f'"{load_list[7]}", "{load_list[8]}", "{load_list[9]}", "{load_list[10]}", "{load_list[11]}", '
                f'"{load_list[12]}", "{load_list[13]}", "{load_list[14]}", "{load_list[15]}", "{load_list[16]}", '
                f'"{load_list[17]}", "{load_list[18]}", "{load_list[19]}", "{load_list[20]}", "{load_list[21]}", '
                f'"{load_list[22]}", "{load_list[23]}");')
    con.commit()


def del_load(load_id):
    con.cursor()
    cur.execute(f'DELETE FROM loads WHERE LOAD_ID = {load_id};')
    con.commit()


def close_and_save():
    cur.close()
    con.close()
