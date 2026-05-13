from flask import Flask, request, jsonify
import os

app = Flask(__name__)

RADIO = {
    "news": "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3",
    "bloomberg": "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac",
    "wnyc": "https://fm939.wnyc.org/wnycfm"
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Alice Radio</title>
<style>
body {{
    background: black;
    color: white;
    font-family: Arial;
    text-align: center;
}}

button {{
    padding: 15px;
    margin: 10px;
    font-size: 18px;
    cursor: pointer;
}}

.player {{
    margin-top: 30px;
}}
</style>
</head>

<body>

<h1>🎧 New York Radio</h1>

<button onclick="play('news')">News</button>
<button onclick="play('bloomberg')">Bloomberg</button>
<button onclick="play('wnyc')">WNYC</button>

<div class="player">
    <audio id="audio" controls autoplay></audio>
</div>

<script>
function play(station) {{
    const streams = {{
        news: "{RADIO['news']}",
        bloomberg: "{RADIO['bloomberg']}",
        wnyc: "{RADIO['wnyc']}"
    }};

    let audio = document.getElementById("audio");
    audio.src = streams[station];
    audio.play();
}}
</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "Окей, радио готово",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)