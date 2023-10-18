from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Set up SQLite database
def create_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS businesses (business_name TEXT, email TEXT, region TEXT, town TEXT, gps_coordinates TEXT, contact TEXT)")
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

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO businesses (business_name, email, region, town, gps_coordinates, contact) VALUES (?, ?, ?, ?, ?, ?)",
                   (business_name, email, region, town, gps_coordinates, contact))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data stored successfully"})

if __name__ == "__main__":
    app.run(debug=True)
