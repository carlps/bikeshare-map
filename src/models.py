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
        return tstmp.strftime('%b %d, %Y - %I:%M:%S %p %Z')

    def to_feature(self):
        ''' convert station_information object to a dict
            that is formatted as needed to load as a feature
            in mapbox. Station_id is also included as a property
            because feature ID is not upheld when loaded and then
            read back from mapbox. So having it as a property as
            well should guarantee we are able to reference online
            back to db. Dynamic values are not included since they
            need to be looked up during run.
        '''
        return {
                "id": str(self.station_id),
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(self.lon), float(self.lat)]
                    },
                "properties": {
                    "station_id": self.station_id,
                    "station_name": self.station_name
                    }
                }
