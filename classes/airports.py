from db import DbQuery


class Airports():

    def __init__(self, icao, iata, name, country, is_hub):
        self.icao = icao
        self.iata = iata
        self.name = name
        self.country = country
        self.is_hub = is_hub

    def change_name(self, id, new_name):
        query = f"UPDATE aiports SET name = {new_name} WHERE id = {id}"
        DbQuery().connect_to_engine(query)