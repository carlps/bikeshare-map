''' src.models '''

# import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Station_Information(Base):

    __tablename__ = 'station_information'

    station_id = Column(Integer,
                        primary_key=True,
                        unique=True,
                        autoincrement=False)
    short_name = Column(String(length=10))
    station_name = Column(String(length=100), nullable=False)
    lat = Column(Numeric)
    lon = Column(Numeric)
    capacity = Column(Integer)
    region_id = Column(Integer)
    eightd_has_key_dispenser = Column(Boolean)
    rental_method_key = Column(Boolean)
    rental_method_creditcard = Column(Boolean)
    rental_method_paypass = Column(Boolean)
    rental_method_applepay = Column(Boolean)
    rental_method_androidpay = Column(Boolean)
    rental_method_transitcard = Column(Boolean)
    rental_method_accountnumber = Column(Boolean)
    rental_method_phone = Column(Boolean)
    row_modified_tstmp = Column(DateTime)
    load_id = Column(Integer)
    transtype = Column(String(length=1))
    modified_by = Column(String(length=50))

    def get_rental_methods(self):
        rental_methods = []
        if self.rental_method_key:
            rental_methods.append('KEY')
        if self.rental_method_creditcard:
            rental_methods.append('CREDITCARD')
        if self.rental_method_paypass:
            rental_methods.append('PAYPASS')
        if self.rental_method_applepay:
            rental_methods.append('APPLEPAY')
        if self.rental_method_androidpay:
            rental_methods.append('ANDROIDPAY')
        if self.rental_method_transitcard:
            rental_methods.append('TRANSITCARD')
        if self.rental_method_accountnumber:
            rental_methods.append('ACCOUNTNUMBER')
        if self.rental_method_phone:
            rental_methods.append('PHONE')
        return rental_methods

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
                    "capacity": self.capacity
                    }
                }
