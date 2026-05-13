from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 🎧 СТАБИЛЬНЫЕ СТАНЦИИ + НОВЫЕ
RADIO = {
    # 🗞️ NEWS
    "news": [
        "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3"
    ],

    "bloomberg": [
        "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac"
    ],

    "wnyc": [
        "https://fm939.wnyc.org/wnycfm"
    ],

    "cnn": [
        "https://tunein-icecast.mediaworks.nz/cnn"
    ],

    "bbcnews": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_world_service"
    ],

    # 🎶 MUSIC
    "bbc1": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one",
        "https://icecast.radiofrance.fr/fip-hifi.aac"
    ],

    "bbc2": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_two",
        "https://icecast.radiofrance.fr/fip-midfi.mp3"
    ],

    "soma": [
        "https://ice1.somafm.com/groovesalad-128-mp3",
        "https://ice1.somafm.com/dronezone-128-mp3"
    ],

    "lofi": [
        "https://streams.ilovemusic.de/iloveradio1.mp3",
        "https://ice1.somafm.com/beatblender-128-mp3"
    ],

    "dance": [
        "https://streaming.tdiradio.com:8000/hits.mp3",
        "https://ice1.somafm.com/spacestation-128-mp3"
    ]
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
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial;
    background: url("https://images.unsplash.com/photo-1522083165195-3424ed129620?auto=format&fit=crop&w=1400&q=80");
    background-size: cover;
    background-position: center;
    color: white;
}}

.card {{
    background: rgba(0,0,0,0.6);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    width: 360px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}}

h1 {{
    font-size: 22px;
    margin-bottom: 15px;
}}

button {{
    width: 100%;
    padding: 12px;
    margin: 6px 0;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    font-size: 15px;
    transition: 0.2s;
}}

button:hover {{
    transform: scale(1.05);
}}

.news {{ background: #ff4d4d; }}
.bloomberg {{ background: #4da6ff; }}
.wnyc {{ background: #4dff88; color: black; }}

.extra-news {{ background: #ff884d; }}

.bbc {{ background: #ffcc00; color: black; }}
.soma {{ background: #9966ff; }}
.lofi {{ background: #66ccff; color: black; }}
.dance {{ background: #ff66cc; }}

audio {{
    width: 100%;
    margin-top: 12px;
}}

</style>
</head>

<body>

<div class="card">
    <h1>🎧 New York Radio+</h1>

    <!-- 🗞️ NEWS -->
    <button class="news" onclick="play('news')">1010 WINS News</button>
    <button class="bloomberg" onclick="play('bloomberg')">Bloomberg</button>
    <button class="wnyc" onclick="play('wnyc')">WNYC</button>

    <button class="extra-news" onclick="play('cnn')">CNN Radio 📰</button>
    <button class="extra-news" onclick="play('bbcnews')">BBC World 🌍</button>

    <hr style="margin:10px 0; opacity:0.3;">

    <!-- 🎶 MUSIC -->
    <button class="bbc" onclick="play('bbc1')">BBC Radio 1 🎶</button>
    <button class="bbc" onclick="play('bbc2')">BBC Radio 2 🎧</button>
    <button class="soma" onclick="play('soma')">SomaFM 🌌</button>

    <button class="lofi" onclick="play('lofi')">LoFi Beats 🌙</button>
    <button class="dance" onclick="play('dance')">Dance Hits 🔥</button>

    <audio id="audio" controls autoplay></audio>
</div>

<script>
function play(station) {{

    const streams = {RADIO};

    let audio = document.getElementById("audio");
    let list = streams[station];
    let index = 0;

    function tryNext() {{
        if (index >= list.length) {{
            console.log("All streams failed:", station);
            return;
        }}

        let url = list[index];
        console.log("Trying:", url);

        audio.src = url;

        audio.play().catch(() => {{
            index++;
            tryNext();
        }});

        let timer = setTimeout(() => {{
            if (audio.readyState < 2) {{
                index++;
                tryNext();
            }}
        }}, 5000);

        audio.onplaying = () => {{
            clearTimeout(timer);
        }};
    }}

    tryNext();
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