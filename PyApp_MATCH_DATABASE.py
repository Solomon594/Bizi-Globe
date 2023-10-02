from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Set up SQLite database
def create_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS businesses (business_name TEXT, email TEXT, region TEXT, town TEXT, gps_coordinates TEXT, contact TEXT, product TEXT)")
    conn.commit()
    conn.close()

create_table()

@app.route("/store_data", methods=["POST"])
def store_data():
    data = request.json
    business_name = data.get("businessName")
    email = data.get("email")
    region = data.get("region")
    town = data.get("town")
    gps_coordinates = data.get("gpsCoordinates")
    contact = data.get("contact")
    product = data.get("product")

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO businesses (business_name, email, region, town, gps_coordinates, contact, product) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (business_name, email, region, town, gps_coordinates, contact, product))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data stored successfully"})

@app.route("/search_businesses", methods=["POST"])
def search_businesses():
    region = request.json.get("region")
    town = request.json.get("town")

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT business_name FROM businesses WHERE region = ? AND town = ?", (region, town))
    matching_businesses = [row[0] for row in cursor.fetchall()]
    conn.close()

    return jsonify({"matching_businesses": matching_businesses})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
