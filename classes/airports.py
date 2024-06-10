from .db import DbQuery


class Airports(DbQuery):

    def get_airports_icao(self):
        query = """
            SELECT id_airport, icao_code FROM airports
        """
        return self.connect_to_engine(query)