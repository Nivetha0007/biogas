from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Initial values shown on UI
latest_data = {
    "temp_c": "--",
    "temp_f": "--",
    "pressure1": "--",
    "pressure2": "--",
    "pressure3": "--",
    "ph": "--"
}

@app.route("/update", methods=["POST"])
def update_data():
    global latest_data
    data = request.get_json()

    print("📡 Received POST from ESP:")
    for key, value in data.items():
        print(f" - {key}: {value}")

    expected_keys = set(latest_data.keys())

    # Check if all expected keys are present in ESP data
    if expected_keys.issubset(data):
        latest_data.update(data)
        return jsonify({"status": "success"}), 200
    else:
        missing = expected_keys - data.keys()
        print("❌ Missing fields:", missing)
        return jsonify({"status": "error", "message": f"Missing fields: {missing}"}), 400

@app.route("/data")
def fetch_data():
    return jsonify(latest_data)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # 🟢 Make accessible to ESP over LAN
