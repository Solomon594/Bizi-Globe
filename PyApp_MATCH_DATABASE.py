from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)



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
