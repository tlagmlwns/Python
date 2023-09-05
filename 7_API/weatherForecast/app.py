from flask import Flask, render_template, request
import requests  # pip install requests
from urllib.parse import urlencode, unquote
import json
import csv
from dotenv import load_dotenv
import os

load_dotenv()
myWeatherKey = os.environ.get("WEATHER_FORECAST_KEY")
print(myWeatherKey)

app = Flask(__name__)  # Initialise app

# Config
#-----------------------------------------------------------
city_dict = {}

with open("C:\shj\Python\city.csv", mode="r",encoding='UTF8') as inp:
    reader = csv.reader(inp)
    city_dict = {rows[0]: rows[1] for rows in reader}

#print(city_dict)
#------------------------------------------------------------

def getWeather(city_id):
    url = "http://apis.data.go.kr/1360000/VilageFcstMsgService/getLandFcst"
    queryString = "?" + urlencode(
        {
            "ServiceKey": unquote(myWeatherKey),
            "pageNo": "1",
            "numOfRows": "10",
            "dataType": "JSON",
            "regId": city_id,
        }
    )

    response = requests.get(url + queryString)
    r_dict = json.loads(response.text)
    r_response = r_dict.get("response")
    r_body = r_response.get("body")
    r_item = r_body.get("items")

    item_list = r_item.get("item")

    for item in item_list:
        if item.get("numEf") == 1:
            temp = item.get("ta")
            weather = item.get("wf")
            break

    return temp, weather


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["name"]
        city_id = city_dict.get(city_name)
        print(city_id)

        if city_id == None:
            return render_template("index.html")

        temp, weather = getWeather(city_id)

        return render_template(
            "index.html",
            temp=temp,
            weather=weather,
            city_name=city_name,
        )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
