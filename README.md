# Bikeshare Map
This was a quick project to plot out bikeshare stations using [Mapbox](https://www.mapbox.com)

The application uses a Flask server to connect to a Postgres DB, which is maintaining the latest data from Capital Bikeshare.

When a user clicks on a bikeshare icon in the map, the server looks up the latest status of the station and presents it as a popup.

![screenshot of map with station clicked](/doc/screenshot.png)