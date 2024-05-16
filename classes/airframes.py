from db import DbQuery


class Airframes():
    def __init__(self, id_type, engine, reg, name, fleet, selcal, modeS, units, etops_cert):
        self.id_type = id_type
        self.engine = engine
        self.reg = reg
        self.name = name
        self.fleet = fleet
        self.selcal = selcal
        self.modeS = modeS
        self.units = units
        self.etops_cert = etops_cert