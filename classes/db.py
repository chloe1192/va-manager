from sqlalchemy import create_engine, text
class DbQuery():
    engine = create_engine("mysql+pymysql://root:MyNewPass@localhost:3336/sql_aircraft?charset=utf8mb4")
    def __init__(self):
        pass

    def create_table(self, table, fields):
        query = ""
        for row in fields:
            query += f"{row}, "
        db_init = f"""
            CREATE TABLE IF NOT EXISTS {table} (
                {query}
            );
        """
        self.connect_to_engine(db_init)

    @staticmethod
    def connect_to_engine( query, want_res=False):
        with DbQuery.engine.connect() as conn:
            res = conn.execute(text(query))
            conn.commit()
            if want_res == True:
                return res.all()

    def select_all_from(self, table):
        query = f"SELECT * FROM {table}"
        return self.connect_to_engine(query, True)
    
    def select_all_from_where_id(self, table, id):
        query = f"SELECT * FROM {table} WHERE id={id}"
        return self.connect_to_engine(query, True)

    def insert_into(self, table, query):
        dict = query.to_dict()
        keys = ""
        values = ""
        for key, value in dict.items():
            keys += str(f"`{key}`, ")
            values += str(f"'{value}', ")
        keys = keys[:-2]
        values = values[:-2]
        query = f"INSERT INTO `{table}` ({keys}) VALUES ({values})"
        self.connect_to_engine(query)
    
    def update_where(self, table, query, id):
        dict = query.to_dict()
        sets = ""
        for key, value in dict.items():
            sets += "`%s` = '%s', " %(key, value)
        sets = sets[:-2]
        query = f"UPDATE `{table}` SET {sets} WHERE id={id}"
        self.connect_to_engine(query)
    
    def delete_where(self, table, id):
        query = f"DELETE FROM `{table}` WHERE id={id}"
        self.connect_to_engine(query)

    def specific_query(self, query, want_res=False):
        if want_res == True:
            return self.connect_to_engine(query, True)
        self.connect_to_engine(query)