''' src.utils
    Common functions used for database
'''
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session(echo=False):
    ''' Create db connection and sqlalchemy engine
        Return a session to interact with db

        Echo defaults to False, but if you want for debugging,
        just pass echo=True and sql statements will print to console

        For explanation of environment variables see
        file required_environment_variables in project root
    '''
    pg_user = environ['MAPS_USER']
    pg_pw = environ['MAPS_USER_PW']
    host = environ['BS_DB_HOST']
    port = environ['PSQL_PORT']
    db = environ['BS_DB']

    engine = create_engine(f'postgres://{pg_user}:{pg_pw}@{host}:{port}/{db}',
                            echo=echo)
    Session = sessionmaker(bind=engine)

    return Session()


if __name__ == '__main__':
    print('Why are you running this? It should only be imported.')
