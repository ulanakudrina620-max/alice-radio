from flask import Flask, request, jsonify

app = Flask(__name__)

# 🎧 радиостанции Нью-Йорка
RADIO = {
    "1010 wins": "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3",
    "bloomberg": "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac",
    "wnyc": "https://fm939.wnyc.org/wnycfm"
}

current_station = "1010 wins"


@app.route("/", methods=["POST", "GET"])
def main():
    global current_station

    data = request.get_json(silent=True)
    command = ""

    if data and "request" in data:
        command = data["request"].get("command", "").lower()

    response_text = "Не понял команду"

    # 🎙 команды
    if "новости" in command or "news" in command:
        current_station = "1010 wins"
        response_text = "Включаю новости Нью-Йорка — 1010 WINS"

    elif "блумберг" in command or "bloomberg" in command:
        current_station = "bloomberg"
        response_text = "Включаю Bloomberg Radio"

    elif "wnyc" in command:
        current_station = "wnyc"
        response_text = "Включаю WNYC"

    elif "радио" in command or "нью-йорк" in command:
        response_text = "Радио Нью-Йорк. Скажи: новости, Bloomberg или WNYC"

    elif "следующая" in command:
        stations = list(RADIO.keys())
        idx = (stations.index(current_station) + 1) % len(stations)
        current_station = stations[idx]
        response_text = f"Переключаю на {current_station}"

    else:
        response_text = "Скажи: включи новости, Bloomberg или WNYC"

    return jsonify({
        "response": {
            "text": response_text,
            "end_session": False
        },
        "station": current_station,
        "stream_url": RADIO[current_station]
    })
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)