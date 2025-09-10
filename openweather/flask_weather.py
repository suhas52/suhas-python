from flask import Flask, render_template, url_for, request
import weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    weather_status = None
    error_message = None
    if request.method == "POST":
        city = request.form.get("city")
        coords = weather.get_coords(city)
        if coords is None:
            error_message = "City not found or API error. Please try again."
        else:
            lat, lon = coords
            data = weather.get_weather_data(lat, lon)
            if data is None:
                error_message = "Could not fetch weather data. Try again later."
            else:
                weather_status = weather.parse_weather(data)
    return render_template("home.html", title="Home", weather_status=weather_status, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)