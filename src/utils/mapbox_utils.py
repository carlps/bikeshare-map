''' src.utils.mapbox_utils
    Common functions for interfacing with mapbox
'''

from mapbox import Datasets


def create_dataset(name, description):
    ''' Creates a new empty dataset with name and description.
        Returns newly created dataset object.
    '''
    datasets = Datasets()
    return datasets.create(name=name, description=description)


def insert_or_update_features(dataset_id, features):
    ''' Takes a list of features (dictionaries formatted as features)
        and adds them to dataset. If the ID of the feature is already
        in the dataset, it will be updated. If it's new, it will be inserted.
        Returns list of updated features.
        Will raise error if response is not 200.
    '''
    datasets = Datasets()
    loads = []
    for feature in features:
        resp = datasets.update_feature(dataset_id, feature['id'], feature)
        if resp.status_code != 200:
            err = (f'Response was {resp.status_code} when trying to',
                   f'update {feature} in dataset with ID {dataset_id}',
                   f'{resp.json()["message"]}')
            
            raise RuntimeError(err)
        loads.append(resp)
    return loads


def get_features(dataset_id):
    ''' Takes the ID of a dataset and returns a dict with all
        the features in the dataset
    '''
    datasets = Datasets()
    return datasets.list_features(dataset_id).json()


def get_feature(dataset_id, feature_id):
    ''' Takes the ID of a dataset and ID of a feature.
        Returns the feature in dict.
    '''
    datasets = Datasets()
    return datasets.read_feature(dataset_id, feature_id).json()


if __name__ == '__main__':
    print("Yo dog. This is a util. Nothing to run here. Try importing.")
