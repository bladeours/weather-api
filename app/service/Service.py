from datetime import datetime
import requests
from app.models import Weather
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


api_key = "f98b1e234b7ba5f3e83ddf8d2fe8e56e"


class Service:
    @staticmethod
    def hello():
        return "Hello World!"

    @staticmethod
    def get_current(lon, lat):
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        )
        weather = Service.convert_to_weather_from_openweathermap(r.json())
        Service.save_to_file(weather)
        return weather.__dict__

    @staticmethod
    def get_current_by_city(city):
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
        weather = Service.convert_to_weather_from_openweathermap(r.json())
        Service.save_to_file(weather)
        return weather.__dict__

    @staticmethod
    def get_historical(city, date):
        r = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json")
        r = requests.get(
            f'https://archive-api.open-meteo.com/v1/archive?latitude={r.json().get("results")[0].get("latitude")}&longitude={r.json().get("results")[0].get("longitude")}&start_date={date}&end_date={date}&hourly=relativehumidity_2m,weathercode,cloudcover&daily=temperature_2m_mean,apparent_temperature_mean,windspeed_10m_max&timezone=auto&min={date}&max={date}'
        )
        weather = Service.convert_to_weather_from_openmeteo(r.json(), city)
        Service.save_to_file(weather)
        return weather.__dict__

    @staticmethod
    def convert_to_weather_from_openmeteo(json, city):
        avg_humidity = round(sum(json.get("hourly").get("relativehumidity_2m")) / 24, 2)
        avg_cloudiness = sum(json.get("hourly").get("cloudcover")) / 24
        return Weather(
            json.get("daily").get("temperature_2m_mean")[0],
            avg_cloudiness,
            json.get("daily").get("apparent_temperature_mean")[0],
            json.get("daily").get("windspeed_10m_max")[0],
            avg_humidity,
            datetime.strptime(json.get("daily").get("time")[0], "%Y-%m-%d").strftime("%d-%m-%Y"),
            city,
        )

    @staticmethod
    def convert_to_weather_from_openweathermap(json):
        return Weather(
            json.get("main").get("temp"),
            json.get("clouds").get("all"),
            json.get("main").get("feels_like"),
            json.get("wind").get("speed"),
            json.get("main").get("humidity"),
            datetime.fromtimestamp(json.get("dt")).strftime("%d-%m-%Y"),
            json.get("name"),
        )

    @staticmethod
    def save_to_file(weather: Weather):
        with open("weather.csv", "a") as f:
            f.write(
                f"{weather.city},{weather.date},{weather.temperature},{weather.feels_like},{weather.cloudiness},{weather.wind_speed},{weather.humidity}\n"
            )

    @staticmethod
    def get_rain_chart(start_date, end_date, city):
        r = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json")
        r = requests.get(
            f'https://archive-api.open-meteo.com/v1/archive?latitude={r.json().get("results")[0].get("latitude")}&longitude={r.json().get("results")[0].get("longitude")}&start_date={start_date}&end_date={end_date}&daily=rain_sum&timezone=auto&min={start_date}&max={end_date}'
        )
    
        data = {"date": r.json().get("daily").get("time"), "rain": r.json().get("daily").get("rain_sum")}

        df = pd.DataFrame(data)

        plt.title("sum rain per day")
        plt.figure(figsize=(25, 6))
        sns.lineplot(x=df["date"], y=df["rain"])
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        return buffer

    @staticmethod
    def get_temperature_chart(start_date, end_date, city):
        r = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json")
        r = requests.get(
            f'https://archive-api.open-meteo.com/v1/archive?latitude={r.json().get("results")[0].get("latitude")}&longitude={r.json().get("results")[0].get("longitude")}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_mean&timezone=auto&min={start_date}&max={end_date}'
        )
        data = {
            "date": r.json().get("daily").get("time"),
            "temperature": r.json().get("daily").get("temperature_2m_mean"),
        }

        df = pd.DataFrame(data)

        plt.title("mean temperature per day")
        plt.figure(figsize=(25, 6))
        sns.lineplot(x=df["date"], y=df["temperature"])
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        return buffer
