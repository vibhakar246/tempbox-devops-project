"""
TempBox - Temperature Data Aggregation API
A DevOps learning project that fetches temperature data from IoT sensors
"""

from flask import Flask, jsonify
import httpx
import os
import time
from datetime import datetime

app = Flask(__name__)
APP_VERSION = "1.0.0"
START_TIME = time.time()

# SenseBox IDs for temperature data
SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c"
]

@app.route('/health', methods=['GET'])
def health_check():
    """Kubernetes health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'app': 'TempBox',
        'version': APP_VERSION,
        'uptime_seconds': int(time.time() - START_TIME)
    })

@app.route('/version', methods=['GET'])
def get_version():
    """Return application version"""
    return jsonify({
        'app': 'TempBox',
        'version': APP_VERSION
    })

@app.route('/temperature', methods=['GET'])
def get_temperature():
    """Fetch average temperature from IoT sensors"""
    temperatures = []
    
    with httpx.Client(timeout=10.0) as client:
        for box_id in SENSEBOX_IDS:
            try:
                response = client.get(f"https://api.opensensemap.org/boxes/{box_id}")
                if response.status_code == 200:
                    data = response.json()
                    for sensor in data.get('sensors', []):
                        if 'temperatur' in sensor.get('title', '').lower():
                            if sensor.get('lastMeasurement', {}).get('value'):
                                temp = float(sensor['lastMeasurement']['value'])
                                temperatures.append(temp)
                            break
            except Exception as e:
                print(f"Error fetching sensor {box_id}: {e}")
                continue
    
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        return jsonify({
            'average_temperature_c': round(avg_temp, 2),
            'sensors_queried': len(temperatures),
            'timestamp': datetime.utcnow().isoformat()
        })
    else:
        return jsonify({'error': 'Could not fetch temperature data'}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
