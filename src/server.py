''' src.server '''
from os import environ

from flask import Flask, request, render_template, jsonify

from src.models import Station_Information
from src.utils.db_utils import get_session

app = Flask(__name__)
app.config.from_object(__name__)

MAPBOX_ACCESS_KEY = environ['MAPBOX_PUBLIC_TOKEN']


@app.route('/_get_status')
def get_status():
    station_id = request.args.get('station_id', 0, int)
    print(station_id)
    session = get_session()
    bikes_available, docks_available, last_updated = session\
        .query(Station_Information.num_bikes_available,
               Station_Information.num_docks_available,
               Station_Information.last_updated)\
        .filter(Station_Information.station_id == station_id).first()
    tstmp = last_updated.strftime('%b %d, %Y - %I:%M:%S %p')
    return jsonify(bikes=bikes_available, docks=docks_available, tstmp=tstmp)


@app.route('/')
def index():
    mapbox_url = 'mapbox://styles/carlps/cj6qydf6v3xju2rpqsre0immg'
    return render_template('index.html',
                           ACCESS_KEY=MAPBOX_ACCESS_KEY,
                           mapbox_url=mapbox_url)
