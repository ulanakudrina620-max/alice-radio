from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

RADIO = {
    "news": "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3",
    "bloomberg": "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac",
    "wnyc": "https://fm939.wnyc.org/wnycfm"
}

current_station = "news"

<<<<<<< HEAD

@app.route("/", methods=["POST", "GET"])
def alice_webhook():
=======
@app.route("/", methods=["GET", "POST"])
def main():
>>>>>>> 6a5736caee0a7ee39ec2a494764f0ffa6e69f0c4
    global current_station

    data = request.get_json(silent=True) or {}

<<<<<<< HEAD
    command = ""
    if "request" in data:
        command = data["request"].get("command", "").lower()

    text = "Скажи: новости, bloomberg или wnyc"

    if "новости" in command or "news" in command:
        current_station = "news"
=======
    text = "Скажи: новости, bloomberg или wnyc"

    if "новости" in command:
        current_station = "1010 wins"
>>>>>>> 6a5736caee0a7ee39ec2a494764f0ffa6e69f0c4
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
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
