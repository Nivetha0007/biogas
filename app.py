from flask import Flask, jsonify, render_template
import requests
import json

app = Flask(__name__)

ESP8266_IP = "http://172.16.127.205/data"  # ESP's endpoint

@app.route("/data")
def fetch_esp_data():
    try:
        response = requests.get(ESP8266_IP, timeout=2)
        data = json.loads(response.text.strip())  # Strip extra chars
        return jsonify(data)
    except Exception as e:
        print("Error:", e)
        return jsonify({
            "ph": "--",
            "temperature": "--",
            "pressure1": "--",
            "pressure2": "--",
            "pressure3": "--"
        })

@app.route("/")
def index():
    return render_template("index.html")  # if using templates folder

if __name__ == "__main__":
    app.run(debug=True)
