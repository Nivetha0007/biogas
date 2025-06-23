from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
latest_data = {
    "ph": "--",
    "temperature": "--",
    "pressure1": "--",
    "pressure2": "--",
    "pressure3": "--"
}

@app.route("/update", methods=["POST"])
def update_data():
    global latest_data
    data = request.get_json()
    print("Received:", data)
    latest_data = data
    return jsonify({"status": "success"})

@app.route("/data")
def fetch_esp_data():
    return jsonify(latest_data)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
