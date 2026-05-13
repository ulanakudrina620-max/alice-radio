from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 СТАНЦИИ (СТАБИЛЬНЫЕ)
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

    "bbcnews": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_world_service"
    ],

    # 🗽 NYC MUSIC
    "z100": [
        "https://stream.revma.ihrhls.com/zc153"
    ],

    "hot97": [
        "https://stream.revma.ihrhls.com/zc142"
    ],

    "litefm": [
        "https://stream.revma.ihrhls.com/zc150"
    ],

    # 🎧 2000s
    "2000s_hits": [
        "https://listen.181fm.com/181-2000s_128k.mp3"
    ],

    "2000s_rock": [
        "https://listen.181fm.com/181-buzz_128k.mp3"
    ],

    "2000s_party": [
        "https://listen.181fm.com/181-party_128k.mp3"
    ],

    # 💃 CLASSIC (ABBA / Beatles / Disco)
    "oldies": [
        "https://listen.181fm.com/181-goodtime_128k.mp3"
    ],

    "beatles": [
        "https://listen.181fm.com/181-beatles_128k.mp3"
    ],

    "disco": [
        "https://ice1.somafm.com/beatblender-128-mp3"
    ],

    "classic_rock": [
        "https://ice1.somafm.com/classicvibes-128-mp3"
    ],

    # 🎶 MODERN
    "bbc1": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"
    ],

    "bbc2": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_two"
    ],

    "soma": [
        "https://ice1.somafm.com/groovesalad-128-mp3"
    ],

    "lofi": [
        "https://ice1.somafm.com/beatblender-128-mp3"
    ]
}


# 🎨 СПОТИФАЙ-ДИЗАЙН
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
    font-family: Arial;
    background: radial-gradient(circle at top, #1a1a2e, #000);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}}

.container {{
    width: 420px;
    padding: 20px;
}}

h1 {{
    text-align: center;
    font-size: 22px;
    margin-bottom: 20px;
}}

.section {{
    margin-bottom: 20px;
}}

.section-title {{
    font-size: 12px;
    opacity: 0.6;
    margin-bottom: 10px;
    text-transform: uppercase;
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}}

.card {{
    background: rgba(255,255,255,0.06);
    padding: 14px;
    border-radius: 14px;
    cursor: pointer;
    text-align: center;
    transition: 0.2s;
    border: 1px solid rgba(255,255,255,0.1);
}}

.card:hover {{
    transform: scale(1.05);
    background: rgba(255,255,255,0.12);
}}

.news {{ color: #ff4d4d; }}
.nyc {{ color: #ff884d; }}
.music {{ color: #4da6ff; }}
.old {{ color: #ffcc00; }}
.alt {{ color: #66ccff; }}

audio {{
    width: 100%;
    margin-top: 15px;
}}
</style>
</head>

<body>

<div class="container">

<h1>🎧 Radio World+ NYC</h1>

<!-- NEWS -->
<div class="section">
<div class="section-title">News</div>
<div class="grid">

<div class="card news" onclick="play('news')">1010 WINS</div>
<div class="card news" onclick="play('bloomberg')">Bloomberg</div>
<div class="card news" onclick="play('wnyc')">WNYC</div>
<div class="card news" onclick="play('bbcnews')">BBC World</div>

</div>
</div>

<!-- NYC -->
<div class="section">
<div class="section-title">NYC Hits</div>
<div class="grid">

<div class="card nyc" onclick="play('z100')">Z100</div>
<div class="card nyc" onclick="play('hot97')">Hot 97</div>
<div class="card nyc" onclick="play('litefm')">Lite FM</div>

</div>
</div>

<!-- 2000s -->
<div class="section">
<div class="section-title">2000s Era</div>
<div class="grid">

<div class="card music" onclick="play('2000s_hits')">Hits</div>
<div class="card music" onclick="play('2000s_rock')">Rock</div>
<div class="card music" onclick="play('2000s_party')">Party</div>

</div>
</div>

<!-- CLASSIC -->
<div class="section">
<div class="section-title">Classic</div>
<div class="grid">

<div class="card old" onclick="play('oldies')">Oldies</div>
<div class="card old" onclick="play('beatles')">Beatles</div>
<div class="card old" onclick="play('disco')">ABBA</div>
<div class="card old" onclick="play('classic_rock')">Rock</div>

</div>
</div>

<!-- MODERN -->
<div class="section">
<div class="section-title">Modern</div>
<div class="grid">

<div class="card alt" onclick="play('bbc1')">BBC 1</div>
<div class="card alt" onclick="play('bbc2')">BBC 2</div>
<div class="card alt" onclick="play('soma')">SomaFM</div>
<div class="card alt" onclick="play('lofi')">LoFi</div>

</div>
</div>

<audio id="audio" controls autoplay></audio>

</div>

<script>
function play(station) {{

    const streams = {RADIO};

    let audio = document.getElementById("audio");
    let list = streams[station];
    let i = 0;

    function next() {{
        if (i >= list.length) return;

        audio.src = list[i];

        audio.play().catch(() => {{
            i++;
            next();
        }});

        let t = setTimeout(() => {{
            if (audio.readyState < 2) {{
                i++;
                next();
            }}
        }}, 5000);

        audio.onplaying = () => clearTimeout(t);
    }}

    next();
}}
</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "Радио работает",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)