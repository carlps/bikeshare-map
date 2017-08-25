''' src.models '''

# import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Station_Information(Base):

    __tablename__ = 'latest_station_info'

    station_id = Column(Integer, primary_key=True)
    station_name = Column(String(length=100), nullable=False)
    lon = Column(Numeric)
    lat = Column(Numeric)
    num_bikes_available = Column(Integer)
    num_docks_available = Column(Integer)
    last_updated = Column(DateTime)

    def dt_format(self, tstmp):
        return tstmp.strftime('%b %d, %Y - %I:%M:%S %p')

    def to_feature(self):
        ''' convert station_information object to a dict
            that is formatted as needed to load as a feature
            in mapbox
        '''
        return {
                "id": str(self.station_id),
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(self.lon), float(self.lat)]
                    },
                "properties": {
                    "station_name": self.station_name,
                    "num_bikes_available": self.num_bikes_available,
                    "num_docks_available": self.num_docks_available,
                    "last_updated": self.dt_format(self.last_updated)
                    }
                }
