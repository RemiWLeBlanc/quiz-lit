""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask, render_template

import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (12.137752, 15.054325)
    folium_map = folium.Map(location=start_coords, tiles = 'cartodbpositron', zoom_start=4)


    africa = 'https://raw.githubusercontent.com/danielgrzenda/mBio/Elyse_geojson_subregion/data/GeoJSON/Natural_Earth/Africa_countries.json?token=AIHLCJ6DF77YPKI2DJ2GYALAEGFZS'

    folium.GeoJson(africa, name="africa_geojson").add_to(folium_map)
    folium.LayerControl().add_to(folium_map)

    #html_string = folium_map.get_root().render()

    folium_map.save('templates/map.html')
    return render_template('index.html') 
    #return folium_map._repr_html_()

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)

