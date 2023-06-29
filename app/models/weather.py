class Weather:
    def __init__(self, temperature, cloudiness, feels_like, wind_speed, humidity, date, city):
        self.temperature = temperature
        self.cloudiness = cloudiness
        self.feels_like = feels_like
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.date = date
        self.city = city

    def get_temperature(self):
        return self.temperature

    def get_cloudiness(self):
        return self.cloudiness

    def get_feels_like(self):
        return self.feels_like

    def get_wind_speed(self):
        return self.wind_speed

    def get_humidity(self):
        return self.humidity

    def get_date(self):
        return self.date

    def get_city(self):
        return self.city
