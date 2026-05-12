from flask import Flask, request, jsonify

app = Flask(__name__)

RADIO = {
    "1010 wins": "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3",
    "bloomberg": "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac",
    "wnyc": "https://fm939.wnyc.org/wnycfm"
}

current_station = "1010 wins"


@app.route("/", methods=["POST", "GET"])
def main():
    global current_station

    data = request.get_json(silent=True) or {}
    command = data.get("request", {}).get("command", "").lower()

    text = "Скажи: новости, Bloomberg или WNYC"

    if "новости" in command or "news" in command:
        current_station = "1010 wins"
        text = "Включаю новости Нью-Йорка — 1010 WINS"

    elif "блумберг" in command or "bloomberg" in command:
        current_station = "bloomberg"
        text = "Включаю Bloomberg Radio"

    elif "wnyc" in command:
        current_station = "wnyc"
        text = "Включаю WNYC"

    elif "следующая" in command:
        keys = list(RADIO.keys())
        idx = (keys.index(current_station) + 1) % len(keys)
        current_station = keys[idx]
        text = f"Переключаю на {current_station}"

    return jsonify({
        "response": {
            "text": text,
            "end_session": False
        },
        "station": current_station,
        "stream_url": RADIO[current_station]
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)