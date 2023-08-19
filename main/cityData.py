from flask import Blueprint, jsonify
import csv

cityData = Blueprint("cityData", __name__)

@cityData.route("/get/data/<city>")
def get_city_data(city):
    city_data = {}
    with open("./assets/city.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["City"].lower() == city.lower():
                city_data = {'city':row["City"],
                                  'population_density':row['Population_Density'],
                                  'unemployment_rate':row["Unemployment_Rate"],
                                  'clean_water_availability':row['Clean_Water_Availability'],
                                  'Air_Quality_Index':row["Air_Quality_Index"],
                                  'literacy_rate':f'{row["Literacy_Rate"]}',
                                  'crime_rate':row["Crime_Rate"],
                                  'Average_Temperature_Rate':row["Average_Temperature_Rate"],
                                  
                            }
                return city_data
    return jsonify("city not in db")