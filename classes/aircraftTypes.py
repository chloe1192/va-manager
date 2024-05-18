from db import DbQuery


class AircraftTypes():
    def __init__(self, name, icao, dew, mzfw, oew, mtow, mlw, max_fuel, min_runway):
        self.name = name
        self.icao = icao
        self.dew = dew
        self.mzfw = mzfw
        self.oew = oew
        self.mtow = mtow
        self.mlw = mlw
        self.max_fuel = max_fuel
        self.min_runway = min_runway