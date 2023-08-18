from flask import Blueprint, jsonify
import csv

cityData = Blueprint("cityData", __name__)

@cityData.route("/get/data/<city>")
def get_city_data(city):
    city_data = []
    with open("./assets/city.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["city"].lower() == city.lower():
                city_data.append({'city':row["city"],
                                  'population_density':row["population_density"],
                                  'clear_water_availability':row["clear_water_availability"],
                                  'aqi':row["aqi"],
                                  'literacy_rate':row["literacy_rate"],
                                  'crime_rate':row["crime_rate"]
                                  })
                return city_data
    return jsonify("city not in db")