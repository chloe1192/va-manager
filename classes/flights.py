from db import DbQuery


class Flights():
    def __init__(self, departure_airport, destination_airport, flt_number, off_block_time, takeoff_time, callsign):
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.flt_number = flt_number
        self.off_block_time = off_block_time
        self.takeoff_time = takeoff_time
        self.callsign = callsign

    def list_flight(self):
        flight = {
            "departure_airport": self.departure_airport,
            "destination_airport": self.destination_airport,
            "flt_number": self.flt_number,
            "off_block_time": self.off_block_time,
            "takeoff_time": self.takeoff_time,
            "callsign": self.callsign
        }
        return flight