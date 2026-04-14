from flask import Flask, jsonify
from flask_cors import CORS
import cv2

from detect import detect_vehicles
from traffic_logic import get_signal

app = Flask(__name__)
CORS(app)

@app.route("/traffic")
def traffic():

    cap = cv2.VideoCapture(0)  # webcam

    ret, frame = cap.read()

    if not ret:
        cap.release()
        return jsonify({"error": "Camera not working"})

    # ✅ FIX: unpack both values
    count, processed_frame = detect_vehicles(frame)

    # ✅ Traffic logic
    signal = get_signal(count)

    # ✅ Release camera
    cap.release()

    return jsonify({
        "vehicle_count": count,
        "signal": signal,
        "emergency": False
    })

if __name__ == "__main__":
    app.run(debug=True)