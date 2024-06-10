from .airports import Airports
from .db import DbQuery
from sqlalchemy.ext.declarative import declarative_base

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
        return dict
    
    @staticmethod
    def get_airports_for_route():
        res = Airports().get_airports_icao()
        return res
    
    def update_route(self, form, id):
        print(form)
        query = f"""
            UPDATE routes
            SET
                flight_number = "{form['flight_number']}",
                callsign = "{form['callsign']}",
                off_block_time = "{form['off_block_time']}",
                takeoff_time = "{form['takeoff_time']}",
                landing_time = "{form['landing_time']}",
                on_block_time = "{form['on_block_time']}",
                cost_index = "{form['cost_index']}",
                altitude = "{form['altitude']}",
                route_fixes = "{form['route_fixes']}"
            WHERE id_route = {id}
        """
        self.connect_to_engine(query)
        return self.get_all_routes()

