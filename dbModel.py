from Entity import *


class MapAutos(db.Model):
    __tablename__ = 'MapAutos'

    def __init__(self
                 , Name
                 , Picture
                 , Color
                 , Longitude
                 , Latitude
                 ):
        self.Name = Name
        self.Picture = Picture
        self.Color = Color
        self.Longitude = Longitude
        self.Latitude = Latitude
