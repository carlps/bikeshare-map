''' src.mapping.create_and_load_stations_dataset
    Uses utils to create stations dataset and then
    load it with station features
'''
from ..models import Station_Information
from ..utils.db_utils import get_session
from ..utils.mapbox_utils import create_dataset, insert_or_update_features


def get_stations_as_feature_dicts():
    ''' Get all station objects from DB.
        Returns list of dicts formatted to load as features
    '''
    session = get_session()
    stations = session.query(Station_Information).all()
    return [station.to_feature() for station in stations]


def main():
    stations = get_stations_as_feature_dicts()
    print('Got stations from DB.')
    ds_name = 'dc_bikeshare_stations'
    ds_description = 'Capital Bikeshare stations in the DC area.'
    dataset = create_dataset(ds_name, ds_description)
    ds_id = dataset.json()['id']
    print(f'Created station {ds_name} with ID {ds_id}')
    features = insert_or_update_features(ds_id, stations)
    print('Loaded stations into dataset.')


if __name__ == '__main__':
    main()
