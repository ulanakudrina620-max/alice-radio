from flask import Flask, request, jsonify
import os

app = Flask(__name__)

RADIO = {
    "1010 wins": "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3",
    "bloomberg": "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac",
    "wnyc": "https://fm939.wnyc.org/wnycfm"
}

current_station = "1010 wins"

@app.route("/", methods=["GET", "POST"])
def main():
    global current_station

    data = request.get_json(silent=True) or {}
    command = data.get("request", {}).get("command", "").lower()

    text = "Скажи: новости, bloomberg или wnyc"

    if "новости" in command:
        current_station = "1010 wins"
        text = "Включаю новости Нью-Йорка"

    elif "bloomberg" in command:
        current_station = "bloomberg"
        text = "Включаю Bloomberg"

    elif "wnyc" in command:
        current_station = "wnyc"
        text = "Включаю WNYC"

    return jsonify({
        "response": {
            "text": text,
            "end_session": False
        },
        "station": current_station,
        "stream_url": RADIO[current_station]
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
