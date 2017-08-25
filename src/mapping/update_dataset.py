''' src.mapping.update_dataset
    Pass in a dataset_id and this script will update features
    to those from model Station_Information
'''
from ..models import Station_Information
from ..utils.db_utils import get_session
from ..utils.mapbox_utils import insert_or_update_features


def get_stations_as_feature_dicts():
    ''' Get all station objects from DB.
        Returns list of dicts formatted to load as features
    '''
    session = get_session()
    stations = session.query(Station_Information).all()
    return [station.to_feature() for station in stations]


def main(stations_dataset_id):
    stations = get_stations_as_feature_dicts()
    print('Got stations from DB.')
    features = insert_or_update_features(stations_dataset_id, stations)
    print('Updated stations in dataset.')
