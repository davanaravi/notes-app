from flask import Flask, jsonify, request

app = Flask(__name__)
notes = []

@app.route("/")
def home():
    return "Notes Microservice is running"

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json
    notes.append(data.get("note"))
    return {"message": "Note added"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
