from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "e41c8f7fdc56d8dc1d5d43eb8930c82a"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
