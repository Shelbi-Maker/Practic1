# weather_app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    api_key = 'your_openweather_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={f79f16cfcac1806dd7ea8e6a3761203a}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    return jsonify({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(debug=True)
