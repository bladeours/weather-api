from app.flask import app
from flask import request, send_file
from app.service import Service


class Controller:
    @app.route("/current", methods=["GET"])
    def current():
        if city := request.args.get("city"):
            return Service.get_current_by_city(city)

        lon = request.args.get("lon")
        lat = request.args.get("lat")
        return Service.get_current(lon, lat)

    @app.route("/historical", methods=["GET"])
    def historical():
        return Service.get_historical(request.args.get("city"), request.args.get("date"))

    @app.route("/chart/rain", methods=["GET"])
    def rain_chart():
        return send_file(
            Service.get_rain_chart(
                request.args.get("start_date"), request.args.get("end_date"), request.args.get("city")
            ),
            mimetype="image/png",
        )

    @app.route("/chart/temp", methods=["GET"])
    def temp_chart():
        return send_file(
            Service.get_temperature_chart(
                request.args.get("start_date"), request.args.get("end_date"), request.args.get("city")
            ),
            mimetype="image/png",
        )
