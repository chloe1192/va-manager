from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:MyNewPass@localhost:3336/sql_aircraft?charset=utf8mb4")

# with engine.connect() as conn:
    # result = conn.execute(text("SELECT * FROM aircraft_type "))
    # result_all = result.all()
    # for row in result_all:
        # row_as_dict = row._mapping

# airframe db operators
def fetch_all_airframes():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM airframes a RIGHT JOIN aircraft_type at on a.id_aircraft_type = at.id"))
        result_all = result.all()
        return result_all

def fetch_single_airframe(aiframe_id):
    with engine.connect() as conn:
        query = f"SELECT * FROM sql_aircraft.airframes,sql_aircraft.aircraft_type WHERE airframes.id_aircraft_type = aircraft_type.id AND airframe.id={aiframe_id}"
        result = conn.execute(text(query))
        return result.all()

def create_airframe(request):
    with engine.connect() as conn:
        dict = request.to_dict()
        keys = ""
        values = ""
        for key, value in dict.items():
            keys += str(f"`{key}`, ")
            values += str(f"'{value}', ")
        keys = keys[:-2]
        values = values[:-2]
        query = f"INSERT INTO `airframes` ({keys}) VALUES ({values});"
        conn.execute(text(query))
        conn.commit()

def edit_airframe(request, id):
    with engine.connect() as conn:
        dict = request.to_dict()
        sets = ""
        for key, value in dict.items():
            sets += "`%s` = '%s', " %(key, value)
        sets = sets[:-2]
        query = f"UPDATE `airframes` SET {sets} WHERE id={id}"
        conn.execute(text(query))
        conn.commit()

def delete_airframe(id):
    with engine.connect() as conn:
        query = f"DELETE FROM `airframes` WHERE id={id}"
        conn.execute(text(query))
        conn.commit()


# type db operators
def fetch_all_aircraft_types():
    with engine.connect() as conn:
        query = "SELECT * FROM aircraft_type"
        result = conn.execute(text(query))
        return result.all()

# routes db operators
def fetch_all_routes():
    pass

def create_route():
    pass

def edit_route():
    pass

def delete_route():
    pass

# generic db functions
# list all
def select_all_from(table):
    with engine.connect() as conn:
        query = f"SELECT * FROM {table}"
        result = conn.execute(text(query))
        return result.all()
    
# list single
def select_all_from_where_id(table, id):
    with engine.connect() as conn:
        query = f"SELECT * FROM {table} WHERE id={id}"
        result = conn.execute(text(query))
        return result.all()

# create
def insert_into(table, request):
    with engine.connect() as conn:
        dict = request.to_dict()
        keys = ""
        values = ""
        for key, value in dict.items():
            keys += str(f"`{key}`, ")
            values += str(f"'{value}', ")
        keys = keys[:-2]
        values = values[:-2]
        query = f"INSERT INTO `{table}` ({keys}) VALUES ({values});"
        conn.execute(text(query))
        conn.commit()

# edit
def update_where(table, request, id):
    with engine.connect() as conn:
        dict = request.to_dict()
        sets = ""
        for key, value in dict.items():
            sets += "`%s` = '%s', " %(key, value)
        sets = sets[:-2]
        query = f"UPDATE `{table}` SET {sets} WHERE id={id}"
        conn.execute(text(query))
        conn.commit()

# delete
def delete_where(table, id):
    with engine.connect() as conn:
        query = f"DELETE FROM `{table}` WHERE id={id}"
        conn.execute(text(query))
        conn.commit()
