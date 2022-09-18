from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from nanoid import generate
from flask_cors import CORS
import os
from mvg_api import *
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

@app.get("/")
def index():
    stationName = "hauptbahnof"
    date=datetime.now().strftime("%d/%m %H:%M:%S")
    station = get_departures(station_id="de:09162:9")
    for departure in station:
        departure["destination"] = (
            departure["destination"].replace("ß", "ss").replace("ü", "UE").upper()
        )
        departure["lineBackgroundColor"] = departure["lineBackgroundColor"].split(",")

    return render_template("index.html", stationName=stationName,date=date, station=station)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# https://www.mvg.de/api/fahrinfo/departure/de:09162:104
