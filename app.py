from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 ВСЕ СТАНЦИИ (NYC + 2000s + CLASSIC + MODERN)
RADIO = {

    # 🗞️ NYC NEWS
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

    # 🗽 REAL NYC MUSIC STATIONS (актуальные)
    "z100": [
        "https://stream.revma.ihrhls.com/zc153"
    ],

    "hot97": [
        "https://stream.revma.ihrhls.com/zc142"
    ],

    "power105": [
        "https://stream.revma.ihrhls.com/zc143"
    ],

    "q104": [
        "https://stream.revma.ihrhls.com/zc154"
    ],

    "litefm": [
        "https://stream.revma.ihrhls.com/zc150"
    ],

    # 🎧 2000s MUSIC
    "2000s_hits": [
        "https://listen.181fm.com/181-2000s_128k.mp3"
    ],

    "2000s_rock": [
        "https://listen.181fm.com/181-buzz_128k.mp3"
    ],

    "2000s_party": [
        "https://listen.181fm.com/181-party_128k.mp3"
    ],

    "dance_2000s": [
        "https://radiorecord.hostingradio.ru/rr_main96.aacp"
    ],

    # 💃 CLASSIC (ABBA / Beatles / DISCO)
    "oldies": [
        "https://listen.181fm.com/181-goodtime_128k.mp3"
    ],

    "beatles": [
        "https://listen.181fm.com/181-beatles_128k.mp3"
    ],

    "disco": [
        "https://strm112.1.fm/disco_mobile_mp3"
    ],

    "classic_rock": [
        "https://ice1.somafm.com/classicvibes-128-mp3"
    ],

    # 🎶 MODERN STABLE MUSIC
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
    ]
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Radio World+</title>

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
    background: rgba(0,0,0,0.65);
    padding: 22px;
    border-radius: 20px;
    width: 380px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}}

h1 {{
    font-size: 20px;
    margin-bottom: 10px;
}}

button {{
    width: 100%;
    padding: 10px;
    margin: 4px 0;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 14px;
}}

.news {{ background: #ff4d4d; }}
.nyc {{ background: #ff884d; }}
.music {{ background: #4da6ff; }}
.old {{ background: #ffcc00; color: black; }}
.dance {{ background: #9966ff; }}
.alt {{ background: #66ccff; color: black; }}

audio {{
    width: 100%;
    margin-top: 10px;
}}

</style>
</head>

<body>

<div class="card">
    <h1>🎧 Radio World+ NYC</h1>

    <!-- 🗞️ NEWS -->
    <button class="news" onclick="play('news')">1010 WINS News</button>
    <button class="news" onclick="play('bloomberg')">Bloomberg</button>
    <button class="news" onclick="play('wnyc')">WNYC</button>
    <button class="news" onclick="play('cnn')">CNN Radio</button>
    <button class="news" onclick="play('bbcnews')">BBC World</button>

    <hr>

    <!-- 🗽 NYC MUSIC -->
    <button class="nyc" onclick="play('z100')">Z100 🔥 Pop NYC</button>
    <button class="nyc" onclick="play('hot97')">Hot 97 🎧 Hip-Hop</button>
    <button class="nyc" onclick="play('power105')">Power 105 💥</button>
    <button class="nyc" onclick="play('q104')">Q104 Rock 🎸</button>
    <button class="nyc" onclick="play('litefm')">Lite FM 🌙 Chill</button>

    <hr>

    <!-- 🎧 2000s -->
    <button class="music" onclick="play('2000s_hits')">2000s Hits 🎧</button>
    <button class="music" onclick="play('2000s_rock')">2000s Rock 🎸</button>
    <button class="music" onclick="play('2000s_party')">2000s Party 🔥</button>
    <button class="music" onclick="play('dance_2000s')">2000s Dance 💃</button>

    <hr>

    <!-- 💃 CLASSIC -->
    <button class="old" onclick="play('oldies')">Oldies 60–80 🎧</button>
    <button class="old" onclick="play('beatles')">The Beatles 🎸</button>
    <button class="dance" onclick="play('disco')">ABBA / Disco 💃</button>
    <button class="old" onclick="play('classic_rock')">Classic Rock ⚡</button>

    <hr>

    <!-- 🎶 MODERN -->
    <button class="music" onclick="play('bbc1')">BBC Radio 1</button>
    <button class="music" onclick="play('bbc2')">BBC Radio 2</button>
    <button class="alt" onclick="play('soma')">SomaFM 🌌</button>
    <button class="alt" onclick="play('lofi')">LoFi Beats 🌙</button>

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
            console.log("All failed:", station);
            return;
        }}

        let url = list[index];
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