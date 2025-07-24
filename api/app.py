from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime
def format_unix_time(timestamp, timezone_offset):
    dt = datetime.utcfromtimestamp(timestamp + timezone_offset)
    return dt.strftime('%B %d, %Y, %I:%M:%S %p')  # Example: July 24, 2025, 06:31:40 AM
    
app = Flask(__name__)

API_KEY = "db9031e9507a688e4e3bbd0a4d122f37"

def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                weather_data = {
                    "city": data["name"],
                    "date": format_unix_time(data["dt"], data["timezone"]),
                    "temperature": kelvin_to_celsius(data["main"]["temp"]),
                    "weather": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "humidity": data["main"]["humidity"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                weather_data = {"error": data.get("message", "API Error")}
    return render_template("index.html", weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)