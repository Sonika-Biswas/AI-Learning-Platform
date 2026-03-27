from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {}
roadmaps = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data["email"]
    password = data["password"]

    if email in users:
        return jsonify({"msg": "User already exists"}), 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[email] = hashed_pw

    return jsonify({"msg": "User registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    if email not in users:
        return jsonify({"msg": "User not found"}), 401

    if not bcrypt.checkpw(password.encode('utf-8'), users[email]):
        return jsonify({"msg": "Wrong password"}), 401

    token = create_access_token(identity=email)

    return jsonify({"access_token": token})

@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user = get_jwt_identity()
    return jsonify({"logged_in_as": user})

@app.route("/")
def home():
    return "AI Learning Platform Running!"

@app.route("/generate-roadmap", methods=["POST"])
@jwt_required()

def generate_roadmap():
    user = get_jwt_identity()
    data = request.json
    topic = data.get("topic")

    # Temporary fake AI response (we'll replace with real AI later)
    roadmap = [
        f"Introduction to {topic}",
        f"Basics of {topic}",
        f"Intermediate {topic}",
        f"Advanced {topic}",
        f"Projects in {topic}"
    ]

    return jsonify({"roadmap": roadmap})

if __name__ == "__main__":
    app.run(debug=True)