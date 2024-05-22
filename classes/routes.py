from airports import Airports
from classes.db import DbQuery
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

Base = declarative_base()

class Routes(DbQuery):
    
    def get_all_routes(self):
        query = f"""
            SELECT id_route, flight_number, callsign, departure.icao_code as departure_icao, arrival.icao_code as arrival_icao FROM routes 
            JOIN operators ON operators.id_operator = routes.id_operator
            JOIN airports AS departure ON departure.id_airport = routes.departure_airport
            JOIN airports AS arrival ON arrival.id_airport = routes.arrival_airport
        """
        res = self.connect_to_engine(query, True)
        dict = []
        for row in res:
            row_as_dict = row._mapping
            dict.append(row_as_dict)
        return dict
    
    def get_single_route(self, id_route):
        query = f"""
            SELECT 
                *,
                departure.icao_code as departure_icao,
                arrival.icao_code as arrival_icao
            FROM routes 
            JOIN operators ON operators.id_operator = routes.id_operator
            JOIN airports AS departure ON departure.id_airport = routes.departure_airport
            JOIN airports AS arrival ON arrival.id_airport = routes.arrival_airport
            WHERE id_route = {id_route}
        """
        res = self.connect_to_engine(query, True)
        dict = []
        for row in res:
            row_as_dict = row._mapping
            dict.append(row_as_dict)
        return res
    
    @staticmethod
    def get_airports_for_route():
        res = Airports().get_airports_icao()
        return res

