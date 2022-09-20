from flask import Flask, request, render_template
from mvg_api import *
from datetime import datetime

app = Flask(__name__)


@app.get("/")
def index():
    date = datetime.now().strftime("%d/%m %H:%M:%S")
    station = []
    for departure in station:
        departure["destination"] = (
            departure["destination"].replace("ß", "ss").replace("ü", "UE").upper()
        )
        departure["lineBackgroundColor"] = departure["lineBackgroundColor"].split(",")

    return render_template("index.html", date=date, station=station)


@app.get("/<path:path>")
def station(path):
    date = datetime.now().strftime("%d/%m %H:%M:%S")

    station = get_departures(station_id=path)
    for departure in station:
        departure["destination"] = (
            departure["destination"].replace("ß", "ss").replace("ü", "UE").upper()
        )
        departure["lineBackgroundColor"] = departure["lineBackgroundColor"].split(",")
        if departure["lineBackgroundColor"][0] == "#000000":
            departure["lineBackgroundColor"][0] = "#ffffff"

    return render_template("station.html", station=station, date=date, id=path)


@app.get("/search")
def search():
    input = request.args.get("q")
    if input:
        results = get_locations(input)
    else:
        results = []
    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
